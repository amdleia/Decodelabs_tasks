def caesar_cipher(text, shift, mode='encrypt'):
    """
    Encrypts or decrypts text using the Caesar Cipher algorithm.
    :param text: The input string to process
    :param shift: The key/number of positions to shift
    :param mode: 'encrypt' or 'decrypt'
    :return: Processed string
    """
    if mode == 'decrypt':
        shift = -shift  # Reverse the direction for decryption

    result = []
    
    for char in text:
        if char.isupper():
            # Shift within 'A'-'Z' (ASCII 65-90)
            shifted = chr((ord(char) - 65 + shift) % 26 + 65)
            result.append(shifted)
        elif char.islower():
            # Shift within 'a'-'z' (ASCII 97-122)
            shifted = chr((ord(char) - 97 + shift) % 26 + 97)
            result.append(shifted)
        elif char.isdigit():
            # Shift numbers within '0'-'9' (ASCII 48-57)
            shifted = chr((ord(char) - 48 + shift) % 10 + 48)
            result.append(shifted)
        else:
            # Leave spaces and special characters intact
            result.append(char)
            
    return "".join(result)

def main():
    print("=" * 45)
    print(" CYBER-CAESAR (Caesar Cipher Encryption & Decryption)")
    print("=" * 45)
    
    message = input("Enter message to process: ")
    while True:
        try:
            shift_key = int(input("Press enter key (number, e.g., 3): "))
            break
        except ValueError:
            print("Invalid input! Please enter a number.")

    # 1. Encrypt text
    encrypted_msg = caesar_cipher(message, shift_key, mode='encrypt')
    
    # 2. Decrypt text back to plaintext
    decrypted_msg = caesar_cipher(encrypted_msg, shift_key, mode='decrypt')

    print("\n" + "-" * 45)
    print(f"Original Text  : {message}")
    print(f"Encrypted Text : {encrypted_msg}")
    print(f"Decrypted Text : {decrypted_msg}")
    print("-" * 45)

if __name__ == "__main__":
    main()