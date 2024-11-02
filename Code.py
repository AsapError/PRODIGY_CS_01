import os

# ANSI escape codes for colored output
class Colors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'

def clear_console():
    # Clear console for better visual experience
    os.system('cls' if os.name == 'nt' else 'clear')

def caesar_cipher(text, shift):
    result = ""
    for char in text:
        if char.isalpha():
            shift_base = ord('A') if char.isupper() else ord('a')
            result += chr((ord(char) - shift_base + shift) % 26 + shift_base)
        else:
            result += char
    return result

def main():
    clear_console()
    print(Colors.OKGREEN + "Welcome to the Caesar Cipher Program!" + Colors.ENDC)
    
    while True:
        print(Colors.OKGREEN + "Would you like to:" + Colors.ENDC)
        print("1. Encrypt a message")
        print("2. Decrypt a message")
        print("3. Quit")
        action = input("Enter your choice (1/2/3): ")

        if action == '3':
            if input(Colors.WARNING + "Are you sure you want to quit? (y/n): " + Colors.ENDC).lower() == 'y':
                print(Colors.OKBLUE + "Goodbye! Have a great day!" + Colors.ENDC)
                break

        if action not in ['1', '2']:
            print(Colors.FAIL + "Invalid option. Please choose 1, 2, or 3." + Colors.ENDC)
            continue
        
        message = input(Colors.OKBLUE + "Enter your message: " + Colors.ENDC)
        
        while True:
            try:
                shift = int(input(Colors.OKBLUE + "Enter shift value (positive for encryption, negative for decryption): " + Colors.ENDC))
                break
            except ValueError:
                print(Colors.FAIL + "Invalid shift value. Please enter an integer." + Colors.ENDC)

        if action == '1':
            encrypted_message = caesar_cipher(message, shift)
            print(Colors.OKGREEN + f"Encrypted Message: {encrypted_message}" + Colors.ENDC)
        elif action == '2':
            decrypted_message = caesar_cipher(message, -shift)
            print(Colors.OKGREEN + f"Decrypted Message: {decrypted_message}" + Colors.ENDC)

if __name__ == "__main__":
    main()
