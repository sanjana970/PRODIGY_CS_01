import string

def caesar_encrypt(message, key):
    shift = key % 26
    cipher = str.maketrans(string.ascii_lowercase, string.ascii_lowercase[shift:] + string.ascii_lowercase[:shift])
    encrypted_message = message.lower().translate(cipher)
    return encrypted_message

def caesar_decrypt(encrypted_message, key):
    shift = 26 - (key % 26)
    cipher = str.maketrans(string.ascii_lowercase, string.ascii_lowercase[shift:] + string.ascii_lowercase[:shift])
    decrypted_message = encrypted_message.translate(cipher)
    return decrypted_message

def main():
    while True:
        choice = input("Enter 'e' to encrypt, 'd' to decrypt, or 'q' to quit: ").lower()
        if choice == 'q':
            print("Exiting program.")
            break
        elif choice == 'e':
            message = input("Enter the message to encrypt: ")
            key = int(input("Enter the shift value (a number between 1 and 25): "))
            encrypted_message = caesar_encrypt(message, key)
            print(f'Encrypted message: {encrypted_message}')
        elif choice == 'd':
            encrypted_message = input("Enter the message to decrypt: ")
            key = int(input("Enter the shift value used for encryption: "))
            decrypted_message = caesar_decrypt(encrypted_message, key)
            print(f'Decrypted message: {decrypted_message}')
        else:
            print("Invalid choice. Please enter 'e', 'd', or 'q'.")

if _name_ == "_main_":
    main()