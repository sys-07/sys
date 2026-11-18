
import hashlib
from google.colab import files

# Upload original file
print("Upload Original File")
uploaded = files.upload()

file_name = list(uploaded.keys())[0]
print("File uploaded successfully:", file_name)


# Calculate hash values
def calculate_hash(file_name, algorithm):
    hasher = hashlib.new(algorithm)

    with open(file_name, "rb") as file:
        data = file.read()
        hasher.update(data)

    return hasher.hexdigest()


# Supported hashing algorithms
algorithms = ["md5", "sha1", "sha256", "sha512"]

# Store original hash values
original_hashes = {}

print("\nOriginal Hash Values:\n")

for algorithm in algorithms:
    original_hashes[algorithm] = calculate_hash(
        file_name, algorithm
    )

    print(algorithm.upper(), ":", original_hashes[algorithm])


# Upload file again for verification
print("\nUpload File for Verification")

uploaded = files.upload()

verify_file = list(uploaded.keys())[0]

print("File selected for verification:", verify_file)


# Verify file integrity
all_match = True

print("\nFile Integrity Verification Results\n")

for algorithm in algorithms:

    current_hash = calculate_hash(verify_file, algorithm)

    if current_hash == original_hashes[algorithm]:
        print(algorithm.upper(), ": MATCH")
    else:
        print(algorithm.upper(), ": MISMATCH")
        all_match = False


# Display final result
if all_match:
    print("\nIntegrity Verified")
else:
    print("\nIntegrity Compromised")
