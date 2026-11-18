# **Information Security Practical Viva Questions with Answers**

**MCA – Information Security Practical Examination**

Prepared according to your six practicals. The questions cover basic concepts, algorithms, mathematical formulas, Python implementation, code-related questions, and possible examiner follow-up questions.

The answers are kept concise so you can revise them quickly before your practical examination.

# **Category 1: Extended Euclidean Algorithm**

### **Basic Concepts**

**Q1. What is the Euclidean Algorithm?**

The Euclidean Algorithm is a method to find the Greatest Common Divisor (GCD) of two integers.

**Q2. What is the Extended Euclidean Algorithm?**

It is an extension of the Euclidean Algorithm that calculates GCD along with two coefficients `x` and `y` satisfying:

\$$ ax+by=\gcd(a,b) \$$

**Q3. What is Bézout's Identity?**

Bézout's Identity states that for any two integers `a` and `b`, there exist integers `x` and `y` such that:

\$$ ax+by=\gcd(a,b) \$$

**Q4. What is the difference between Euclidean and Extended Euclidean Algorithm?**

- Euclidean Algorithm calculates only GCD.
- Extended Euclidean Algorithm calculates GCD and coefficients `x` and `y`.

**Q5. What is the base condition in the recursive Extended Euclidean Algorithm?**

When `b == 0`, the algorithm returns:

```
return a, 1, 0
```

Because:

\$$ a(1)+0(0)=a \$$

**Q6. What is the recursive relationship used in the algorithm?**

```
extended_gcd(b, a % b)
```

It repeatedly reduces the problem until the second number becomes zero.

**Q7. What is the purpose of&#x20;**`a // b`**&#x20;in the code?**

It performs integer division and calculates the quotient of `a` divided by `b`.

**Q8. What is the purpose of the modulo operator&#x20;**`%`**?**

It returns the remainder after division.

**Q9. What is the time complexity of the Extended Euclidean Algorithm?**

\$$ O(\log(\min(a,b))) \$$

**Q10. Where is the Extended Euclidean Algorithm used in cryptography?**

- Finding modular multiplicative inverses.
- RSA key generation.
- Modular arithmetic.
- Multiplicative Cipher decryption.

### **Numerical and Code-Based Questions**

**Q11. Find GCD of 34 and 367.**

\$$ \gcd(34,367)=1 \$$

**Q12. What are the coefficients for 34 and 367?**

\$$ 34(54)+367(-5)=1 \$$

Therefore:

- GCD = 1
- x = 54
- y = -5

**Q13. Can the Extended Euclidean Algorithm find the modular inverse?**

Yes. If:

\$$ \gcd(a,m)=1 \$$

Then the coefficient `x` obtained from Extended Euclidean Algorithm gives the modular inverse:

\$$ a^{-1}=x\bmod m \$$

**Q14. Does a modular inverse always exist?**

No. It exists only when the number and modulus are coprime.

**Q15. What happens if GCD of two numbers is not 1?**

They are not coprime. A modular inverse does not exist for one number under the modulus of the other.

# **Category 2: Additive Cipher – Encryption and Decryption**

### **Basic Concepts**

**Q1. What is a cipher?**

A cipher is an algorithm used to convert plaintext into ciphertext and vice versa using a key.

**Q2. What is the Additive Cipher?**

Additive Cipher is a substitution cipher in which each plaintext character is shifted by a fixed number of positions using a secret key.

It is also known as the Caesar or Shift Cipher.

**Q3. What is plaintext?**

The original readable message before encryption.

**Q4. What is ciphertext?**

The encrypted message that is not directly understandable.

**Q5. What is a key in Additive Cipher?**

A key is an integer between 0 and 25 that determines how many positions each character is shifted.

**Q6. What is the encryption formula?**

\$$ C=(P+K)\bmod 26 \$$

**Q7. What is the decryption formula?**

\$$ P=(C-K)\bmod 26 \$$

**Q8. Why do we use modulo 26?**

Because the English alphabet contains 26 letters. Modulo 26 ensures that shifting beyond Z starts again from A.

