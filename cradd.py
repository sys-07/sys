
# Helper function
def clean_text(text):
    return ''.join(ch for ch in text if ch.isalpha()).upper()


# Additive Cipher Encryption
def additive_encrypt(text, key):
    result = ""

    for ch in text:
        if ch.isupper():
            result += chr((ord(ch) - ord('A') + key) % 26 + ord('A'))
        elif ch.islower():
            result += chr((ord(ch) - ord('a') + key) % 26 + ord('a'))
        else:
            result += ch

    return result


# Additive Cipher Decryption
def additive_decrypt(text, key):
    result = ""

    for ch in text:
        if ch.isupper():
            result += chr((ord(ch) - ord('A') - key) % 26 + ord('A'))
        elif ch.islower():
            result += chr((ord(ch) - ord('a') - key) % 26 + ord('a'))
        else:
            result += ch

    return result


# Cryptanalysis using Brute Force
def cryptanalysis_additive(ciphertext):
    ciphertext = clean_text(ciphertext)

    print("\nCiphertext:", ciphertext)
    print("\nTrying all 26 possible keys:\n")
    print(f"{'Key':<5}{'Decrypted Text'}")

    for key in range(26):
        decrypted = ""

        for ch in ciphertext:
            c_num = ord(ch) - ord('A')
            p_num = (c_num - key) % 26
            decrypted += chr(p_num + ord('A'))

        print(f"{key:<5}{decrypted}")

    print("\nThe row containing meaningful English text reveals the key.")


# Main Program
print("\nAdditive Cipher")

plaintext = input("Enter plaintext: ")
key = int(input("Enter key (0-25): "))

ciphertext = additive_encrypt(plaintext, key)
decrypted = additive_decrypt(ciphertext, key)

print("\nPlaintext       :", plaintext)
print("Encrypted text  :", ciphertext)
print("Decrypted text  :", decrypted)

# Perform Cryptanalysis
cryptanalysis_additive(ciphertext)
