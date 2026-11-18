
# GCD using Recursive Euclidean Algorithm
def gcd(a, b):
    if b == 0:
        return a
    return gcd(b, a % b)


# Extended Euclidean Algorithm
def extended_gcd(a, b):
    if b == 0:
        return a, 1, 0

    gcd, x1, y1 = extended_gcd(b, a % b)

    x = y1
    y = x1 - (a // b) * y1

    return gcd, x, y


# Modular Inverse
def mod_inverse(key, m=26):
    gcd, x, _ = extended_gcd(key, m)

    if gcd != 1:
        return None

    return x % m


# Clean Text
def clean_text(text):
    return ''.join(ch for ch in text if ch.isalpha()).upper()


# Multiplicative Encryption
def multiplicative_encrypt(text, key):
    result = ""

    for ch in text:
        if ch.isupper():
            result += chr(((ord(ch) - ord('A')) * key) % 26 + ord('A'))
        elif ch.islower():
            result += chr(((ord(ch) - ord('a')) * key) % 26 + ord('a'))
        else:
            result += ch

    return result


# Multiplicative Decryption
def multiplicative_decrypt(text, key):
    key_inv = mod_inverse(key, 26)

    if key_inv is None:
        print("Invalid key! Choose a key coprime with 26.")
        return None

    result = ""

    for ch in text:
        if ch.isupper():
            result += chr(((ord(ch) - ord('A')) * key_inv) % 26 + ord('A'))
        elif ch.islower():
            result += chr(((ord(ch) - ord('a')) * key_inv) % 26 + ord('a'))
        else:
            result += ch

    return result


# Cryptanalysis using Brute Force
def cryptanalysis_multiplicative(ciphertext):
    ciphertext = clean_text(ciphertext)

    print("\nCiphertext:", ciphertext)

    valid_keys = [k for k in range(1, 26) if gcd(k, 26) == 1]

    print("\nValid keys:", valid_keys)
    print("Total valid keys:", len(valid_keys))

    print("\nTrying all valid keys:\n")
    print(f"{'Key':<6}{'Inverse':<10}{'Decrypted Text'}")

    for key in valid_keys:
        inv = mod_inverse(key, 26)
        decrypted = ""

        for ch in ciphertext:
            c_num = ord(ch) - ord('A')
            p_num = (c_num * inv) % 26
            decrypted += chr(p_num + ord('A'))

        print(f"{key:<6}{inv:<10}{decrypted}")

    print("\nThe row containing meaningful English text reveals the key.")


# Main Program
print("\nMultiplicative Cipher")

plaintext = input("Enter plaintext: ")
key = int(input("Enter key (coprime with 26): "))

if gcd(key, 26) != 1:
    print("Invalid key! Choose a key coprime with 26.")

else:
    ciphertext = multiplicative_encrypt(plaintext, key)
    decrypted = multiplicative_decrypt(ciphertext, key)

    print("\nPlaintext       :", plaintext)
    print("Encrypted text  :", ciphertext)
    print("Decrypted text  :", decrypted)

    # Perform Cryptanalysis
    cryptanalysis_multiplicative(ciphertext)