**Q9. What numerical values are assigned to alphabets?**

| Character | Value |
| --------- | ----- |
| A         | 0     |
| B         | 1     |
| C         | 2     |
| ...       | ...   |
| Z         | 25    |

**Q10. How many possible keys are available in Additive Cipher?**

There are 26 possible keys, from 0 to 25.

**Q11. What happens when the key is 0?**

The plaintext remains unchanged because no shifting occurs.

**Q12. What happens when the key is 3?**

Every character shifts three positions forward.

Example:

```
Plaintext  : HELLO
Key        : 3
Ciphertext : KHOOR
```

**Q13. Why is Additive Cipher called a substitution cipher?**

Because every plaintext character is replaced with another character, while its position remains unchanged.

**Q14. Does Additive Cipher require GCD?**

No.

**Q15. Does Additive Cipher require modular inverse?**

No. Decryption only requires subtracting the key.

### **Python Code-Based Questions**

**Q16. What is the purpose of&#x20;**`ord()`**?**

It returns the Unicode integer value of a character.

Example:

```
ord('A')  # 65
```

**Q17. What is the purpose of&#x20;**`chr()`**?**

It converts an integer Unicode value into its corresponding character.

Example:

```
chr(65)  # A
```

**Q18. Why do we subtract&#x20;**`ord('A')`**&#x20;from&#x20;**`ord(ch)`**?**

To convert an uppercase alphabet character into a number between 0 and 25.

**Q19. Why do we add&#x20;**`ord('A')`**&#x20;again?**

To convert the calculated alphabet position back into its corresponding uppercase character.

**Q20. Why do we use&#x20;**`isupper()`**&#x20;and&#x20;**`islower()`**?**

To identify whether a character is uppercase or lowercase and preserve its original case.

**Q21. Why do we use&#x20;**`result.append()`**&#x20;or&#x20;**`result +=`**?**

To store the encrypted or decrypted characters one by one.

**Q22. Why do we use&#x20;**`''.join(result)`**?**

To combine the individual characters into a single string.

**Q23. What happens to spaces and punctuation in your implementation?**

They remain unchanged because the code handles them using the `else` condition.

# **Category 3: Cryptanalysis of Additive Cipher**

### **Basic Concepts**

**Q1. What is cryptanalysis?**

Cryptanalysis is the process of analyzing ciphertext to recover the original plaintext without knowing the secret key.

**Q2. What is the difference between cryptography and cryptanalysis?**

- Cryptography focuses on securing information through encryption.
- Cryptanalysis focuses on breaking or analyzing encryption to recover information.

**Q3. What is brute-force attack?**

A brute-force attack tries every possible key until the correct plaintext is obtained.

**Q4. How many keys are tested in Additive Cipher cryptanalysis?**

All 26 possible keys are tested.

**Q5. Why is Additive Cipher vulnerable to brute-force attacks?**

Because it has only 26 possible keys, making it easy to test all combinations.

**Q6. Do we need the original key to perform cryptanalysis?**

No. We try all possible keys and identify the one that produces meaningful plaintext.

**Q7. What is the formula used during cryptanalysis?**

\$$ P=(C-K)\bmod 26 \$$

**Q8. How do we identify the correct key?**

By examining the decrypted outputs and identifying the one that forms meaningful English text.

**Q9. Is brute-force cryptanalysis always successful?**

For a short Additive Cipher message, it is generally easy to find the correct key. However, very short or ambiguous messages may produce multiple meaningful-looking results.

### **Python Code-Based Questions**

**Q10. Why do we use&#x20;**`range(26)`**?**

To generate all possible keys from 0 to 25.

**Q11. What is the purpose of&#x20;**`clean_text()`**?**

It removes non-alphabetic characters and converts the remaining text into uppercase.

**Q12. Why do we use nested loops in cryptanalysis?**

- Outer loop tries every possible key.
- Inner loop decrypts every character using that key.

**Q13. Does cryptanalysis require the encryption key?**

