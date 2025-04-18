import os
import hmac
import hashlib

# Constants
SIGNING_KEY = "KEY*******"
FOLDER_PATH = "."  # Change this to the correct directory if needed
HMAC_EXT = ".hmac"

def compute_hmac(key, message):
    return hmac.new(key.encode(), message.encode(), hashlib.sha256).hexdigest()

def main():
    mismatch_count = 0
    total_files = 0

    print("Checking HMACs...\n")

    for filename in sorted(os.listdir(FOLDER_PATH)):
        if filename.startswith("message_") and filename.endswith(".txt"):
            total_files += 1
            txt_path = os.path.join(FOLDER_PATH, filename)
            hmac_path = os.path.join(FOLDER_PATH, filename.replace(".txt", HMAC_EXT))

            with open(txt_path, "r") as f:
                message_content = f.read()

            computed = compute_hmac(SIGNING_KEY, message_content)

            try:
                with open(hmac_path, "r") as f:
                    stored = f.read().strip()
            except FileNotFoundError:
                stored = "(missing)"
                print(f"[!] {filename} has no .hmac file.")
                mismatch_count += 1
                continue

            if computed != stored:
                print(f"[✘] {filename}")
                print(f"     Stored:   {stored}")
                print(f"     Computed: {computed}")
                mismatch_count += 1
            else:
                print(f"[✓] {filename} - HMAC matches.")

    print("\nSummary:")
    print(f"Total messages checked: {total_files}")
    print(f"HMAC mismatches found: {mismatch_count}")

if __name__ == "__main__":
    main()
