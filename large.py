
!pip install cryptography

from cryptography.fernet import Fernet
from cryptography.hazmat.primitives.asymmetric import rsa, padding
from cryptography.hazmat.primitives import hashes
from google.colab import files

# Upload file
print("Upload a file:")
uploaded = files.upload()

file_name = list(uploaded.keys())[0]

with open(file_name, "rb") as file:
    data = file.read()


# =====================================
# 1. SYMMETRIC ENCRYPTION USING AES
# =====================================

print("\n--- Symmetric Encryption (AES) ---")

# Generate secret key
secret_key = Fernet.generate_key()

# Create cipher
cipher = Fernet(secret_key)

# Encrypt file data
encrypted_data = cipher.encrypt(data)

with open("symmetric_encrypted.bin", "wb") as file:
    file.write(encrypted_data)

# Decrypt file data
decrypted_data = cipher.decrypt(encrypted_data)

with open("symmetric_decrypted_" + file_name, "wb") as file:
    file.write(decrypted_data)

print("File encrypted successfully!")
print("File decrypted successfully!")


# =====================================
# 2. ASYMMETRIC ENCRYPTION USING RSA
# =====================================

print("\n--- Asymmetric Encryption (RSA) ---")

# Generate private and public keys
private_key = rsa.generate_private_key(
    public_exponent=65537,
    key_size=2048
)

public_key = private_key.public_key()

# Generate AES key for file encryption
aes_key = Fernet.generate_key()
aes_cipher = Fernet(aes_key)

# Encrypt file using AES
encrypted_file = aes_cipher.encrypt(data)

# Encrypt AES key using RSA public key
encrypted_key = public_key.encrypt(
    aes_key,
    padding.OAEP(
        mgf=padding.MGF1(algorithm=hashes.SHA256()),
        algorithm=hashes.SHA256(),
        label=None
    )
)

# Save encrypted file and encrypted key
with open("asymmetric_encrypted.bin", "wb") as file:
    file.write(encrypted_file)

with open("encrypted_aes_key.bin", "wb") as file:
    file.write(encrypted_key)

# Decrypt AES key using RSA private key
decrypted_key = private_key.decrypt(
    encrypted_key,
    padding.OAEP(
        mgf=padding.MGF1(algorithm=hashes.SHA256()),
        algorithm=hashes.SHA256(),
        label=None
    )
)

# Decrypt file using recovered AES key
decrypted_data = Fernet(decrypted_key).decrypt(encrypted_file)

with open("asymmetric_decrypted_" + file_name, "wb") as file:
    file.write(decrypted_data)

print("File encrypted successfully!")
print("File decrypted successfully!")


# =====================================
# 3. VERIFY RESULTS
# =====================================

print("\n--- Verification ---")

if data == decrypted_data:
    print("RSA: Original and decrypted files match.")

if data == Fernet(secret_key).decrypt(encrypted_data):
    print("AES: Original and decrypted files match.")

print("\nEncryption and Decryption Completed!")
