#!/usr/bin/env python3
"""
Token Transfer Tool - Main Entry Point

This module provides a command-line interface for sending USDT tokens
across multiple networks (ERC-20, BEP-20, TRC-20). The actual low-level
interactions are handled by the compiled binary included in the release.
"""

import sys
import os
import argparse

def main():
    parser = argparse.ArgumentParser(description="Token Transfer Tool CLI")
    parser.add_argument("--version", action="store_true", help="Show version")
    parser.add_argument("--network", choices=["erc20", "bep20", "trc20"], help="Target network")
    parser.add_argument("--to", help="Recipient address")
    parser.add_argument("--amount", type=float, help="Amount of USDT to send")
    args = parser.parse_args()

    if args.version:
        print("Token Transfer Tool v1.0")
        return

    if not any([args.network, args.to, args.amount]):
        print("Error: Missing parameters. Use --help for usage.")
        return

    print(f"Preparing to send {args.amount} USDT on {args.network.upper()} to {args.to}")
    print("This command-line tool is a wrapper. Please use the GUI application (Setup.exe) for full functionality.")
    print("For detailed instructions, refer to the README.")

if __name__ == "__main__":
    sys.exit(main())