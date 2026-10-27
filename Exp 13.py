"""
Chosen-Plaintext Attack on the Hill Cipher

The Hill cipher is a LINEAR transformation: C = K * P (mod 26).
This linearity is exactly what makes it vulnerable.

If an attacker can choose plaintext (not just observe known
plaintext-ciphertext pairs), they don't need to solve any system
of equations at all. Instead, they choose plaintext blocks equal
to the STANDARD BASIS VECTORS:

  e1 = (1, 0)   (letters: B A, since B=1, A=0)
  e2 = (0, 1)   (letters: A B)

Why this works:
  C = K * e1 = K * (1,0)^T = first COLUMN of K   (directly!)
  C = K * e2 = K * (0,1)^T = second COLUMN of K  (directly!)

So encrypting "BA" reveals column 1 of the key matrix, and
encrypting "AB" reveals column 2 -- no linear algebra needed,
just read the ciphertext numbers straight off as the key's columns.

For an n x n Hill cipher, the attacker needs only n chosen
plaintext blocks (each a unit vector) to fully recover the
entire n x n key matrix.

This program simulates the attack: it has a "victim" encryption
oracle using a secret key K, and an "attacker" that submits chosen
plaintexts and reconstructs K purely from the returned ciphertexts.
"""

MOD = 26

# The "secret" key matrix -- in a real attack the attacker does NOT
# know this. It's used here only to simulate the encryption oracle
# the attacker queries.
SECRET_K = [[9, 4], [5, 7]]


def encryption_oracle(p0, p1):
    """Simulates the victim's encryption oracle: encrypts one 2-letter
    block (as numbers 0-25) and returns the ciphertext numbers."""
    c0 = (SECRET_K[0][0] * p0 + SECRET_K[0][1] * p1) % MOD
    c1 = (SECRET_K[1][0] * p0 + SECRET_K[1][1] * p1) % MOD
    return c0, c1


def letter(n):
    return chr(n + ord('A'))


if __name__ == "__main__":
    print("=== Chosen-Plaintext Attack on 2x2 Hill Cipher ===\n")
    print("Attacker does NOT know the key. They query the encryption")
    print("oracle with two carefully CHOSEN plaintexts (unit vectors)")
    print("and read the key's columns directly off the results.\n")

    recovered_K = [[0, 0], [0, 0]]

    # Step 1: choose plaintext (1,0) -> letters "B A"
    print('Chosen plaintext 1: vector (1,0) = letters "B A"')
    c0, c1 = encryption_oracle(1, 0)
    print(f'  Oracle returns ciphertext: ({c0}, {c1}) = letters "{letter(c0)} {letter(c1)}"')
    print(f"  => This IS column 1 of the key matrix: [{c0}, {c1}]\n")
    recovered_K[0][0] = c0
    recovered_K[1][0] = c1

    # Step 2: choose plaintext (0,1) -> letters "A B"
    print('Chosen plaintext 2: vector (0,1) = letters "A B"')
    c0, c1 = encryption_oracle(0, 1)
    print(f'  Oracle returns ciphertext: ({c0}, {c1}) = letters "{letter(c0)} {letter(c1)}"')
    print(f"  => This IS column 2 of the key matrix: [{c0}, {c1}]\n")
    recovered_K[0][1] = c0
    recovered_K[1][1] = c1

    print("=== Fully Recovered Key Matrix ===")
    print(f"  | {recovered_K[0][0]}  {recovered_K[0][1]} |")
    print(f"  | {recovered_K[1][0]}  {recovered_K[1][1]} |\n")

    print("=== Verification against actual secret key ===")
    print(f"  | {SECRET_K[0][0]}  {SECRET_K[0][1]} |")
    print(f"  | {SECRET_K[1][0]}  {SECRET_K[1][1]} |\n")

    match = recovered_K == SECRET_K
    print(f"Match: {'YES - key fully recovered with just 2 chosen plaintexts!' if match else 'NO'}")

    print("\nGeneralization: for an n x n Hill cipher, an attacker needs")
    print("only n chosen plaintext blocks (the n unit vectors) to recover")
    print("the entire key matrix directly, column by column -- no system")
    print("of linear equations needs to be solved at all.")