No. Its purpose is to discover the key.

**Q14. What is the difference between normal decryption and cryptanalysis?**

| Normal Decryption      | Cryptanalysis         |
| ---------------------- | --------------------- |
| Uses a known key       | Does not know the key |
| Decrypts directly      | Tries possible keys   |
| One decryption attempt | Multiple attempts     |

**Q15. Can we use frequency analysis instead of brute force?**

Yes. Frequency analysis examines the frequency of letters in ciphertext to identify likely substitutions.

# **Category 4: Multiplicative Cipher – Encryption and Decryption**

### **Basic Concepts**

**Q1. What is Multiplicative Cipher?**

Multiplicative Cipher is a substitution cipher in which each plaintext character is multiplied by a secret key modulo 26.

**Q2. What is its encryption formula?**

\$$ C=(P\times K)\bmod 26 \$$

**Q3. What is its decryption formula?**

\$$ P=(C\times K^{-1})\bmod 26 \$$

**Q4. What is a modular multiplicative inverse?**

It is a number that, when multiplied by another number, gives remainder 1 under a specified modulus.

\$$ K\times K^{-1}\bmod 26=1 \$$

**Q5. Why is modular inverse required in Multiplicative Cipher?**

Because multiplication cannot be reversed using ordinary division in modular arithmetic. We use the modular inverse to recover the original plaintext.

**Q6. What is the condition for a valid key?**

\$$ \gcd(K,26)=1 \$$

The key must be coprime with 26.

**Q7. Why must the key be coprime with 26?**

Because only numbers coprime with the modulus have a modular multiplicative inverse.

**Q8. What are the valid keys for Multiplicative Cipher modulo 26?**

```
1, 3, 5, 7, 9, 11,
15, 17, 19, 21, 23, 25
```

There are 12 valid keys.

**Q9. Why are 2, 4, 6, 8 and 10 invalid keys?**

Because their GCD with 26 is not 1.

For example:

\$$ \gcd(2,26)=2 \$$

Therefore, the modular inverse does not exist.

**Q10. Find the modular inverse of 5 modulo 26.**

\$$ 5\times21=105 \$$

\$$ 105\bmod26=1 \$$

Therefore:

\$$ 5^{-1}=21 \$$

**Q11. What is the difference between Additive and Multiplicative Cipher?**

| Additive Cipher             | Multiplicative Cipher      |
| --------------------------- | -------------------------- |
| Uses addition               | Uses multiplication        |
| \$C=(P+K)\bmod26\$        | \$C=(P\times K)\bmod26\$ |
| No modular inverse required | Modular inverse required   |
| 26 possible keys            | 12 valid keys              |

**Q12. Can we use any number as a key?**

No. The key must be coprime with 26.

### **Python Code-Based Questions**

**Q13. Why do we use&#x20;**`mod_inverse()`**?**

To calculate the modular inverse of the encryption key.

**Q14. Why do we use Extended Euclidean Algorithm here?**

To calculate the modular inverse efficiently.

**Q15. What does&#x20;**`return None`**&#x20;mean in modular inverse?**

It indicates that the modular inverse does not exist.

**Q16. What does&#x20;**`gcd(key, 26) != 1`**&#x20;indicate?**

It means the selected key is invalid for Multiplicative Cipher.

**Q17. Can we use the same key for encryption and decryption?**

Not directly. Decryption uses the modular inverse of the encryption key.

**Q18. Is Multiplicative Cipher stronger than Additive Cipher?**

Both are weak classical substitution ciphers. Multiplicative Cipher has 12 valid keys, whereas Additive Cipher has 26 possible keys. Neither is secure by modern standards.

# **Category 5: Cryptanalysis of Multiplicative Cipher**

### **Basic Concepts**

**Q1. What is cryptanalysis of Multiplicative Cipher?**

It is the process of recovering the plaintext and secret key from ciphertext without knowing the original key.

**Q2. Which attack is used in your practical?**

Brute-force attack.

**Q3. How many possible valid keys are tested?**

12 valid keys.

