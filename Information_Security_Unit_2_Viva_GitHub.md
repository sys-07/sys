# Information Security – Unit II Viva Questions with Answers

**MCA – Information Security Practical Examination**

**Unit II: Cryptography**

This revision sheet follows the Unit II syllabus:

- Substitution and transposition ciphers
- Symmetric-key algorithms: DES, AES and IDEA
- Block cipher operations
- Stream cipher: RC4
- Public-key encryption: Knapsack, RSA, ElGamal and Elliptic Curve Cryptography (ECC)

Answers are concise and focused on important practical-viva concepts.

---

# Category 1: Basic Cryptography Concepts

**Q1. What is cryptography?**

Cryptography is the science of protecting information by transforming it so that only authorized parties can understand or verify it.

**Q2. What are plaintext and ciphertext?**

- **Plaintext:** The original readable message.
- **Ciphertext:** The transformed, encrypted message.

**Q3. What is encryption?**

Encryption converts plaintext into ciphertext using an encryption algorithm and a key.

**Q4. What is decryption?**

Decryption converts ciphertext back into plaintext using the appropriate decryption key.

**Q5. What is a cryptographic key?**

A key is a value used by a cryptographic algorithm to control encryption, decryption or another cryptographic operation.

**Q6. What are the two broad types of encryption?**

- Symmetric-key encryption
- Asymmetric-key encryption (public-key encryption)

**Q7. What is the difference between symmetric and asymmetric encryption?**

| Symmetric-key encryption | Asymmetric-key encryption |
|---|---|
| Uses the same shared secret key for encryption and decryption | Uses a related public-key/private-key pair |
| Generally faster | Generally slower for bulk data |
| Secret key must be shared securely | Public key can be distributed openly |
| Examples: AES, DES, IDEA | Examples: RSA, ElGamal |

**Q8. What is a substitution cipher?**

A substitution cipher replaces each plaintext symbol or group of symbols with another symbol or group according to a rule and key.

**Q9. What is a transposition cipher?**

A transposition cipher rearranges the positions of plaintext characters without replacing the characters themselves.

**Q10. What is the difference between substitution and transposition?**

| Substitution | Transposition |
|---|---|
| Replaces symbols | Rearranges symbol positions |
| Character identities change | Character identities remain the same |
| Example: Additive/Caesar cipher | Example: Columnar transposition cipher |

---

# Category 2: Symmetric-Key Algorithms – DES, AES and IDEA

## Data Encryption Standard (DES)

**Q1. What is DES?**

DES (Data Encryption Standard) is a symmetric-key block cipher that encrypts data in 64-bit blocks.

**Q2. What is the effective key size of DES?**

DES has a 64-bit key representation, but 8 bits are used for parity. Its effective key length is 56 bits.

**Q3. How many rounds does DES use?**

DES uses 16 rounds of processing.

**Q4. What is the block size of DES?**

64 bits.

**Q5. What structure does DES use?**

DES uses a Feistel network.

**Q6. What is a Feistel network?**

A Feistel network divides a data block into two halves and processes them through repeated rounds. In each round, one half is combined with a function of the other half and a round key.

**Q7. Why is DES considered insecure today?**

Its 56-bit effective key is too short to resist modern brute-force attacks.

**Q8. What is Triple DES (3DES)?**

3DES applies the DES operation three times, commonly using an encrypt-decrypt-encrypt (EDE) sequence. It improves on DES but is now deprecated for most new applications because of its performance and security limitations.

## Advanced Encryption Standard (AES)

**Q9. What is AES?**

AES (Advanced Encryption Standard) is a symmetric-key block cipher standardized to replace DES.

**Q10. What is the block size of AES?**

AES always uses a 128-bit block size.

**Q11. What key sizes does AES support?**

- 128 bits
- 192 bits
- 256 bits

**Q12. How many rounds does AES use?**

| AES key size | Number of rounds |
|---|---:|
| 128 bits | 10 |
| 192 bits | 12 |
| 256 bits | 14 |

**Q13. What are the four main transformations in an AES encryption round?**

1. SubBytes
2. ShiftRows
3. MixColumns
4. AddRoundKey

The final round omits MixColumns.

**Q14. What is SubBytes in AES?**

SubBytes replaces each byte using a fixed substitution table called the S-box.

**Q15. What is ShiftRows in AES?**

ShiftRows cyclically shifts the rows of the AES state by different offsets.

**Q16. What is MixColumns in AES?**

MixColumns mixes the bytes in each column using arithmetic in the finite field GF(2^8).

**Q17. What is AddRoundKey in AES?**

AddRoundKey combines the state with a round key using bitwise XOR.

**Q18. Why is AES preferred over DES?**

AES supports longer keys, provides stronger security against known practical attacks, and is efficient in software and hardware.

