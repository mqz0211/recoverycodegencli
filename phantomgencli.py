import secrets
import os
import sys

# ASCII art banner
ASCII_BANNER = r"""

    ____  _________________________   __
   / __ \/ ____/ ____/ ____/ ____/ | / /
  / /_/ / __/ / /   / / __/ __/ /  |/ / 
 / _, _/ /___/ /___/ /_/ / /___/ /|  /  
/_/ |_/_____/\____/\____/_____/_/ |_/   
                                        

"""

WORDLIST_PATH = "english.txt"

def load_wordlist(path):
    if not os.path.exists(path):
        raise FileNotFoundError(f"Wordlist not found: {path}")
    with open(path, "r", encoding="utf-8") as f:
        return [word.strip() for word in f.readlines()]

def generate_mnemonic(wordlist, word_count):
    return " ".join(secrets.choice(wordlist) for _ in range(word_count))

def main():
    print(ASCII_BANNER)
    try:
        wordlist = load_wordlist(WORDLIST_PATH)
    except FileNotFoundError as e:
        print(e)
        sys.exit(1)

    count = 20
    word_count = 12
    for i in range(count):
        mnemonic = generate_mnemonic(wordlist, word_count)
        print(f"{i+1:02}: {mnemonic}")

if __name__ == "__main__":
    main()