**Q4. Why don't we test all 26 keys?**

Because only 12 keys are coprime with 26 and have modular inverses.

**Q5. What formula is used to decrypt during cryptanalysis?**

\$$ P=(C\times K^{-1})\bmod26 \$$

**Q6. Why do we calculate the modular inverse for every key?**

Because every valid encryption key has a corresponding modular inverse needed for decryption.

**Q7. How do we identify the correct key?**

By examining the decrypted outputs and finding meaningful English text.

**Q8. What is the role of GCD in cryptanalysis?**

It helps identify valid keys by checking whether:

\$$ \gcd(K,26)=1 \$$

**Q9. Can we use Extended Euclidean Algorithm in cryptanalysis?**

Yes. It is used to calculate modular inverses for valid keys.

### **Python Code-Based Questions**

**Q10. What is the purpose of this code?**

```
valid_keys = [k for k in range(1, 26) if gcd(k, 26) == 1]
```

It generates all valid encryption keys that are coprime with 26.

**Q11. What is the purpose of&#x20;**`inv = mod_inverse(key, 26)`**?**

It calculates the modular inverse of the current key.

**Q12. Why do we use a loop inside another loop?**

- Outer loop tries all valid keys.
- Inner loop decrypts every character using the current key.

**Q13. Is the original key required during cryptanalysis?**

No.

**Q14. What is the main difference between Additive and Multiplicative cryptanalysis?**

Additive cryptanalysis tries all 26 possible keys, whereas Multiplicative cryptanalysis tries only 12 valid keys and uses modular inverses for decryption.

# **Category 6: Columnar Transposition Cipher**

### **Basic Concepts**

**Q1. What is Columnar Transposition Cipher?**

It is a classical encryption technique in which plaintext characters are rearranged according to the alphabetical order of a keyword.

**Q2. Is Columnar Transposition a substitution cipher?**

No. It is a transposition cipher.

**Q3. What is the difference between substitution and transposition cipher?**

- Substitution cipher replaces characters with other characters.
- Transposition cipher rearranges the positions of existing characters.

**Q4. What is the role of the key in Columnar Transposition Cipher?**

The key determines the order in which columns are read during encryption.

**Q5. How is the plaintext arranged?**

The plaintext is arranged row by row in a grid.

**Q6. How is ciphertext generated?**

The columns are read according to the alphabetical order of the keyword characters.

**Q7. Why do we use padding?**

To complete the grid when the message length is not divisible by the number of columns.

**Q8. Which padding character is used in your implementation?**

`X`.

**Q9. Is padding always necessary?**

No. It is required when the message length is not an exact multiple of the number of columns in this implementation.

**Q10. How is decryption performed?**

The ciphertext is placed into columns according to the alphabetical order of the key. Then the grid is read row by row.

**Q11. Does Columnar Transposition change the actual characters?**

No. It only changes their positions.

### **Example-Based Questions**

**Q12. What happens if the keyword is DUCS?**

The alphabetical order is:

| Character | Original index | Alphabetical position |
| --------- | -------------- | --------------------- |
| D         | 0              | 2                     |
| U         | 1              | 4                     |
| C         | 2              | 1                     |
| S         | 3              | 3                     |

Therefore, columns are read in the order:

```
C → D → S → U
```

**Q13. What happens if the message is shorter than the grid size?**

Padding characters are added until the grid is complete.

**Q14. What happens if the key contains repeated letters?**

Repeated letters are ordered according to their original positions when a stable sorting method such as Python's `sorted()` is used.

**Q15. What happens if we use a different key during decryption?**

The original plaintext will generally not be recovered correctly.

### **Python Code-Based Questions**

**Q16. What is the purpose of&#x20;**`get_order(key)`**?**

It determines the alphabetical order of the key characters.

**Q17. Explain this code:**

```
sorted(range(len(key)), key=lambda i: key[i])
```

- `range(len(key))` generates column indices.
- `key[i]` accesses the character at the given index.
- `lambda` tells Python to sort indices based on their corresponding key characters.
- `sorted()` returns the indices in alphabetical order.

