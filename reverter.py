#fully made by chatgpt so i can safe time

import os
import shutil

def revert_files(folder):
    for root, _, files in os.walk(folder):
        for file in files:
            if file.endswith(".bak"):
                original_path = os.path.splitext(file)[0]  # Get the original file name (remove .bak)
                backup_path = os.path.join(root, file)
                
                # Check if the backup file exists
                if os.path.exists(backup_path):
                    shutil.copy(backup_path, original_path)
                    print(f"[+] Reverted changes for {original_path}")
                else:
                    print(f"[-] Backup file {file} not found. Skipping.")

folder = input("[+] Path to folder including files to revert.\n")
# Run revert function
revert_files(folder)
