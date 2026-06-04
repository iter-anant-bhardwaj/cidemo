import os
import sys

def main():
    # Read the secret token from environment variables
    # (Secrets should always be passed to your code via environment variables, not hardcoded!)
    secret_token = os.environ.get("MY_SECRET_TOKEN")
    
    if not secret_token:
        print("[-] Error: MY_SECRET_TOKEN environment variable is not set!")
        print("    Please configure the secret in GitHub and ensure the workflow passes it.")
        sys.exit(1)
        
    print("[+] Successfully loaded MY_SECRET_TOKEN from environment.")
    print(f"[+] Secret token length: {len(secret_token)} characters")
    
    # We will print the secret here to demonstrate how GitHub Actions 
    # automatically masks secrets in the build logs.
    print(f"[i] Printing secret directly: {secret_token}")

if __name__ == "__main__":
    main()
