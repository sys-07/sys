# Information Security Practical Viva Questions – Practicals 7, 8 and 9

**MCA – Information Security Practical Examination**

This revision sheet covers only the important viva questions for the following practicals:

- **Practical 7:** File encryption and decryption using symmetric and asymmetric encryption.
- **Practical 8:** SHA-512 hash and HMAC for file integrity verification using a shared secret key.
- **Practical 9:** File integrity verification using multiple hashing algorithms.

Answers are kept short for quick practical-exam revision.

---

# Category 1: File Encryption and Decryption Using Symmetric and Asymmetric Encryption

## Important Concepts

**Q1. What is encryption?**

Encryption converts readable data (plaintext) into unreadable data (ciphertext) using an algorithm and a key.

**Q2. What is decryption?**

Decryption converts ciphertext back into the original plaintext using the appropriate key.

**Q3. What is symmetric encryption?**

Symmetric encryption uses the same secret key for both encryption and decryption.

**Q4. What is asymmetric encryption?**

Asymmetric encryption uses a pair of keys: a public key and a private key.

**Q5. What is the main difference between symmetric and asymmetric encryption?**

| Symmetric Encryption | Asymmetric Encryption |
|---|---|
| Uses one shared secret key | Uses a public/private key pair |
| Generally faster | Generally slower |
| Secret key must be shared securely | Public key can be shared openly |
| Example: AES | Example: RSA |

**Q6. What is AES?**

AES (Advanced Encryption Standard) is a symmetric block cipher used to encrypt data.

**Q7. What is RSA?**

RSA is an asymmetric cryptographic algorithm that uses a public key and a private key.

**Q8. What is the role of the public key and private key in RSA encryption?**

The public key encrypts the data, and the corresponding private key decrypts it.

**Q9. What is a hybrid encryption system?**

A hybrid system combines symmetric and asymmetric encryption. A symmetric algorithm encrypts the file, while an asymmetric algorithm protects the symmetric key.

**Q10. Why is hybrid encryption used for file encryption?**

Symmetric encryption is fast for large files, while asymmetric encryption can securely protect the symmetric key.

## Python and Code-Based Questions

**Q11. What is the `cryptography` library?**

It is a Python library that provides cryptographic functions such as encryption, decryption, hashing, and key generation.

**Q12. What is Fernet?**

Fernet is a high-level authenticated symmetric encryption method provided by Python's `cryptography` library. It uses AES internally.

**Q13. What does `Fernet.generate_key()` do?**

It generates a new secret key for Fernet encryption and decryption.

**Q14. What do `encrypt()` and `decrypt()` do?**

- `encrypt()` encrypts the input data.
- `decrypt()` decrypts the encrypted data using the correct key.

**Q15. What does `rsa.generate_private_key()` do?**

It generates an RSA private key. The corresponding public key can be obtained from it.

**Q16. What is OAEP padding in RSA?**

OAEP (Optimal Asymmetric Encryption Padding) is a secure padding scheme used with RSA encryption.

**Q17. Why do we open a file using `"rb"`?**

`rb` means read binary. It reads the file as bytes, which is suitable for encryption.

**Q18. Why can't we directly encrypt a large file using RSA?**

RSA can encrypt only small amounts of data relative to its key size and padding. Therefore, a symmetric algorithm such as AES is used to encrypt the file, and RSA encrypts the AES key.

**Q19. What happens if we use the wrong key for decryption?**

Decryption fails or produces an authentication/decryption error, depending on the algorithm and method used.

**Q20. Is encryption the same as hashing?**

No. Encryption is reversible using the correct key, while cryptographic hashing is designed to be a one-way operation.

---

# Category 2: SHA-512 Hash and HMAC Using a Shared Secret Key

## Important Concepts

**Q1. What is a hash function?**

A hash function converts input data of any length into a fixed-length hash value.

**Q2. What is SHA-512?**

SHA-512 is a cryptographic hash algorithm from the SHA-2 family that produces a 512-bit (64-byte) hash.

**Q3. What is HMAC?**

HMAC stands for Hash-based Message Authentication Code. It combines a cryptographic hash function with a secret key to provide message integrity and authentication.

**Q4. What is the difference between SHA-512 and HMAC-SHA-512?**