## IDEA

**Q19. What is IDEA?**

IDEA (International Data Encryption Algorithm) is a symmetric-key block cipher.

**Q20. What are the block size and key size of IDEA?**

- Block size: 64 bits.
- Key size: 128 bits.

**Q21. How many rounds does IDEA use?**

IDEA uses 8 full rounds followed by an output transformation (often described as a half-round).

**Q22. Which operations are used in IDEA?**

IDEA combines:
- XOR
- Addition modulo 2^16
- Multiplication modulo 2^16 + 1

**Q23. How is IDEA different from AES?**

| IDEA | AES |
|---|---|
| 64-bit block size | 128-bit block size |
| 128-bit key | 128, 192 or 256-bit key |
| 8 rounds plus output transformation | 10, 12 or 14 rounds |
| Uses XOR, modular addition and modular multiplication | Uses byte substitution and finite-field transformations |

---

# Category 3: Block Cipher Operations and Modes of Operation

**Q1. What is a block cipher?**

A block cipher is a symmetric-key algorithm that encrypts data in fixed-size blocks using a secret key.

**Q2. What is a block cipher mode of operation?**

A mode of operation defines how a block cipher is applied to data longer than one block and how blocks are related during encryption and decryption.

**Q3. Name important block cipher modes.**

- ECB (Electronic Codebook)
- CBC (Cipher Block Chaining)
- CFB (Cipher Feedback)
- OFB (Output Feedback)
- CTR (Counter)
- GCM (Galois/Counter Mode)

**Q4. What is ECB mode?**

ECB encrypts each block independently using the same key. Identical plaintext blocks produce identical ciphertext blocks.

**Q5. What is the main weakness of ECB?**

It reveals patterns in data because identical plaintext blocks encrypt to identical ciphertext blocks. It is generally unsuitable for encrypting structured multi-block data.

**Q6. What is CBC mode?**

CBC combines each plaintext block with the previous ciphertext block using XOR before encryption. The first block uses an initialization vector (IV).

**Q7. What is an IV?**

An Initialization Vector is a value used by certain encryption modes to introduce variation into encryption. Its required properties depend on the mode.

**Q8. What is the role of XOR in CBC mode?**

XOR combines the current plaintext block with the previous ciphertext block (or the IV for the first block) before encryption.

**Q9. What is CFB mode?**

CFB (Cipher Feedback) uses the block cipher's encryption operation to generate a feedback-based stream that is combined with plaintext using XOR.

**Q10. What is OFB mode?**

OFB (Output Feedback) repeatedly encrypts an internal state to generate a keystream, which is XORed with plaintext.

**Q11. What is CTR mode?**

CTR (Counter) encrypts successive counter values to generate a keystream, which is XORed with plaintext or ciphertext.

**Q12. Which modes can turn a block cipher into a stream-like operation?**

CFB, OFB and CTR can process data in a stream-like manner.

**Q13. What is padding?**

Padding adds extra data to a message so its length meets a block-size requirement. Some modes, such as CBC, require padding when the message length is not a whole number of blocks. CTR, CFB and OFB do not require block padding.

**Q14. What is authenticated encryption?**

Authenticated encryption provides confidentiality and also checks integrity and authenticity of the encrypted data.

**Q15. Is AES-GCM an authenticated encryption mode?**

Yes. AES-GCM provides authenticated encryption with associated data (AEAD).

---

# Category 4: Stream Cipher – RC4

**Q1. What is a stream cipher?**

A stream cipher generates a keystream that is combined with plaintext, commonly using XOR, to produce ciphertext.

**Q2. What is RC4?**

RC4 is a symmetric stream cipher designed by Ron Rivest. It generates a pseudorandom keystream that is XORed with plaintext.

**Q3. Is RC4 a block cipher or a stream cipher?**

RC4 is a stream cipher.

**Q4. What are the two main stages of RC4?**

1. Key Scheduling Algorithm (KSA)
2. Pseudo-Random Generation Algorithm (PRGA)

**Q5. What is the purpose of KSA?**

KSA initializes and permutes the internal state array using the secret key.

**Q6. What is the purpose of PRGA?**

PRGA updates the internal state and generates the keystream bytes.

**Q7. How does RC4 encryption work?**

RC4 XORs each plaintext byte with the corresponding keystream byte.

**Q8. How does RC4 decryption work?**

It XORs the ciphertext with the same keystream. XOR is reversible, so the original plaintext is recovered.

**Q9. Why is RC4 considered insecure?**

RC4 has statistical biases in its keystream and weaknesses in its design and use. It is deprecated and should not be used in modern systems.

**Q10. Where was RC4 historically used?**

RC4 was historically used in protocols and systems such as WEP and older versions of TLS. It is no longer considered safe for these uses.

---

# Category 5: Public-Key Encryption

