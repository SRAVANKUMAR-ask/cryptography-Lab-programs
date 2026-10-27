"""
Hill Cipher Encryption and Decryption (2x2 key matrix)

Key matrix:
  | 9  4 |
  | 5  7 |

Encryption: C = K * P (mod 26), where P is a column vector of 2 plaintext
            letter-numbers (A=0 ... Z=25), taken two letters at a time.
Decryption: P = K_inverse * C (mod 26)

To find K_inverse mod 26:
  det(K) = (9*7 - 4*5) = 63 - 20 = 43 -> 43 mod 26 = 17
  det_inverse: find x such that (17 * x) mod 26 = 1  ->  x = 23
  adjugate(K) = |  7  -4 |
                | -5   9 |
  K_inverse = det_inverse * adjugate(K) mod 26
            = 23 * |  7  -4 |  mod 26
                   | -5   9 |
            = |  5  12 |
              | 15  25 |
"""

MOD = 26

K = [[9, 4], [5, 7]]
K_INV = [[5, 12], [15, 25]]


def clean_text(message):
    """Uppercase letters only, pad with X if odd length."""
    cleaned = "".join(ch for ch in message.upper() if ch.isalpha())
    if len(cleaned) % 2 != 0:
        cleaned += "X"
    return cleaned


def matrix_vector_mult(M, v0, v1):
    """Multiply a 2x2 matrix by a 2x1 vector, mod 26."""
    r0 = (M[0][0] * v0 + M[0][1] * v1) % MOD
    r1 = (M[1][0] * v0 + M[1][1] * v1) % MOD
    return r0, r1


def hill_process(text, M, label):
    """Apply the Hill cipher transform block-by-block, printing each step."""
    output = []
    for i in range(0, len(text), 2):
        p0 = ord(text[i]) - ord('A')
        p1 = ord(text[i + 1]) - ord('A')

        c0, c1 = matrix_vector_mult(M, p0, p1)

        out_a = chr(c0 + ord('A'))
        out_b = chr(c1 + ord('A'))
        output.append(out_a)
        output.append(out_b)

        print(f"  Block {i // 2 + 1:2d}: [{text[i]} {text[i+1]}] -> "
              f"P=[{p0:2d} {p1:2d}] -> C=[{c0:2d} {c1:2d}] -> [{out_a} {out_b}]")

    return "".join(output)


if __name__ == "__main__":
    message = "meet me at the usual place at ten rather than eight oclock"

    print(f"Key matrix K:\n  | {K[0][0]}  {K[0][1]} |\n  | {K[1][0]}  {K[1][1]} |\n")
    print(f"Inverse key matrix K_inv (mod 26):\n"
          f"  | {K_INV[0][0]:2d}  {K_INV[0][1]:2d} |\n"
          f"  | {K_INV[1][0]:2d}  {K_INV[1][1]:2d} |\n")

    clean = clean_text(message)
    print(f"Original message : {message}")
    print(f"Cleaned/padded   : {clean} (length {len(clean)})\n")

    print("=== ENCRYPTION (C = K * P mod 26) ===")
    ciphertext = hill_process(clean, K, "encrypt")
    print(f"\nCiphertext: {ciphertext}\n")

    print("=== DECRYPTION (P = K_inv * C mod 26) ===")
    decrypted = hill_process(ciphertext, K_INV, "decrypt")
    print(f"\nDecrypted (should match cleaned plaintext): {decrypted}")