**Q18. What is the purpose of&#x20;**`len(key)`**?**

It determines the number of columns in the grid.

**Q19. What is the purpose of this code?**

```
rows = len(message) // cols
```

It calculates the number of rows required in the grid after padding.

**Q20. What is the purpose of&#x20;**`list()`**&#x20;while creating the grid?**

It converts a string into a list of individual characters.

**Q21. What is the purpose of&#x20;**`grid[r][c]`**?**

It accesses the character at row `r` and column `c`.

**Q22. What is the purpose of&#x20;**`join()`**?**

It combines multiple characters into a single string.

**Q23. Why do we use&#x20;**`rstrip("X")`**&#x20;during decryption?**

To remove the padding characters added during encryption.

**Q24. What is the limitation of using&#x20;**`rstrip("X")`**?**

If the original plaintext genuinely ends with `X`, it may also be removed. A more robust implementation would store the original message length or padding count.

**Q25. Is Columnar Transposition Cipher secure for modern communication?**

No. It is a classical cipher and can be broken using cryptanalysis.

# **Category 7: Common Information Security Viva Questions**

These questions are important because examiners often ask general security concepts even when the practical is based on a specific algorithm.

**Q1. What is Information Security?**

Information Security is the practice of protecting information from unauthorized access, modification, disclosure, or destruction.

**Q2. What are the three main principles of Information Security?**

The CIA Triad:

- Confidentiality
- Integrity
- Availability

**Q3. What is confidentiality?**

Ensuring that information is accessible only to authorized individuals.

**Q4. What is integrity?**

Ensuring that information remains accurate and has not been modified without authorization.

**Q5. What is availability?**

Ensuring that information and services are available whenever authorized users need them.

**Q6. What is encryption?**

Encryption is the process of converting plaintext into ciphertext using an algorithm and a key.

**Q7. What is decryption?**

Decryption is the process of converting ciphertext back into plaintext.

**Q8. What is a symmetric encryption algorithm?**

An encryption algorithm that uses the same secret key for encryption and decryption.

Examples: AES and DES.

**Q9. What is an asymmetric encryption algorithm?**

An encryption algorithm that uses a public key and a private key.

Example: RSA.

**Q10. What is the difference between hashing and encryption?**

| Hashing                         | Encryption                            |
| ------------------------------- | ------------------------------------- |
| One-way process                 | Reversible process                    |
| No decryption                   | Can be decrypted with the correct key |
| Used for integrity verification | Used for confidentiality              |
| Example: SHA-256                | Example: AES                          |

**Q11. What is a cryptographic key?**

A key is a value used by a cryptographic algorithm to encrypt, decrypt, or authenticate information.

**Q12. What is a brute-force attack?**

An attack that attempts every possible key or password until the correct one is found.

**Q13. What is a hash function?**

A hash function converts input data of arbitrary length into a fixed-length output.

**Q14. Can two different messages produce the same hash?**

Yes. This is called a hash collision.

**Q15. What is the difference between a block cipher and a stream cipher?**

- Block cipher encrypts data in fixed-size blocks.
- Stream cipher encrypts data one bit or byte at a time.

**Q16. What is modular arithmetic?**

It is arithmetic in which numbers wrap around after reaching a specified modulus.

For example:

\$$ 29\bmod26=3 \$$

**Q17. What is coprime?**

Two integers are coprime if their GCD is 1.

**Q18. What is the purpose of the modulo operation in classical ciphers?**

It keeps the resulting alphabet positions within the range 0–25.

**Q19. What is the difference between a classical and modern cipher?**

Classical ciphers generally use simple substitution or transposition techniques, while modern ciphers use mathematically sophisticated algorithms designed to resist computational attacks.

**Q20. What is the difference between authentication and authorization?**

- Authentication verifies who a user is.
- Authorization determines what that user is allowed to access.

# **Category 8: Important Mathematical and Practical Revision**

These are particularly useful for quick revision immediately before the examination.

## **1. Important formulas**

