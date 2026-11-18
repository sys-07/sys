
import hashlib
import hmac
from google.colab import files

# Upload file
uploaded = files.upload()

file_name = list(uploaded.keys())[0]

# Enter shared secret key
secret_key = input("Enter secret key: ").encode()

# Read uploaded file
with open(file_name, "rb") as file:
    data = file.read()

# Calculate SHA-512 hash
sha512_hash = hashlib.sha512(data).hexdigest()

# Generate HMAC
hmac_hash = hmac.new(secret_key, data, hashlib.sha512).hexdigest()

print("\nSHA-512 Hash:")
print(sha512_hash)

print("\nHMAC:")
print(hmac_hash)

# Verify file integrity
new_hmac = hmac.new(secret_key, data, hashlib.sha512).hexdigest()

if hmac.compare_digest(hmac_hash, new_hmac):
    print("\nFile integrity verified. File is unchanged.")
else:
    print("\nFile integrity verification failed!")
