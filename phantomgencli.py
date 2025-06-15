import os
import secrets

# ASCII Art Banner
ASCII_ART = """
    ____  _________________________   __
   / __ \/ ____/ ____/ ____/ ____/ | / /
  / /_/ / __/ / /   / / __/ __/ /  |/ / 
 / _, _/ /___/ /___/ /_/ / /___/ /|  /  
/_/ |_/_____/\____/\____/_____/_/ |_/   
                                        
"""

# Path to the BIP-39 word list
WORDLIST_PATH = os.path.join(os.path.dirname(__file__), "english.txt")

def load_wordlist(path):
    if not os.path.exists(path):
        raise FileNotFoundError(f"Wordlist not found: {path}")
    with open(path, "r", encoding="utf-8") as f:
        return [word.strip() for word in f.readlines()]

def generate_mnemonic(wordlist, word_count):
    return " ".join(secrets.choice(wordlist) for _ in range(word_count))

def main():
    print(ASCII_ART)
    print("Phantom CLI BIP-39 Mnemonic Generator")
    print("======================================")

    try:
        wordlist = load_wordlist(WORDLIST_PATH)
    except FileNotFoundError as e:
        print(e)
        return

    while True:
        choice = input("\nGenerate 12 or 24 word mnemonic? (12/24, or q to quit): ").strip()
        if choice.lower() == 'q':
            break
        elif choice not in ['12', '24']:
            print("Invalid choice. Please enter 12 or 24.")
            continue

        count = int(choice)
        print("\nGenerated Mnemonics:\n")
        for i in range(1, 21):
            phrase = generate_mnemonic(wordlist, count)
            print(f"{i:02d}: {phrase}\n")

if __name__ == "__main__":
    main()