## Basic Concepts

**Q1. What is public-key encryption?**

Public-key encryption uses a public key to encrypt data and the corresponding private key to decrypt it.

**Q2. What is a public key?**

A public key is the key that can be shared openly and is used for operations such as encryption or signature verification, depending on the cryptographic scheme.

**Q3. What is a private key?**

A private key is kept secret by its owner and is used for operations such as decryption or digital signing, depending on the scheme.

**Q4. What is the main advantage of public-key cryptography?**

It reduces the need to share a secret encryption key in advance. Public keys can be distributed openly, provided their authenticity is verified.

**Q5. What is the main disadvantage of public-key cryptography?**

It is generally slower and more computationally expensive than symmetric encryption for large amounts of data.

**Q6. Why is public-key cryptography often combined with symmetric encryption?**

Symmetric encryption efficiently protects large data, while public-key cryptography can securely establish or protect the symmetric key.

## Knapsack Cryptosystem

**Q7. What is the knapsack cryptosystem?**

The knapsack cryptosystem is a public-key cryptographic approach based on the subset-sum problem. A classic example is the Merkle–Hellman knapsack cryptosystem.

**Q8. What is the subset-sum problem?**

Given a set of numbers and a target value, the problem is to determine whether some subset of those numbers adds up to the target.

**Q9. What is a superincreasing sequence?**

A sequence is superincreasing if every element is greater than the sum of all previous elements.

**Example:** 2, 3, 7, 14.

**Q10. Why was a superincreasing sequence used in the Merkle–Hellman system?**

It makes the private subset-sum problem easy to solve. The system disguises this easy sequence using modular arithmetic to form the public key.

**Q11. Is the original Merkle–Hellman knapsack cryptosystem secure today?**

No. The classic Merkle–Hellman system was cryptanalyzed and is not considered secure for modern use.

## RSA Algorithm

**Q12. What is RSA?**

RSA is a public-key cryptographic algorithm whose security is based on the difficulty of factoring a large composite integer.

**Q13. What do the letters RSA represent?**

They are the initials of the algorithm's inventors: Rivest, Shamir and Adleman.

**Q14. What are the main steps in RSA key generation?**

1. Choose two large distinct prime numbers, p and q.
2. Calculate n = p × q.
3. Calculate φ(n) = (p − 1)(q − 1).
4. Choose a public exponent e that is coprime with φ(n).
5. Calculate the private exponent d, the modular inverse of e modulo φ(n).

**Q15. What is the RSA public key?**

The public key consists of (e, n).

**Q16. What is the RSA private key?**

The private key includes d and n, along with other values that may be stored to make decryption more efficient.

**Q17. What is the RSA encryption formula?**

For textbook RSA:

C = M^e mod n

Here, M is the encoded message representative and C is the ciphertext.

**Q18. What is the RSA decryption formula?**

For textbook RSA:

M = C^d mod n

**Q19. Why must e be coprime with φ(n)?**

This allows the modular inverse d of e modulo φ(n) to exist.

**Q20. What is the role of n in RSA?**

n is the modulus, calculated as the product of two large prime numbers p and q. It is part of both the public and private key.

**Q21. Is plain textbook RSA secure for real applications?**

No. Textbook RSA is deterministic and lacks secure padding. Real applications must use a secure scheme such as RSA-OAEP for encryption.

## ElGamal Cryptosystem

**Q22. What is ElGamal encryption?**

ElGamal is an asymmetric encryption scheme based on the difficulty of the discrete logarithm problem in a suitable group.

**Q23. What type of keys does ElGamal use?**

It uses a public key and a private key.

**Q24. What is the mathematical problem behind ElGamal?**

The discrete logarithm problem: given a generator g and a value g^x in a group, finding x is computationally difficult for appropriately chosen groups and parameters.

**Q25. Does ElGamal use randomness during encryption?**

Yes. It uses a fresh random ephemeral value for each encryption. Reusing or poorly generating this randomness can seriously compromise security.

**Q26. What is one important property of ElGamal ciphertext?**

For its basic form, encryption is probabilistic: encrypting the same message more than once with fresh randomness normally produces different ciphertexts.

**Q27. What is a disadvantage of basic ElGamal encryption?**

Its ciphertext is larger than the plaintext representation, commonly containing two group elements. It also requires careful parameter and randomness selection.

## Elliptic Curve Cryptography (ECC)

**Q28. What is Elliptic Curve Cryptography?**

ECC is a family of public-key cryptographic techniques based on mathematical operations involving points on elliptic curves over finite fields.

**Q29. What is the main advantage of ECC?**

ECC can provide strong security with significantly smaller key sizes than many traditional public-key systems such as RSA.

**Q30. What is the elliptic curve discrete logarithm problem (ECDLP)?**

