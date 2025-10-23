import sys
import time

def spinner():
    while True:
        for cursor in '|/-\\':
            yield cursor

def encrypt_password(password, shift=3):
    encrypted = ""
    spin = spinner()
    for i, char in enumerate(password):
        if char.isalpha():
            shift_base = ord('A') if char.isupper() else ord('a')
            encrypted_char = chr((ord(char) - shift_base + shift) % 26 + shift_base)
            encrypted += encrypted_char
        else:
            encrypted += char
        # Display spinner animation
        sys.stdout.write(f"\rEncrypting... {next(spin)}")
        sys.stdout.flush()
        time.sleep(0.05)  # simulate processing delay
    print("\rEncryption complete!    ")
    return encrypted

def decrypt_password(encrypted_password, shift=3):
    decrypted = ""
    spin = spinner()
    for i, char in enumerate(encrypted_password):
        if char.isalpha():
            shift_base = ord('A') if char.isupper() else ord('a')
            decrypted_char = chr((ord(char) - shift_base - shift) % 26 + shift_base)
            decrypted += decrypted_char
        else:
            decrypted += char
        # Display spinner animation
        sys.stdout.write(f"\rDecrypting... {next(spin)}")
        sys.stdout.flush()
        time.sleep(0.05)  # simulate processing delay
    print("\rDecryption complete!    ")
    return decrypted

def main():
    password = input("Enter your password: ")
    choice = input("Type 'E' to Encrypt or 'D' to Decrypt your password: ").upper()

    if choice == 'E':
        result = encrypt_password(password)
        print(f"Encrypted password: {result}")
    elif choice == 'D':
        result = decrypt_password(password)
        print(f"Decrypted password: {result}")
    else:
        print("Invalid choice! Please choose 'E' or 'D'.")

if __name__ == "__main__":
    main()
