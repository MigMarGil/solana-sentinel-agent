import os
import json
import requests
from dotenv import load_dotenv
from solders.pubkey import Pubkey
from solders.system_program import transfer, TransferParams
from solders.message import Message
from solders.transaction import Transaction
from solders.keypair import Keypair

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

    def generate_sample_transfer_tx_b64(self) -> str:
        # Generates a valid real serialized Solana transaction for testing simulation via RPC
        sender = Keypair()
        receiver = Pubkey.from_string("11111111111111111111111111111111")
        
        instruction = transfer(
            TransferParams(
                from_pubkey=sender.pubkey(),
                to_pubkey=receiver,
                lamports=1000
            )
        )
        
        # Fetch recent blockhash or use a dummy valid base58 for simulation payload structure
        # Using a dummy blockhash standard for simulation payload testing
        msg = Message.new_with_blockhash(
            [instruction],
            sender.pubkey(),
            Pubkey.from_string("11111111111111111111111111111111")
        )
        tx = Transaction([sender], msg, sender.pubkey())
        import base64
        return base64.b64encode(bytes(tx)).decode('utf-8')

if __name__ == "__main__":
    inspector = SolanaInspector()
    info = inspector.get_account_info("11111111111111111111111111111111")
    print("Devnet RPC Status:", "OK" if "result" in info else "Error")
