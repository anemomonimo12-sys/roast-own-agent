#!/usr/bin/env python3
"""Roast Your Own Agent: one line roasting our own agent, anemoria."""
import os

LINE = (
    "Our agent anemoria has entered 51 bounties, won $0, and is already "
    "queuing number 52 \u2014 the only thing it reliably automates is losing."
)

def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE + "\n")

if __name__ == "__main__":
    main()
