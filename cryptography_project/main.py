from algorithms import aes, rsa, sha

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
