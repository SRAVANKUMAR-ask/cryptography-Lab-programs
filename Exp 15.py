# English letter frequencies (%) A-Z
FREQ = [8.167,1.492,2.782,4.253,12.702,2.228,2.015,6.094,6.966,0.153,0.772,4.025,2.406,
        6.749,7.507,1.929,0.095,5.987,6.327,9.056,2.758,0.978,2.360,0.150,1.974,0.074]

def decrypt(text, k):
    return "".join(chr((ord(c) - 65 - k) % 26 + 65) for c in text)

def score(text):
    """Chi-squared distance from English (lower = more likely English)."""
    n = len(text)
    s = 0.0
    for i in range(26):
        observed = text.count(chr(65 + i))
        expected = FREQ[i] * n / 100
        s += (observed - expected) ** 2 / expected
    return s

def attack(cipher, top):
    cipher = "".join(c for c in cipher.upper() if c.isalpha())
    results = sorted((score(decrypt(cipher, k)), k, decrypt(cipher, k)) for k in range(26))
    for rank, (sc, k, plain) in enumerate(results[:top], 1):
        print(f"{rank:2d}. key={k:2d}  score={sc:8.2f}  {plain}")

cipher = input("Enter ciphertext: ")
top = int(input("How many top possible plaintexts? "))
attack(cipher, top)