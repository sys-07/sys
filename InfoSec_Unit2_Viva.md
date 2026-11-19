# Information Security – Unit II (Viva Notes)

**Cryptography: Classical ciphers · DES · AES · IDEA · Block modes · RC4 · Knapsack · RSA · ElGamal · ECC**

> For every algorithm, be ready with: **What is it? → Block/key size & rounds → Simple steps → Is it secure today?**

---

## 1. Basic Terms

**Q. Cryptography?**
Science of protecting information by converting it into a form only authorized people can read or verify.

**Q. Plaintext / Ciphertext?**
Plaintext = original readable message. Ciphertext = scrambled, encrypted message.

**Q. Encryption / Decryption?**
Encryption: plaintext → ciphertext using an algorithm + key.
Decryption: ciphertext → plaintext using the right key.

**Q. Cipher vs Encryption?**
Cipher = the **algorithm** (AES, RSA). Encryption = the **process** of using it.

**Q. Key?**
Secret value that controls the algorithm's output. Same algorithm + different key = different ciphertext.

**Q. Cryptanalysis?**
Breaking ciphers without knowing the key. Cryptology = cryptography + cryptanalysis.

**Q. Kerckhoffs's principle?**
The system should stay secure even if **everything except the key** is public. Security lies in the key, not in hiding the algorithm.

**Q. Confusion vs Diffusion (Shannon)?**
- **Confusion:** hides the relation between **key and ciphertext** → done by **substitution** (S-boxes).
- **Diffusion:** spreads one plaintext bit's effect over many ciphertext bits → done by **permutation/transposition**.

**Q. Avalanche effect?**
Changing **one bit** of input or key changes **about half** the output bits. Good ciphers and hashes show this.

**Q. Symmetric vs Asymmetric?**
| Symmetric | Asymmetric (Public-key) |
|---|---|
| One shared secret key | Key pair: public + private |
| Fast, good for bulk data | Slow, used for small data/keys |
| Problem: key distribution | Solves key distribution |
| AES, DES, IDEA, RC4 | RSA, ElGamal, ECC, Knapsack |

**Q. Public and private key together are called?**
A **key pair**.

---

## 2. Classical Ciphers – Substitution and Transposition

**Q. Substitution cipher?**
**Replaces** each letter with another letter/symbol. Letters change, positions stay.

**Q. Transposition cipher?**
**Rearranges** the positions of letters. Letters stay the same, order changes.

