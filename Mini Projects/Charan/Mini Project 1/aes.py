from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad
from base64 import b64encode, b64decode

def encrypt(plain_text, key):
    cipher = AES.new(key, AES.MODE_CBC)
    padded_text = pad(plain_text.encode('utf-8'), AES.block_size)
    encrypted_text = cipher.encrypt(padded_text)
    return b64encode(cipher.iv + encrypted_text).decode('utf-8')

def decrypt(encrypted_text, key):
    raw = b64decode(encrypted_text)
    iv = raw[:AES.block_size]
    encrypted_text = raw[AES.block_size:]
    cipher = AES.new(key, AES.MODE_CBC, iv)
    decrypted_data = cipher.decrypt(encrypted_text)
    return unpad(decrypted_data, AES.block_size).decode('utf-8')

def main():
    action = input("Do you want to encrypt or decrypt? (e/d): ").lower()
    key_input = input("Enter a 16, 24, or 32-character key: ")

    if len(key_input) not in (16, 24, 32):
        print("Invalid key length. It must be 16, 24, or 32 characters long.")
        return

    key = key_input.encode()

    if action == 'e':
        plain_text = input("Enter the plaintext to encrypt: ")
        encrypted_text = encrypt(plain_text, key)
        print('Encrypted:', encrypted_text)
    elif action == 'd':
        encrypted_text = input("Enter the encrypted text to decrypt: ")
        try:
            decrypted_text = decrypt(encrypted_text, key)
            print('Decrypted:', decrypted_text)
        except ValueError as e:
            print("Decryption error:", e)
    else:
        print("Invalid option. Please enter 'e' for encryption or 'd' for decryption.")

if __name__ == "__main__":
    main()
