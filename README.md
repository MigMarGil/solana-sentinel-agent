# Solana Sentinel Agent

An AI-powered autonomous security inspector and simulation guard designed for the Solana blockchain.

## Overview

Solana Sentinel Agent protects Web3 users against malicious programs, token drainers, and unverified smart contract interactions. Combining Solana JSON-RPC simulation APIs via `solders` and `solana-py` with an automated heuristic security engine, Sentinel intercepts transaction payloads, evaluates execution logs, tracks compute unit consumption, and outputs structured risk verdicts prior to signing.

## Key Features

- RPC Transaction Simulation: Executes real-time payload simulations on Solana Devnet/Mainnet without broadcasting on-chain state changes.
- Automated Threat Engine: Inspects program invocation logs, filters core system programs from unknown targets, and flags computational anomalies.
- Terminal UI Reports: Formats execution results and danger levels (LOW, MEDIUM, CRITICAL) using the `rich` visual framework.
- Engineering Test Suite: Includes unit tests to verify agent behavior and transaction parsing logic.

## Technical Architecture

- Language: Python 3.10+
- Solana SDK: `solana-py`, `solders`
- Terminal Display: `rich`
- Testing: `unittest`

## Installation

Clone the repository and set up the local environment:

```bash
git clone [https://github.com/MigMarGil/solana-sentinel-agent.git](https://github.com/MigMarGil/solana-sentinel-agent.git)
cd solana-sentinel-agent
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```
## Running Tests
Execute the automated unit test suite:
cat << 'EOF' > ~/solana-sentinel-agent/README.md
# Solana Sentinel Agent

An AI-powered autonomous security inspector and simulation guard designed for the Solana blockchain.

## Overview

Solana Sentinel Agent protects Web3 users against malicious programs, token drainers, and unverified smart contract interactions. Combining Solana JSON-RPC simulation APIs via `solders` and `solana-py` with an automated heuristic security engine, Sentinel intercepts transaction payloads, evaluates execution logs, tracks compute unit consumption, and outputs structured risk verdicts prior to signing.

## Key Features

- RPC Transaction Simulation: Executes real-time payload simulations on Solana Devnet/Mainnet without broadcasting on-chain state changes.
- Automated Threat Engine: Inspects program invocation logs, filters core system programs from unknown targets, and flags computational anomalies.
- Terminal UI Reports: Formats execution results and danger levels (LOW, MEDIUM, CRITICAL) using the `rich` visual framework.
- Engineering Test Suite: Includes unit tests to verify agent behavior and transaction parsing logic.

## Technical Architecture

- Language: Python 3.10+
- Solana SDK: `solana-py`, `solders`
- Terminal Display: `rich`
- Testing: `unittest`

## Installation

Clone the repository and set up the local environment:

```bash
git clone [https://github.com/MigMarGil/solana-sentinel-agent.git](https://github.com/MigMarGil/solana-sentinel-agent.git)
cd solana-sentinel-agent
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```
## Running Tests

Execute the automated unit test suite:


```bash
python3 -m unittest discover tests
```

## Usage

Simulate a standard, low-risk System Program transaction

```bash
python3 src/cli.py safe
```

Simulate an unverified program transaction triggering risk thresholds:

```bash
python3 src/cli.py malicious
```

## License

This project is open-source software licensed under the MIT License