**Q. Substitution vs Transposition?**
Substitution → *what* the letter is changes. Transposition → *where* the letter is changes.
(Frequency of letters is preserved in transposition – that's how you recognise it.)

### Substitution ciphers (one line each)

**Caesar cipher:** shift each letter by fixed key (k = 3). `C = (P + k) mod 26`. HELLO → KHOOR. Only 25 keys → easy brute force.

**Monoalphabetic cipher:** each letter maps to a fixed other letter (26! keys). Broken by **frequency analysis** (E is most common in English).

**Playfair cipher:** 5×5 key matrix (I/J together); encrypts **pairs of letters (digraphs)**.
Rules: same row → take letter to the right; same column → take letter below; otherwise → swap columns (rectangle rule).

**Vigenère cipher:** **polyalphabetic** – uses a keyword; each letter shifted by the matching key letter. Same plaintext letter can become different ciphertext letters.

**Hill cipher:** uses **matrix multiplication** mod 26 on blocks of letters. Key matrix must be invertible (to decrypt).

**One-Time Pad (Vernam):** key is **random, as long as the message, used only once**. Theoretically **unbreakable** (perfect secrecy). Problem: key distribution.

### Transposition ciphers

**Rail Fence:** write the message in a zig-zag over *n* rows, read row by row.
HELLOWORLD (2 rails) → HLOOL + ELWRD → **HLOOLELWRD**.

**Columnar transposition:** write message in rows under a keyword, read **columns** in alphabetical order of the keyword.

---

## 3. Block Cipher Basics and Feistel Structure

**Q. Block cipher?**
Encrypts data in **fixed-size blocks** (64 or 128 bits) using a key. Ex: DES, AES, IDEA.

**Q. Stream cipher?**
Encrypts data **bit by bit / byte by byte** by XORing it with a keystream. Ex: RC4.

**Q. What is a Feistel network/structure? (steps)**
1. Split block into two halves: **L** and **R**.
2. Each round: `L(new) = R`, `R(new) = L XOR F(R, round key)`.
3. Repeat for many rounds.
- **Big advantage:** encryption and decryption use the **same structure**, just **reverse the round keys**. F need not be reversible.
- Used by **DES**. (AES is **not** Feistel – it is an SPN.)

**Q. What is an SPN?**
Substitution-Permutation Network – each round does substitution (S-box) + permutation + key mixing on the **whole block**. Used by AES. Decryption needs **inverse** operations.

---

## 4. DES – Data Encryption Standard

**Q. What is DES?**
Symmetric **block cipher** by IBM, adopted as US standard in **1977**. Uses a **Feistel** structure.

**Key facts:**
| Block | Key | Rounds | Subkey |
|---|---|---|---|
| 64 bits | 64 bits given, **56 effective** (8 parity bits) | **16** | 48 bits per round |

**Q. How does DES work? (simple steps)**
1. **Initial Permutation (IP)** – rearrange the 64 plaintext bits.
2. **Split** into Left (32) and Right (32).
3. **16 rounds**, each:
   - **Expansion:** R expanded 32 → 48 bits.
   - **XOR** with 48-bit round key.
   - **S-boxes (8 of them):** 48 → 32 bits (the only non-linear step, gives confusion).
   - **P-box permutation** of the 32 bits.
   - **XOR with Left half**, then **swap** halves.
4. **Final Permutation (FP = inverse of IP)** → 64-bit ciphertext.

**Q. How are DES round keys generated?**
56-bit key → split into two 28-bit halves → **left circular shift** each round (1 or 2 bits) → **compression permutation (PC-2)** picks 48 bits = round key.

**Q. DES decryption?**
**Same algorithm**, round keys used in **reverse order (K16 → K1)**. (Feistel advantage.)

**Q. Why is DES insecure?**
56-bit key is too small – can be **brute-forced** (EFF cracked it in 1998 in ~56 hours).

**Q. What is 2DES and why not used?**
Double encryption with two keys – vulnerable to **meet-in-the-middle attack**, so security is only ~57 bits, not 112.

**Q. What is 3DES?**
DES applied **3 times: Encrypt–Decrypt–Encrypt (EDE)** with 2 or 3 keys (112 / 168-bit). More secure but **slow**; now deprecated, replaced by AES.

---

## 5. AES – Advanced Encryption Standard

**Q. What is AES?**
Symmetric **block cipher**, chosen by NIST in **2001** to replace DES. Original name **Rijndael** (by Daemen and Rijmen). Uses an **SPN** structure, not Feistel.

**Key facts:**
| Key size | Rounds |
|---|---|
| 128 bits | 10 |
| 192 bits | 12 |
| 256 bits | 14 |
Block size is **always 128 bits**.

**Q. How does AES work? (simple steps)**
1. Arrange 128-bit plaintext into a **4×4 byte matrix (State)**.
2. **Key Expansion** – generate round keys from the main key.
3. **Initial round:** AddRoundKey.
4. **Main rounds** (9 for AES-128), each:
   - **SubBytes** – replace each byte using the **S-box** (confusion).
   - **ShiftRows** – row 0 no shift, row 1 shift left by 1, row 2 by 2, row 3 by 3 (diffusion).
   - **MixColumns** – mix the 4 bytes of each column using GF(2⁸) math (diffusion).
   - **AddRoundKey** – XOR state with the round key.
5. **Final round:** SubBytes, ShiftRows, AddRoundKey (**no MixColumns**).
6. Output = ciphertext.

**Q. AES decryption?**
Apply the **inverse** steps in reverse: InvShiftRows (shift right), InvSubBytes (inverse S-box), AddRoundKey, InvMixColumns, using round keys in **reverse order**. Final round skips InvMixColumns.

**Q. Why is MixColumns skipped in the last round?**
It adds no security at the end and makes encryption and decryption structure symmetric/efficient.

**Q. Only step that uses the key?**
**AddRoundKey.**

**Q. Why AES over DES?**
Bigger block (128 vs 64), bigger keys (128–256 vs 56), faster, no practical attack known.

---

## 6. IDEA – International Data Encryption Algorithm

**Q. What is IDEA?**
Symmetric **block cipher** by **Xuejia Lai and James Massey (1991)**. Famous for being used in **PGP** (email security).

**Key facts:**
| Block | Key | Rounds | Subkeys |
|---|---|---|---|
| 64 bits | 128 bits | **8 rounds + 1 output transformation (8.5)** | **52** subkeys of 16 bits (6 per round × 8 + 4) |

**Q. How does IDEA work? (simple steps)**
1. Split 64-bit block into **four 16-bit sub-blocks**.
2. Generate **52 subkeys** (16-bit each) from the 128-bit key.
3. **8 rounds**, each mixes the sub-blocks with 6 subkeys using **three different operations**:
   - **XOR** (⊕)
   - **Addition mod 2¹⁶** (⊞)
   - **Multiplication mod 2¹⁶ + 1** (⊙)
4. **Output transformation** (half round) with the last 4 subkeys → 64-bit ciphertext.

**Q. What makes IDEA strong?**
Mixing **three algebraically incompatible operations** – no S-boxes needed.

**Q. IDEA decryption?**
Same structure, using **inverse subkeys** (additive and multiplicative inverses) in reverse order.

---

## 7. Block Cipher Modes of Operation

**Q. Why do we need modes?**
A block cipher encrypts only one block; modes define how to encrypt **long messages** with many blocks.

| Mode | How it works (1 line) | Remember |
|---|---|---|
| **ECB** – Electronic Codebook | Each block encrypted **independently** | Same plaintext block → same ciphertext → **leaks patterns** (ECB penguin). Avoid. |
| **CBC** – Cipher Block Chaining | Plaintext block **XOR previous ciphertext**, then encrypt. First block uses **IV** | Hides patterns; needs IV + padding; encryption not parallel |
| **CFB** – Cipher Feedback | Encrypt previous ciphertext → XOR with plaintext | Turns block cipher into **stream** cipher |
| **OFB** – Output Feedback | Encrypt previous **output** repeatedly → keystream → XOR | Stream-like; errors **don't propagate** |
| **CTR** – Counter | Encrypt a **counter** (nonce + 1, 2, 3…) → keystream → XOR | **Parallel**, fast; never reuse counter |
| **GCM** | CTR + authentication tag | Gives confidentiality **+ integrity** (used in TLS) |

**Q. What is an IV?**
Initialization Vector – random/unique starting value so the **same message encrypts differently** each time.

**Q. What is padding?**
Extra bytes added to make the last block full size (needed in ECB/CBC). CFB, OFB, CTR don't need it.

---

## 8. Stream Cipher – RC4

**Q. What is RC4?**
Symmetric **stream cipher** by **Ron Rivest (1987)**. Generates a pseudo-random **keystream** that is **XORed** with plaintext byte by byte. Key size variable: 1–256 bytes (40–2048 bits).

**Q. How does RC4 work? (simple steps)**
**Stage 1 – KSA (Key Scheduling Algorithm):**
1. Create array **S[0..255]**, fill with S[i] = i.
2. Shuffle S using the key: `j = (j + S[i] + K[i mod keylen]) mod 256`, then **swap S[i], S[j]**.

**Stage 2 – PRGA (Pseudo-Random Generation Algorithm):**
1. `i = (i + 1) mod 256`, `j = (j + S[i]) mod 256`
2. Swap S[i], S[j]
3. Keystream byte **= S[(S[i] + S[j]) mod 256]**

**Stage 3:** Ciphertext = Plaintext **XOR** Keystream.

**Q. RC4 decryption?**
Generate the **same keystream** with the same key and **XOR again** (XOR is its own inverse).

**Q. Why is RC4 insecure?**
**Biases** in the first keystream bytes and weak key scheduling. Broke **WEP** Wi-Fi; banned in TLS (2015).

**Q. Where was RC4 used?**
WEP, WPA (TKIP), old SSL/TLS.

---

## 9. Public-Key Cryptography – Basics

**Q. What is public-key (asymmetric) encryption?**
Uses a **key pair**. Public key is shared openly; private key is kept secret.

**Q. Flow for confidentiality (Alice → Bob)?**
1. Bob generates key pair, shares **public key**.
2. Alice encrypts with **Bob's public key**.
3. Only Bob decrypts with **Bob's private key**.
> **Encrypt with receiver's public key, decrypt with receiver's private key.**

**Q. What is a trapdoor one-way function?**
Easy to compute one way, very hard to reverse – **unless** you know a secret (the trapdoor = private key).
Ex: RSA – multiplying p × q is easy, factoring n is hard.

**Q. Why is public-key combined with symmetric (hybrid encryption)?**
Public-key is slow → used only to exchange a **symmetric key**; then AES encrypts the actual data. Ex: **HTTPS/TLS**.

---

## 10. Knapsack Cryptosystem (Merkle–Hellman, 1978)

**Q. What is it?**
Public-key system based on the **subset-sum (knapsack) problem**: given numbers and a total, find which numbers add to that total – hard in general.

**Q. Superincreasing sequence?**
Each number is **greater than the sum of all previous ones**. Ex: 2, 3, 7, 14, 30.
Subset-sum on it is **easy** (greedy, from largest down).

**Q. How does it work? (simple steps)**
**Key generation:**
1. Choose a superincreasing sequence **W** (private).
2. Choose **q > sum(W)** and **r** coprime with q (private).
3. Public key: **bᵢ = r × wᵢ mod q** (looks like a random, hard knapsack).

**Encryption:** For each **1-bit** in the message, add the matching bᵢ → **C = sum**.

**Decryption:**
1. Compute **C' = C × r⁻¹ mod q**.
2. Solve the easy superincreasing knapsack on C' → get the bits back.

**Q. Is it secure?**
**No.** Broken by **Adi Shamir (1982)** in polynomial time. Only historically important.

---

## 11. RSA (Rivest–Shamir–Adleman, 1977)

**Q. What is RSA?**
Most popular public-key algorithm. Security based on the difficulty of **factoring a large number n = p × q**. Used for **encryption and digital signatures**.

**Q. RSA key generation (steps):**
1. Choose two large primes **p, q**.
2. **n = p × q**
3. **φ(n) = (p − 1)(q − 1)**
4. Choose **e** such that 1 < e < φ(n) and **gcd(e, φ(n)) = 1**.
5. Find **d** such that **(d × e) mod φ(n) = 1** (d = e⁻¹ mod φ(n)).
- **Public key = (e, n)**, **Private key = (d, n)**.

**Q. Formulas:**
- Encryption: **C = Mᵉ mod n**
- Decryption: **M = Cᵈ mod n**

**Small example (good to quote in viva):**
p = 3, q = 11 → n = 33, φ(n) = 20, e = 3, d = 7 (since 3 × 7 = 21 ≡ 1 mod 20).
M = 4 → C = 4³ mod 33 = 64 mod 33 = **31**. Decrypt: 31⁷ mod 33 = **4**. ✔

**Q. Why must e be coprime to φ(n)?**
Otherwise the inverse **d** does not exist.

**Q. What is the trapdoor in RSA?**
Knowing **p and q (→ d)**. Without it, reversing encryption requires factoring n.

**Q. Typical key size today?**
2048 bits or more.

**Q. Is textbook RSA safe?**
No – it's deterministic. Real systems use padding like **OAEP**.

---

## 12. ElGamal (Taher ElGamal, 1985)

**Q. What is ElGamal?**
Public-key encryption based on the **Discrete Logarithm Problem (DLP)**: given g, p and gˣ mod p, finding **x** is hard.

**Q. How does it work? (simple steps)**
**Key generation:**
1. Choose large prime **p** and generator **g**.
2. Choose private key **x**.
3. Public key: **y = gˣ mod p** → publish (p, g, y).

**Encryption** (message M):
1. Pick a **random k** (new every time).
2. **C1 = gᵏ mod p**
3. **C2 = M × yᵏ mod p**
4. Ciphertext = **(C1, C2)**.

**Decryption:**
**M = C2 × (C1ˣ)⁻¹ mod p**

**Q. Key property of ElGamal?**
**Probabilistic** – same message gives **different ciphertexts** each time (due to random k).

**Q. Disadvantage?**
Ciphertext is **double the size** of the plaintext (C1, C2). If k is reused, security breaks.

**Q. RSA vs ElGamal?**
RSA → factoring, deterministic. ElGamal → discrete log, randomized, bigger ciphertext.

---

## 13. Elliptic Curve Cryptography (ECC)

**Q. What is ECC?**
Public-key cryptography based on **points on an elliptic curve** over a finite field. Proposed by **Koblitz and Miller (1985)**.
Curve equation: **y² = x³ + ax + b (mod p)**.

**Q. Problem behind ECC?**
**ECDLP (Elliptic Curve Discrete Log Problem):** given points **P** and **Q = kP**, finding **k** is hard.

**Q. How does it work? (simple steps)**
1. Agree on a curve and a **base point G**.
2. Private key = random number **d**.
3. Public key = **Q = d × G** (point multiplication = adding G to itself d times).
4. Used for key exchange (**ECDH**), signatures (**ECDSA**) and encryption (**ECIES** / EC-ElGamal).

**Q. ECDH in one line?**
Alice sends dₐG, Bob sends d_bG; both compute **dₐd_bG** = shared secret.

**Q. Main advantage?**
**Same security with much smaller keys** → faster, less memory, ideal for mobiles/IoT.
**256-bit ECC ≈ 3072-bit RSA.**

**Q. Point at infinity?**
The **identity element** of the curve group (P + O = P).

**Q. RSA vs ECC?**
| RSA | ECC |
|---|---|
| Factoring problem | ECDLP |
| Large keys (2048–3072) | Small keys (256) |
| Slower | Faster, low power |

---

## 14. Bonus (from your doubts – may come as follow-ups)

**Q. Hashing?**
**One-way** function that turns any data into a **fixed-length** digest. Can't be reversed. Used for **integrity** and password storage. Ex: SHA-256 (256-bit = 64 hex chars).
Collisions are possible in theory, but practically impossible to find for good hashes.

**Q. Digital signature (steps)?**
1. Alice **hashes** the message.
2. Alice **signs the hash with her private key** (older books: "encrypts the hash with private key").
3. Sends **message + signature**.
4. Bob verifies using **Alice's public key** and compares hashes.
- Gives **authentication, integrity, non-repudiation** – **not confidentiality** (message is not encrypted).
> **Sign with private key, verify with public key.**

**Q. MAC vs Digital signature?**
MAC uses a **shared secret key** (integrity + authentication, no non-repudiation). Digital signature uses a **key pair** (adds non-repudiation).

---

## Last-Minute Recap

| Algorithm | Type | Block | Key | Rounds | Based on |
|---|---|---|---|---|---|
| DES | Symmetric block (Feistel) | 64 | 56 | 16 | – |
| 3DES | Symmetric block | 64 | 112/168 | 48 | EDE |
| AES | Symmetric block (SPN) | 128 | 128/192/256 | 10/12/14 | – |
| IDEA | Symmetric block | 64 | 128 | 8.5 | XOR, add, multiply |
| RC4 | Symmetric stream | – | 40–2048 | – | KSA + PRGA |
| Knapsack | Public key | – | – | – | Subset-sum (broken) |
| RSA | Public key | – | 2048+ | – | Factoring |
| ElGamal | Public key | – | – | – | Discrete log |
| ECC | Public key | – | 256 | – | ECDLP |

- Substitution = change letters; Transposition = change positions.
- Confusion = S-box (substitution); Diffusion = permutation.
- DES decrypt = same steps, reverse keys. AES decrypt = inverse steps.
- AES round: **SubBytes → ShiftRows → MixColumns → AddRoundKey** (last round: no MixColumns).
- ECB leaks patterns; CBC uses IV + chaining; CTR is parallel.
- RSA: n = pq, φ = (p−1)(q−1), ed ≡ 1 mod φ, C = Mᵉ mod n, M = Cᵈ mod n.
- Encrypt with **receiver's public key**; sign with **sender's private key**.
