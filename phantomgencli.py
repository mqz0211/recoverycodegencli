import secrets
import os
import time

# ASCII art logo
ASCII_ART = r"""
  ____  _     ___  ____  ____  ____  ____  ____ 

    ____  _________________________   __
   / __ \/ ____/ ____/ ____/ ____/ | / /
  / /_/ / __/ / /   / / __/ __/ /  |/ / 
 / _, _/ /___/ /___/ /_/ / /___/ /|  /  
/_/ |_/_____/\____/\____/_____/_/ |_/   
                                        

"""

# Load wordlist file
def load_wordlist(path):
    if not os.path.exists(path):
        raise FileNotFoundError(f"[ERROR] Wordlist not found: {path}")
    with open(path, "r", encoding="utf-8") as f:
        return [word.strip() for word in f.readlines()]

# Generate one mnemonic
def generate_mnemonic(wordlist, word_count):
    return " ".join(secrets.choice(wordlist) for _ in range(word_count))

def main():
    print(ASCII_ART)
    print("[INFO] Starting mnemonic generation...\n")

    # Use wordlist file from current directory
    wordlist_path = os.path.join(os.path.dirname(__file__), "english.txt")

    try:
        wordlist = load_wordlist(wordlist_path)
    except FileNotFoundError as e:
        print(e)
        return

    word_count = 12  # or change to 24 if desired
    num_phrases = 20

    for i in range(1, num_phrases + 1):
        phrase = generate_mnemonic(wordlist, word_count)
        print(f"[{i}] {phrase}")
        time.sleep(0.1)  # for smoother output

if __name__ == "__main__":
    main()
