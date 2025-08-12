from Crypto.Cipher import AES
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
