#this code is horrible. backup stuff is written by chat gpt. 
#does the job ig.

import os
import re
import shutil  

def clean_files(folder, ext):
    pattern = re.compile(r'(?<=http).*?\.onion')  # Regex to find text between 'http' and '.onion' #ty chat gpt
    
    for root, _, files in os.walk(folder):
        for file in files:
            print("[+] Scanning for files ending in your chosen extension.")
            
            if file.endswith(ext):
                path = os.path.join(root, file)
                backup_path = f"{path}.bak" 
                
                shutil.copy(path, backup_path)
                print(f"[+] Backup created for {file}")
                
                with open(path, 'r', encoding='utf-8') as f:
                    content = f.read()

                print("[+] Attempting to read file.")
                
                content = pattern.sub("REDACTED", content)
                print("[+] Attempting to redact URLs.")
                
                with open(path, 'w', encoding='utf-8') as f:
                    f.write(content)
                    print(f"[+] Writing redacted content to {file}")

folder = input("[+] Path to folder including files. \n")
ext = input("[+] Extension to scan and redact. \n")
#run
clean_files(folder, ext)
