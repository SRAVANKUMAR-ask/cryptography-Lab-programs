from math import gcd


def mod_inverse(a):
    for i in range(26):
        if (a * i) % 26 == 1:
            return i
    return None


def decrypt(ciphertext, a, b):
    plaintext = ""

    a_inv = mod_inverse(a)

    for char in ciphertext:
        if char.isalpha():
            c = ord(char.upper()) - ord('A')
            p = (a_inv * (c - b)) % 26
            plaintext += chr(p + ord('A'))
        else:
            plaintext += char

    return plaintext


ciphertext = input("Enter ciphertext: ")

# Most frequent ciphertext letter = B
# Assume it corresponds to plaintext E
# Second most frequent ciphertext letter = U
# Assume it corresponds to plaintext T

c1 = ord('B') - ord('A')   # 1
p1 = ord('E') - ord('A')   # 4

c2 = ord('U') - ord('A')   # 20
p2 = ord('T') - ord('A')   # 19

# Equations:
# 1 = 4a + b (mod 26)
# 20 = 19a + b (mod 26)

# Subtracting:
# 19 = 15a (mod 26)

a = None

for value in range(26):
    if (15 * value) % 26 == 19:
        if gcd(value, 26) == 1:
            a = value
            break

if a is not None:
    b = (c1 - a * p1) % 26

    print("Found a =", a)
    print("Found b =", b)

    plaintext = decrypt(ciphertext, a, b)

    print("Decrypted plaintext:", plaintext)
else:
    print("No valid affine cipher key found.")