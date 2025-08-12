from Crypto.PublicKey import RSA
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
