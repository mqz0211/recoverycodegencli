#!/usr/bin/env python3
import secrets
import os
import argparse

# ASCII art logo
ASCII_ART = r"""
██████╗ ██████╗  ██████╗ ██████╗ ███████╗ ██████╗ ██████╗ ███████╗
██╔══██╗██╔══██╗██╔════╝ ██╔══██╗██╔════╝██╔════╝ ██╔══██╗██╔════╝
██████╔╝██████╔╝██║  ███╗██████╔╝█████╗  ██║  ███╗██████╔╝█████╗  
██╔═══╝ ██╔═══╝ ██║   ██║██╔═══╝ ██╔══╝  ██║   ██║██╔═══╝ ██╔══╝  
██║     ██║     ╚██████╔╝██║     ███████╗╚██████╔╝██║     ███████╗
╚═╝     ╚═╝      ╚═════╝ ╚═╝     ╚══════╝ ╚═════╝ ╚═╝     ╚══════╝
"""

WORDLIST_PATH = r"C:\Users\User\hash\english.txt"  # Adjust as needed

def load_wordlist(path):
    if not os.path.exists(path):
        raise FileNotFoundError(f"Wordlist not found: {path}")
    with open(path, "r", encoding="utf-8") as f:
        return [word.strip() for word in f.readlines()]

def generate_mnemonic(wordlist, word_count):
    return " ".join(secrets.choice(wordlist) for _ in range(word_count))

def main():
    parser = argparse.ArgumentParser(description="CLI BIP-39 Mnemonic Generator")
    parser.add_argument("-n", "--num", type=int, default=1, help="Number of mnemonics to generate")
    parser.add_argument("-w", "--words", type=int, choices=[12, 24], default=12, help="Number of words in each mnemonic")
    args = parser.parse_args()

    wordlist = load_wordlist(WORDLIST_PATH)

    print(ASCII_ART)
    print(f"Generating {args.num} mnemonic phrase(s), each with {args.words} words:\n")

    for i in range(args.num):
        print(f"{i+1:02d}: {generate_mnemonic(wordlist, args.words)}")

if __name__ == "__main__":
    main()
