import os

# Project folder structure
project_name = "cryptography_project"
folders = [
    project_name,
    f"{project_name}/algorithms",
    f"{project_name}/data",
]

files = {
    f"{project_name}/README.md": "# Cryptography Project\nThis project implements AES, RSA, and SHA algorithms in Python.",
    
    f"{project_name}/requirements.txt": "pycryptodome\n",

    f"{project_name}/main.py": """from algorithms import aes, rsa, sha

def main():
    print("=== Cryptography Project ===")
    print("Choose an algorithm:")
    print("1. AES Encryption/Decryption")
    print("2. RSA Encryption/Decryption")
    print("3. SHA Hashing")

    choice = input("Enter choice: ")

    if choice == "1":
        aes.run_aes_demo()
    elif choice == "2":
        rsa.run_rsa_demo()
    elif choice == "3":
        sha.run_sha_demo()
    else:
        print("Invalid choice.")

if __name__ == "__main__":
    main()
""",

    f"{project_name}/algorithms/aes.py": """from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes
import base64

def run_aes_demo():
    data = input("Enter text to encrypt: ").encode()
    key = get_random_bytes(16)
    cipher = AES.new(key, AES.MODE_EAX)
    ciphertext, tag = cipher.encrypt_and_digest(data)

    print(f"Key: {base64.b64encode(key).decode()}")
    print(f"Ciphertext: {base64.b64encode(ciphertext).decode()}")

    # Decrypt
    cipher_dec = AES.new(key, AES.MODE_EAX, nonce=cipher.nonce)
    plaintext = cipher_dec.decrypt(ciphertext)
    print(f"Decrypted text: {plaintext.decode()}")
""",

    f"{project_name}/algorithms/rsa.py": """from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP
import base64

def run_rsa_demo():
    key = RSA.generate(2048)
    public_key = key.publickey()

    data = input("Enter text to encrypt: ").encode()

    cipher = PKCS1_OAEP.new(public_key)
    ciphertext = cipher.encrypt(data)

    print(f"Ciphertext: {base64.b64encode(ciphertext).decode()}")

    # Decrypt
    cipher_dec = PKCS1_OAEP.new(key)
    plaintext = cipher_dec.decrypt(ciphertext)
    print(f"Decrypted text: {plaintext.decode()}")
""",

    f"{project_name}/algorithms/sha.py": """import hashlib

def run_sha_demo():
    data = input("Enter text to hash: ").encode()
    sha_hash = hashlib.sha256(data).hexdigest()
    print(f"SHA-256 Hash: {sha_hash}")
"""
}

# Create folders
for folder in folders:
    os.makedirs(folder, exist_ok=True)

# Create files with content
for path, content in files.items():
    with open(path, "w", encoding="utf-8") as f:
        f.write(content)

print(f"✅ Project '{project_name}' scaffold created successfully.")
