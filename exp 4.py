def encrypt(plaintext, key):
    ciphertext = ""
    key = key.upper()
    key_index = 0

    for char in plaintext:
        if char.isalpha():
            p = ord(char.upper()) - ord('A')
            k = ord(key[key_index % len(key)]) - ord('A')

            c = (p + k) % 26
            ciphertext += chr(c + ord('A'))

            key_index += 1
        else:
            ciphertext += char

    return ciphertext


plaintext = input("Enter plaintext: ")
key = input("Enter key: ")

ciphertext = encrypt(plaintext, key)

print("Encrypted text:", ciphertext)
def decrypt(ciphertext, key):
    plaintext = ""
    key = key.upper()
    key_index = 0

    for char in ciphertext:
        if char.isalpha():
            c = ord(char.upper()) - ord('A')
            k = ord(key[key_index % len(key)]) - ord('A')

            p = (c - k) % 26
            plaintext += chr(p + ord('A'))

            key_index += 1
        else:
            plaintext += char

    return plaintext


ciphertext = input("Enter ciphertext: ")
key = input("Enter key: ")

plaintext = decrypt(ciphertext, key)

print("Decrypted text:", plaintext)