import sys
import time
from rich.console import Console
from rich.panel import Panel
from rich.table import Table
from solana_inspector import SolanaInspector
from ai_agent import SecurityAgent

console = Console()

def run_sentinel_demo(scenario: str = "safe"):
    console.print(Panel.fit("SOLANA SENTINEL AGENT\nAI Transaction Inspector & Safety Guard", border_style="cyan"))
    
    inspector = SolanaInspector()
    agent = SecurityAgent()

    console.print("\n[bold yellow][1/3] Connecting to Solana Devnet RPC...[/bold yellow]")
    account_info = inspector.get_account_info("11111111111111111111111111111111")
    
    if "result" in account_info:
        console.print("[bold green][OK] Connection established with Devnet.[/bold green]")
    else:
        console.print("[bold red][ERROR] RPC connection failed.[/bold red]")
        return

    console.print(f"\n[bold yellow][2/3] Simulating incoming transaction (Scenario: {scenario.upper()})...[/bold yellow]")
    
    if scenario == "malicious":
        mock_sim = {
            "result": {
                "value": {
                    "err": None,
                    "logs": [
                        "Program BadDrainer111111111111111111111111111111 invoke [1]",
                        "Program BadDrainer111111111111111111111111111111 failed: custom program error: 0x1"
                    ],
                    "unitsConsumed": 185000
                }
            }
        }
    else:
        mock_sim = {
            "result": {
                "value": {
                    "err": None,
                    "logs": [
                        "Program 11111111111111111111111111111111 invoke [1]",
                        "Program 11111111111111111111111111111111 success"
                    ],
                    "unitsConsumed": 150
                }
            }
        }
        
    time.sleep(1)

    console.print("\n[bold yellow][3/3] Running security analysis with AI Agent...[/bold yellow]")
    report = agent.analyze_simulation(mock_sim)
    time.sleep(1)

    table = Table(title=f"Security Verdict [{scenario.upper()}]", show_header=True, header_style="bold magenta")
    table.add_column("Metric", style="cyan")
    table.add_column("Result", style="white")

    color_map = {"LOW": "green", "MEDIUM": "yellow", "CRITICAL": "red"}
    sev_color = color_map.get(report["severity"], "white")

    table.add_row("Risk Level", f"[{sev_color}]{report['severity']}[/{sev_color}]")
    table.add_row("Risk Score (0-100)", str(report["risk_score"]))
    table.add_row("Recommendation", report["recommendation"])
    table.add_row("Risk Factors", ", ".join(report["risk_factors"]) if report["risk_factors"] else "None")
    table.add_row("Explanation", report["explanation"])

    console.print(table)

if __name__ == "__main__":
    scenario = "safe"
    if len(sys.argv) > 1 and sys.argv[1] in ["safe", "malicious"]:
        scenario = sys.argv[1]
    run_sentinel_demo(scenario)
