import hashlib

def run_sha_demo():
    data = input("Enter text to hash: ").encode()
    sha_hash = hashlib.sha256(data).hexdigest()
    print(f"SHA-256 Hash: {sha_hash}")