Given points P and Q where Q = kP, the problem is to determine the integer k. For properly selected curves and parameters, this is computationally difficult.

**Q31. What is a point at infinity in elliptic curve cryptography?**

It is the identity element of the elliptic-curve group. Adding it to any point leaves that point unchanged.

**Q32. What is scalar multiplication in ECC?**

Scalar multiplication means repeatedly adding an elliptic-curve point to itself. For example, kP means adding P to itself k times.

**Q33. Is ECC an encryption algorithm by itself?**

ECC is a family of cryptographic techniques. It supports key agreement and digital signatures, and can be used in public-key encryption constructions. In practice, schemes such as ECIES combine elliptic-curve operations with symmetric encryption.

**Q34. What is the difference between RSA and ECC?**

| RSA | ECC |
|---|---|
| Based on integer factorization | Based on the elliptic-curve discrete logarithm problem |
| Typically needs larger keys for comparable security | Provides comparable security with smaller keys |
| Used for encryption and digital signatures | Used in key agreement, signatures and encryption constructions |

---

# Category 6: Important Comparisons for Quick Revision

## 1. DES vs AES vs IDEA

| Feature | DES | AES | IDEA |
|---|---:|---:|---:|
| Block size | 64 bits | 128 bits | 64 bits |
| Key size | 56 effective bits | 128, 192 or 256 bits | 128 bits |
| Rounds | 16 | 10, 12 or 14 | 8 rounds plus output transformation |
| Structure / design | Feistel network | Substitution-permutation network | Uses mixed algebraic operations |
| Modern status | Insecure | Widely used | Historically important; less commonly used today |

## 2. Block Cipher vs Stream Cipher

| Block Cipher | Stream Cipher |
|---|---|
| Processes fixed-size blocks | Generates a keystream |
| Examples: AES, DES, IDEA | Example: RC4 |
| May require a mode of operation for longer data | Combines keystream with data, commonly using XOR |

## 3. ECB vs CBC vs CTR

| Mode | Basic operation | Important point |
|---|---|---|
| ECB | Encrypts each block independently | Reveals patterns; generally avoid |
| CBC | XORs plaintext with previous ciphertext before encryption | Requires an IV and padding for incomplete final blocks |
| CTR | Encrypts counter values to generate a keystream | Supports parallel processing; counter/nonce reuse must be avoided |

## 4. RSA vs ElGamal vs ECC

| Algorithm / Family | Mathematical basis | Main idea |
|---|---|---|
| RSA | Integer factorization | Modular exponentiation using public and private exponents |
| ElGamal | Discrete logarithm problem | Randomized public-key encryption |
| ECC | Elliptic-curve discrete logarithm problem | Cryptography using elliptic-curve point operations |

---

# Category 7: Top 25 Questions to Prepare First

If you have limited revision time, prepare these questions first:

1. What is the difference between substitution and transposition ciphers?
2. What is the difference between symmetric and asymmetric encryption?
3. What is DES, and why is it insecure today?
4. What are the block size, effective key size and number of rounds in DES?
5. What is AES?
6. What are the block size and supported key sizes of AES?
7. Explain the four main transformations in AES.
8. What is IDEA? State its block size and key size.
9. What is a Feistel network?
10. What is a block cipher mode of operation?
11. What is the difference between ECB and CBC?
12. What is an initialization vector (IV)?
13. What is the difference between block and stream ciphers?
14. What is RC4, and why is it insecure?
15. What is public-key encryption?
16. What is the subset-sum problem in the knapsack cryptosystem?
17. What is a superincreasing sequence?
18. What is RSA, and what is its mathematical basis?
19. Explain the steps of RSA key generation.
20. State the RSA encryption and decryption formulas.
21. What is ElGamal, and what problem is its security based on?
22. Why does ElGamal use random values during encryption?
23. What is Elliptic Curve Cryptography (ECC)?
24. What is the elliptic curve discrete logarithm problem?
25. Why can ECC use smaller keys than RSA for comparable security levels?

---

## Final Revision Tips

1. Memorize the block sizes, key sizes and round counts of DES, AES and IDEA.
2. Understand the four AES transformations: SubBytes, ShiftRows, MixColumns and AddRoundKey.
3. Know the purpose and weaknesses of ECB and the basic operation of CBC and CTR.
4. Remember that RC4 is a stream cipher and is deprecated because of security weaknesses.
5. Understand the basic RSA key-generation steps and encryption/decryption formulas.
6. Learn the mathematical foundations of RSA, ElGamal and ECC.
7. Remember that the classic Merkle–Hellman knapsack cryptosystem is broken and should not be used today.

**Practical viva tip:** Examiners often ask for comparisons, key sizes, block sizes, rounds, formulas and the purpose of individual algorithm steps. Be ready to explain these without simply memorizing definitions.