| Practical                 | Formula                         |
| ------------------------- | ------------------------------- |
| Extended Euclidean        | \$ax+by=\gcd(a,b)\$           |
| Additive Encryption       | \$C=(P+K)\bmod26\$            |
| Additive Decryption       | \$P=(C-K)\bmod26\$            |
| Multiplicative Encryption | \$C=(P\times K)\bmod26\$      |
| Multiplicative Decryption | \$P=(C\times K^{-1})\bmod26\$ |
| Modular Inverse           | \$K\times K^{-1}\bmod26=1\$   |

## **2. Important values to remember**

| Concept                                           | Answer               |
| ------------------------------------------------- | -------------------- |
| Number of English alphabets                       | 26                   |
| Additive Cipher keys                              | 26                   |
| Multiplicative Cipher valid keys                  | 12                   |
| Additive Cipher key range                         | 0–25                 |
| Multiplicative Cipher key condition               | GCD(K, 26) = 1       |
| Modular inverse of 5 mod 26                       | 21                   |
| Modular inverse of 7 mod 26                       | 15                   |
| Modular inverse of 3 mod 26                       | 9                    |
| Padding character in your columnar implementation | X                    |
| Columnar Transposition type                       | Transposition cipher |

## **3. Python functions you should know**

| Function / Operator | Purpose                            |
| ------------------- | ---------------------------------- |
| `ord()`             | Character to Unicode integer       |
| `chr()`             | Integer to character               |
| `range()`           | Generates a sequence of numbers    |
| `len()`             | Returns length                     |
| `append()`          | Adds an element to a list          |
| `join()`            | Combines strings                   |
| `sorted()`          | Sorts elements                     |
| `lambda`            | Creates a small anonymous function |
| `isupper()`         | Checks uppercase character         |
| `islower()`         | Checks lowercase character         |
| `//`                | Integer division                   |
| `%`                 | Modulo / remainder                 |
| `**`                | Exponentiation                     |

# **Category 9: Most Important Questions to Prepare First**

If you have limited revision time, prioritize these 25 questions. These cover the central logic of all six practicals.

**Your revision checklist**

0/25 completed

1\. Explain the Extended Euclidean Algorithm.

2\. What is Bézout's Identity?

3\. What is the difference between Euclidean and Extended Euclidean Algorithm?

4\. How is modular inverse calculated using Extended Euclidean Algorithm?

5\. What is Additive Cipher?

6\. Explain the encryption and decryption formulas of Additive Cipher.

7\. Why do we use modulo 26?

8\. Why does Additive Cipher not require modular inverse?

9\. What is cryptanalysis?

10\. What is a brute-force attack?

11\. How many possible keys are there in Additive Cipher?

12\. What is Multiplicative Cipher?

13\. Why is modular inverse required in Multiplicative Cipher?

14\. Why must the multiplicative key be coprime with 26?

15\. What are the 12 valid multiplicative keys?

16\. How do you find the modular inverse of 5 modulo 26?

17\. How does brute-force cryptanalysis work for Multiplicative Cipher?

18\. What is the difference between Additive and Multiplicative Cipher?

19\. What is Columnar Transposition Cipher?

20\. What is the difference between substitution and transposition?

21\. How does the keyword determine column order?

22\. Why is padding required in Columnar Transposition?

23\. Explain the purpose of the lambda function in get_order().

24\. What happens if the wrong key is used during decryption?

25\. What is the difference between encryption, hashing and cryptanalysis?

Reset checklist

## **My recommendation for your practical examination**

Prepare in this order:

1. Understand the logic and mathematical formulas of all six practicals.
2. Learn why each important Python function is used.
3. Practice explaining your code without looking at it.
4. Practice at least one numerical example for Extended GCD, Additive Cipher and Multiplicative Cipher.
5. Understand the difference between normal decryption and cryptanalysis.

**One important tip:** In a practical viva, the examiner may point to any line in your code and ask, "Why did you write this?" So don't just memorize the answers. Understand the purpose of each function, loop, condition and mathematical operation.