| SHA-512 | HMAC-SHA-512 |
|---|---|
| Does not require a secret key | Requires a shared secret key |
| Produces a hash digest | Produces a keyed authentication code |
| Can detect changes if the expected hash is trusted | Verifies integrity and authenticity for parties sharing the secret key |

**Q5. Why is a shared secret key required in HMAC?**

The sender and receiver use the same secret key to generate and verify the HMAC. Someone without the key should not be able to generate a valid HMAC.

**Q6. What is the output size of SHA-512?**

512 bits, or 64 bytes. Its hexadecimal representation contains 128 characters.

**Q7. Can the original file be recovered from its SHA-512 hash?**

No. Cryptographic hashing is designed to be one-way.

**Q8. What happens if even one byte of the file changes?**

The resulting hash or HMAC will normally be very different.

**Q9. What is the difference between integrity and authenticity?**

- Integrity means data has not been changed unexpectedly.
- Authenticity means the data or message can be verified as coming from someone who possesses the correct secret key or credential.

## Python and Code-Based Questions

**Q10. What is the purpose of `hashlib`?**

It is a Python module that provides hash algorithms such as SHA-256 and SHA-512.

**Q11. What is the purpose of the `hmac` module?**

It provides functions to generate and verify Hash-based Message Authentication Codes.

**Q12. What does `hashlib.sha512(data).hexdigest()` return?**

It returns the SHA-512 digest as a hexadecimal string.

**Q13. Explain this code:**

```python
hmac.new(secret_key, data, hashlib.sha512).hexdigest()
```

It creates an HMAC using the shared secret key, file data, and SHA-512, then returns the result in hexadecimal form.

**Q14. Why do we use `.encode()` on the secret key?**

Cryptographic functions operate on bytes. `.encode()` converts a string into bytes.

**Q15. Why do we open a file using `"rb"`?**

To read the file as bytes without changing its contents.

**Q16. Why should the expected HMAC be stored or received securely?**

The verifier needs a trusted, previously generated HMAC to compare with the newly calculated HMAC. If an attacker can replace both the file and the stored HMAC, verification can be defeated.

**Q17. What is `hmac.compare_digest()` used for?**

It compares two digest values in a way designed to reduce timing-based comparison attacks.

**Q18. What happens if the wrong secret key is used?**

The newly calculated HMAC will not match the expected HMAC, so verification fails.

**Q19. Is HMAC encryption?**

No. HMAC does not encrypt or hide the data. It is used for integrity verification and message authentication.

**Q20. Can SHA-512 alone prove who created a file?**

No. SHA-512 alone does not authenticate the creator. HMAC can provide authentication between parties that share the secret key.

---

# Category 3: File Integrity Verification Using Multiple Hashing Algorithms

## Important Concepts

**Q1. What is file integrity verification?**

It checks whether a file has changed by comparing its current hash value with a previously stored trusted hash value.

**Q2. Which hashing algorithms are used in this practical?**

- MD5
- SHA-1
- SHA-256
- SHA-512

**Q3. What is MD5?**

MD5 is a hash algorithm that produces a 128-bit hash value. It is considered cryptographically broken and should not be used for security-sensitive integrity protection.

**Q4. What is SHA-1?**

SHA-1 is a hash algorithm that produces a 160-bit hash value. It is also considered insecure against collision attacks.

**Q5. What is SHA-256?**

SHA-256 is a member of the SHA-2 family that produces a 256-bit hash value.

**Q6. What is the output size of these algorithms?**

| Algorithm | Digest size | Hexadecimal characters |
|---|---:|---:|
| MD5 | 128 bits | 32 |
| SHA-1 | 160 bits | 40 |
| SHA-256 | 256 bits | 64 |
| SHA-512 | 512 bits | 128 |

**Q7. What is a hash collision?**

A collision occurs when two different inputs produce the same hash value.

**Q8. What does `Integrity Verified` mean?**

It means the newly calculated hash values match the previously stored trusted hash values for the algorithms being checked.

**Q9. What does `Integrity Compromised` mean?**

It means at least one newly calculated hash value does not match its corresponding stored hash value.

**Q10. Why do we calculate and store the original hash values?**

They serve as reference values for checking whether the file has changed later.

**Q11. Why do we upload the file again for verification?**

