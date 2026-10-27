def encrypt(plain, key):
    plain = plain.replace(" ", "").upper()
    return "".join(chr((ord(p) - 65 + k) % 26 + 65) for p, k in zip(plain, key))

def decrypt(cipher, key):
    return "".join(chr((ord(c) - 65 - k) % 26 + 65) for c, k in zip(cipher, key))

def find_key(cipher, plain):
    plain = plain.replace(" ", "").upper()
    return [(ord(c) - ord(p)) % 26 for c, p in zip(cipher, plain)]

# Part (a): encrypt
plain = input("Enter plaintext: ")
key = list(map(int, input("Enter key stream (space separated): ").split()))
cipher = encrypt(plain, key)
print("Ciphertext:", cipher)

# Part (b): find the key for a new plaintext
new_plain = input("\nEnter desired plaintext for the same ciphertext: ")
new_key = find_key(cipher, new_plain)
print("New key:", *new_key)
print("Decrypted with new key:", decrypt(cipher, new_key))