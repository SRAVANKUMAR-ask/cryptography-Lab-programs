# Monoalphabetic Substitution Cipher

# Plain alphabet
plain = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

# Cipher alphabet (must contain all 26 unique letters)
cipher = "QWERTYUIOPASDFGHJKLZXCVBNM"

# Encryption Function
def encrypt(text):
    result = ""

    for ch in text.upper():
        if ch in plain:
            index = plain.index(ch)
            result += cipher[index]
        else:
            result += ch

    return result


# Decryption Function
def decrypt(text):
    result = ""

    for ch in text.upper():
        if ch in cipher:
            index = cipher.index(ch)
            result += plain[index]
        else:
            result += ch

    return result


# Main Program
message = input("Enter Plain Text: ")

encrypted = encrypt(message)
print("Encrypted Text :", encrypted)

decrypted = decrypt(encrypted)
print("Decrypted Text :", decrypted)