To calculate fresh hash values from the file being checked and compare them with the original reference values.

**Q12. What happens if the file is modified?**

Its hash values will normally change, resulting in a mismatch.

**Q13. Does hashing require a secret key?**

Ordinary hashing algorithms such as MD5, SHA-1, SHA-256, and SHA-512 do not require a secret key.

**Q14. Which algorithms should be preferred for modern integrity checking?**

SHA-256 or SHA-512 are preferred over MD5 and SHA-1 for security-sensitive applications.

## Python and Code-Based Questions

**Q15. What is the purpose of `hashlib.new(algorithm)`?**

It creates a hash object for the specified algorithm.

**Q16. What does `hasher.update(data)` do?**

It adds the file data to the hash calculation.

**Q17. What does `hasher.hexdigest()` return?**

It returns the calculated hash digest as a hexadecimal string.

**Q18. Why do we use a dictionary to store original hashes?**

A dictionary stores each algorithm name with its corresponding original hash value.

**Q19. What is the purpose of `all_match = True`?**

It assumes initially that all hashes match. If any mismatch occurs, the variable is changed to `False`.

**Q20. Why do we use a loop over all algorithms?**

To calculate and compare the file hash separately for each selected algorithm.

**Q21. What is the difference between `MATCH` and `MISMATCH`?**

- `MATCH`: The newly calculated hash equals the stored original hash.
- `MISMATCH`: The two hash values are different.

**Q22. Can two different files have the same hash?**

Yes, this is theoretically possible due to hash collisions. Strong modern hash algorithms make finding such collisions computationally infeasible with current practical methods.

---

# Category 4: Most Important Differences for Viva

## 1. Symmetric vs Asymmetric Encryption

| Symmetric | Asymmetric |
|---|---|
| One shared secret key | Public and private key pair |
| Faster | Generally slower |
| Example: AES | Example: RSA |
| Same key encrypts and decrypts | Public key encrypts, private key decrypts in the confidentiality use case |

## 2. SHA-512 vs HMAC-SHA-512

| SHA-512 | HMAC-SHA-512 |
|---|---|
| No secret key | Uses a shared secret key |
| Hashing | Keyed message authentication |
| 512-bit output | 512-bit output |
| Integrity check when reference hash is trusted | Integrity and authenticity verification |

## 3. Hashing vs Encryption

| Hashing | Encryption |
|---|---|
| One-way operation | Reversible with the correct key |
| No decryption | Supports decryption |
| Used for integrity checking | Used for confidentiality |
| Example: SHA-512 | Example: AES |

## 4. Important Hash Output Sizes

| Algorithm | Bits | Hex characters |
|---|---:|---:|
| MD5 | 128 | 32 |
| SHA-1 | 160 | 40 |
| SHA-256 | 256 | 64 |
| SHA-512 | 512 | 128 |

---

# Category 5: Top 15 Questions to Prepare First

If you have limited time, prepare these questions first:

1. What is the difference between symmetric and asymmetric encryption?
2. What is AES?
3. What is RSA?
4. What is hybrid encryption, and why is it used?
5. Why can't RSA directly encrypt a large file?
6. What is Fernet?
7. What is SHA-512, and what is its output size?
8. What is HMAC?
9. What is the difference between SHA-512 and HMAC-SHA-512?
10. Why does HMAC require a shared secret key?
11. What is file integrity verification?
12. What are MD5, SHA-1, SHA-256 and SHA-512?
13. What is a hash collision?
14. What does `Integrity Verified` or `Integrity Compromised` indicate?
15. What is the difference between hashing, encryption and HMAC?

---

## Final Revision Tips

1. Understand the difference between symmetric and asymmetric encryption.
2. Remember that AES encrypts the file and RSA can protect the AES key in hybrid encryption.
3. Remember that SHA-512 produces a 512-bit digest.
4. Understand why HMAC requires a shared secret key.
5. Memorize the output sizes of MD5, SHA-1, SHA-256 and SHA-512.
6. Be able to explain how your program compares original and newly calculated hash values.

**Practical viva tip:** Be prepared to explain why you used each library (`cryptography`, `hashlib`, and `hmac`), what each important function does, and how the program verifies that the decrypted or uploaded file matches the original.
