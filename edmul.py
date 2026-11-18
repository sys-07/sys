
def extended_gcd(a, b):
    if b == 0:
        return a, 1, 0

    gcd, x1, y1 = extended_gcd(b, a % b)

    x = y1
    y = x1 - (a // b) * y1

    return gcd, x, y


def mod_inverse(key, m=26):
    gcd, x, _ = extended_gcd(key, m)

    if gcd != 1:
        return None

    return x % m


def multiplicative_encrypt(text, key):
    result = []

    for ch in text:
        if ch.isupper():
            result.append(chr(((ord(ch) - ord('A')) * key) % 26 + ord('A')))
        elif ch.islower():
            result.append(chr(((ord(ch) - ord('a')) * key) % 26 + ord('a')))
        else:
            result.append(ch)

    return ''.join(result)


def multiplicative_decrypt(text, key):
    key_inv = mod_inverse(key, 26)

    if key_inv is None:
        print("Error: Key is not invertible modulo 26.")
        print("Choose a key coprime with 26.")
        return None

    result = []

    for ch in text:
        if ch.isupper():
            result.append(chr(((ord(ch) - ord('A')) * key_inv) % 26 + ord('A')))
        elif ch.islower():
            result.append(chr(((ord(ch) - ord('a')) * key_inv) % 26 + ord('a')))
        else:
            result.append(ch)

    return ''.join(result)


def run_multiplicative_cipher():
    print("\nMultiplicative Cipher")

    plaintext = input("Enter plaintext: ")
    key = int(input("Enter key (must be coprime with 26): "))

    gcd, _, _ = extended_gcd(key, 26)

    if gcd != 1:
        print(f"Invalid key: gcd({key}, 26) = {gcd}. Choose another key.")
        return

    ciphertext = multiplicative_encrypt(plaintext, key)
    decrypted = multiplicative_decrypt(ciphertext, key)

    print(f"Plaintext        : {plaintext}")
    print(f"Encrypted (key={key}) : {ciphertext}")
    print(f"Decrypted back   : {decrypted}")


run_multiplicative_cipher()
