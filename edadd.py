
def additive_encrypt(text, key):
    result = []

    for ch in text:
        if ch.isupper():
            result.append(chr((ord(ch) - ord('A') + key) % 26 + ord('A')))
        elif ch.islower():
            result.append(chr((ord(ch) - ord('a') + key) % 26 + ord('a')))
        else:
            result.append(ch)  # Preserve spaces and punctuation

    return ''.join(result)


def additive_decrypt(text, key):
    result = []

    for ch in text:
        if ch.isupper():
            result.append(chr((ord(ch) - ord('A') - key) % 26 + ord('A')))
        elif ch.islower():
            result.append(chr((ord(ch) - ord('a') - key) % 26 + ord('a')))
        else:
            result.append(ch)

    return ''.join(result)


def run_additive_cipher():
    print("\nAdditive Cipher")

    plaintext = input("Enter plaintext: ")
    key = int(input("Enter key (0-25): "))

    ciphertext = additive_encrypt(plaintext, key)
    decrypted = additive_decrypt(ciphertext, key)

    print(f"Plaintext        : {plaintext}")
    print(f"Encrypted (key={key}) : {ciphertext}")
    print(f"Decrypted back   : {decrypted}")


run_additive_cipher()
