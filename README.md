# Solana Sentinel Agent

> An AI-powered autonomous security inspector and simulation guard designed for the Solana blockchain.

## Overview
Solana Sentinel Agent is built to protect Web3 users against malicious programs, token drainers, and unverified smart contract interactions. Leveraging Solana's JSON-RPC simulation API combined with a heuristic AI agent engine in Python, Sentinel intercepts incoming transactions, evaluates execution logs, tracks compute unit consumption, and issues immediate risk verdicts in natural language before users sign.

## Features
- RPC Simulation Integration: Connects directly to Solana Devnet/Mainnet to test transaction payloads without broadcast risk.
- AI Security Agent: Analyzes program invocation logs, filters trusted system programs vs. unknown/malicious contracts, and flags anomalous compute loads.
- Rich CLI Interface: Provides clean, structured terminal security reports categorized by risk levels (LOW, MEDIUM, CRITICAL).

## Tech Stack
- Language: Python 3.11+
- Blockchain Interface: Requests / Solana JSON-RPC
- Terminal UI: Rich

## Usage

1. Clone the repository and set up your virtual environment:
   git clone https://github.com/MigMarGil/solana-sentinel-agent.git
   cd solana-sentinel-agent
   python3 -m venv venv
   source venv/bin/activate
   pip install -r requirements.txt

2. Run the safe transaction simulation:
   python3 src/cli.py safe

3. Run the malicious transaction simulation:
   python3 src/cli.py malicious

## License
MIT License
