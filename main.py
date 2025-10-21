def encrypt_password(password, shift=3):
    encrypted = ""
    for char in password:   
        if char.isalpha():
            shift_base = ord('A') if char.isupper() else ord('a')
            encrypted_char = chr((ord(char) - shift_base + shift) % 26 + shift_base)
            encrypted += encrypted_char
        else:
            encrypted += char
    return encrypted

def decrypt_password(encrypted_password, shift=3):
    decrypted = ""
    for char in encrypted_password:
        if char.isalpha():
            shift_base = ord('A') if char.isupper() else ord('a')
            decrypted_char = chr((ord(char) - shift_base - shift) % 26 + shift_base)
            decrypted += decrypted_char
        else:
            decrypted += char
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
