import os  # Importing the 'os' module to interact with the file system
import hmac  # Importing 'hmac' for creating hash-based message authentication codes
import hashlib  # Importing 'hashlib' for cryptographic hash functions, like sha256

# Constants
SIGNING_KEY = "KEY*******"  # The secret key used for HMAC calculation (replace with actual key)
FOLDER_PATH = "."  # The path to the folder containing the message and HMAC files (current directory by default)
HMAC_EXT = ".hmac"  # The extension for HMAC files (e.g., message_1.txt would have message_1.hmac)

def compute_hmac(key, message):
    """
    Function to compute the HMAC (Hash-based Message Authentication Code) for a given message using SHA-256.
    
    :param key: The key used to sign the message (HMAC key).
    :param message: The message content to be hashed.
    :return: The computed HMAC in hexadecimal format.
    """
    return hmac.new(key.encode(), message.encode(), hashlib.sha256).hexdigest()
    # hmac.new() creates a new HMAC object, using the key and message, then applying SHA-256
    # .hexdigest() returns the hash as a hexadecimal string

def main():
    """
    Main function to iterate through the folder and check the HMACs for all message files.
    It compares the computed HMAC against the stored one in the corresponding .hmac file.
    """
    mismatch_count = 0  # A counter for how many files have mismatched HMACs
    total_files = 0  # A counter for the total number of message files checked

    print("Checking HMACs...\n")  # Output to indicate the start of the process

    # Loop over all files in the directory and sort them alphabetically
    for filename in sorted(os.listdir(FOLDER_PATH)):
        # Check if the file name starts with "message_" and ends with ".txt" (message files)
        if filename.startswith("message_") and filename.endswith(".txt"):
            total_files += 1  # Increment the total files counter as we're processing a message file
            # Construct the full file path for the .txt message file
            txt_path = os.path.join(FOLDER_PATH, filename)
            # Construct the full file path for the corresponding .hmac file
            hmac_path = os.path.join(FOLDER_PATH, filename.replace(".txt", HMAC_EXT))

            # Open the message file and read its content
            with open(txt_path, "r") as f:
                message_content = f.read()  # Read the entire content of the message file

            # Compute the HMAC for the message content using the secret signing key
            computed = compute_hmac(SIGNING_KEY, message_content)

            # Try to open the corresponding .hmac file to read the stored HMAC
            try:
                with open(hmac_path, "r") as f:
                    stored = f.read().strip()  # Read the stored HMAC and remove any surrounding whitespace
            except FileNotFoundError:
                # If the .hmac file is missing, handle the error gracefully
                stored = "(missing)"  # Mark it as missing if the .hmac file doesn't exist
                print(f"[!] {filename} has no .hmac file.")  # Alert the user
                mismatch_count += 1  # Increment the mismatch count since no HMAC file exists
                continue  # Skip to the next file in the loop

            # Compare the computed HMAC with the stored HMAC
            if computed != stored:
                # If they do not match, print the file name and both HMACs for comparison
                print(f"[✘] {filename}")
                print(f"     Stored:   {stored}")  # Show the stored (possibly incorrect) HMAC
                print(f"     Computed: {computed}")  # Show the computed (correct) HMAC
                mismatch_count += 1  # Increment the mismatch counter
            else:
                # If they match, indicate that the HMAC verification succeeded
                print(f"[✓] {filename} - HMAC matches.")

    # Print a summary of the checks performed
    print("\nSummary:")
    print(f"Total messages checked: {total_files}")  # Display how many files were checked
    print(f"HMAC mismatches found: {mismatch_count}")  # Display how many mismatches were found

# Ensure the main function runs when the script is executed directly
if __name__ == "__main__":
    main()  # Call the main function to start the process
