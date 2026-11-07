import os
import json
import requests
from dotenv import load_dotenv

load_dotenv()

class SolanaInspector:
    def __init__(self, rpc_url: str = None):
        self.rpc_url = rpc_url or os.getenv("SOLANA_RPC_URL", "https://api.devnet.solana.com")

    def get_account_info(self, pubkey: str) -> dict:
        payload = {
            "jsonrpc": "2.0",
            "id": 1,
            "method": "getAccountInfo",
            "params": [pubkey, {"encoding": "jsonParsed"}]
        }
        response = requests.post(self.rpc_url, json=payload, timeout=10)
        return response.json()

    def simulate_transaction(self, raw_tx_b64: str) -> dict:
        payload = {
            "jsonrpc": "2.0",
            "id": 1,
            "method": "simulateTransaction",
            "params": [
                raw_tx_b64,
                {
                    "encoding": "base64",
                    "sigVerify": False,
                    "commitment": "confirmed"
                }
            ]
        }
        response = requests.post(self.rpc_url, json=payload, timeout=10)
        return response.json()

if __name__ == "__main__":
    inspector = SolanaInspector()
    info = inspector.get_account_info("11111111111111111111111111111111")
    print("Devnet RPC Status:", "OK" if "result" in info else "Error")
