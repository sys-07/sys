# Information Security – Unit I (Viva Notes)

**Overview of Security · Security Threats and Models**

> Answer like this in the viva: **one-line definition → one example → one difference (if asked).**

---

## 1. Overview of Security

**Q. What is information security?**
Protecting information and systems from unauthorized access, use, disclosure, modification or destruction.

**Q. Protection vs Security?**
- **Protection** = *internal* mechanism that controls which user/process can access which resource (e.g., file permissions).
- **Security** = *broader* goal of defending the system against *external and internal* threats/attacks. Protection is one part of security.
- One line: *Protection is the mechanism, security is the overall defence.*

**Q. What are the aspects (goals) of security?**
Confidentiality, Integrity, Availability (CIA triad) + Privacy.

**Q. Confidentiality?**
Only authorized people can **read** the data.
Example: encrypting a file. Attack on it: eavesdropping / tapping.

**Q. Data integrity?**
Data is **not changed** without authorization.
Example: a hash detects if a file was modified. Attack on it: modifying a bank balance.

**Q. Availability?**
Data and services are **accessible when needed** by authorized users.
Attack on it: DoS / DDoS. Protected by backups, redundancy.

**Q. Privacy?**
The right of a person to control how **their personal data** is collected, used and shared.

**Q. Confidentiality vs Privacy?**
- Confidentiality → *who* can access the data.
- Privacy → *how personal data is used* and whether the owner agreed to it.

**Q. Which cryptographic tool gives which goal?**
| Goal | Tool |
|---|---|
| Confidentiality | Encryption (AES, RSA) |
| Integrity | Hashing, MAC |
| Authentication + Non-repudiation | Digital signature |
| Availability | Not cryptography → backups, redundancy |

**Q. Types of security attacks (classic 4)?**
| Attack | Goal attacked | Example |
|---|---|---|
| Interruption | Availability | DoS, cutting a cable |
| Interception | Confidentiality | Wiretapping |
| Modification | Integrity | Changing a message in transit |
| Fabrication | Authenticity | Inserting a fake message |

**Q. Passive vs Active attack?**
- **Passive:** only observes/listens, does not change data. Hard to detect. Ex: tapping, traffic analysis.
- **Active:** modifies, deletes or creates data. Ex: DoS, masquerade, replay, modification.

---

## 2. User Authentication

**Q. What is authentication?**
Verifying **who you are** (identity of a user/device).

**Q. Identification vs Authentication vs Authorization?**
- Identification → *claiming* an identity (typing username).
- Authentication → *proving* it (entering password).
- Authorization → deciding *what you are allowed to do* (read/write permission).
- Order: Identification → Authentication → Authorization.

**Q. Three authentication factors?**
1. Something you **know** – password, PIN
2. Something you **have** – OTP device, smart card, phone
3. Something you **are** – fingerprint, face, iris

**Q. What is MFA / 2FA?**
Using **two or more different factors**. Ex: password + OTP.
Password + PIN is **not** MFA (both are "know" factors).

**Q. How are passwords stored securely?**
Not in plaintext. Stored as a **hash** with a **salt** (random value added to each password) so identical passwords give different hashes and rainbow-table attacks fail.

**Q. What is an OTP?**
One-Time Password – valid for one login/session only, so a stolen OTP is useless later.

**Q. Common attacks on passwords?**
Brute force, dictionary attack, guessing, shoulder surfing, phishing, keylogger.

---

## 3. Access Control

**Q. What is access control?**
Mechanism that **allows or denies** a user/process access to a resource based on permissions.

**Q. Main access control models?**
| Model | Who decides access | Example |
|---|---|---|
| **DAC** (Discretionary) | Owner of the resource | Linux file permissions (chmod) |
| **MAC** (Mandatory) | System/central authority using security labels | Military: Top Secret, Secret |
| **RBAC** (Role-Based) | User's role | Admin, Teacher, Student roles |

**Q. What is an access matrix?**
A table where **rows = users/domains**, **columns = objects (files)**, and each cell = rights (read, write, execute).

**Q. ACL vs Capability list?**
- **Access Control List (ACL):** stored per **object** (column of matrix) – "who can access this file".
- **Capability list:** stored per **user/domain** (row of matrix) – "what this user can access".

**Q. Principle of least privilege?**
Give a user/process only the **minimum permissions** needed for its job.

---

## 4. Program Threats

**Q. What is a program threat?**
A program (malicious or buggy) that misuses the system or other programs. Ex: virus, worm, Trojan, trap door, buffer overflow.

**Q. Virus?**
Malicious code that **attaches to a host file/program** and spreads when that file is run.
Needs a host + human action. Ex: infected .exe.

**Q. Worm?**
**Standalone** malware that **self-replicates and spreads over the network automatically** – no host file needed. Uses system resources heavily.
Ex: Morris Worm (1988), WannaCry.

**Q. Trojan horse?**
Malware **disguised as useful software** to trick the user into installing it. Does **not** self-replicate.
Ex: a fake game that steals passwords.

**Q. Virus vs Worm vs Trojan?**
| Feature | Virus | Worm | Trojan |
|---|---|---|---|
| Needs host file | Yes | No | No |
| Self-replicates | Yes | Yes | No |
| Spreads automatically | No (needs user) | Yes | No |
| Key idea | Infects files | Spreads over network | Disguise/deception |

**Q. Trap door (backdoor)?**
A **hidden entry point** in a program that **bypasses normal authentication**.
Ex: a programmer leaves a secret password that always works.
Can be left by developers (for testing) or installed by attackers.

> Note: In **cryptography (RSA)**, "trapdoor" means something different – a secret (private key) that makes a one-way function easy to reverse. Clarify which one if asked.

**Q. Logic bomb?** *(often asked with trap door)*
Malicious code that runs only when a **condition** is met (a date, an event). Ex: delete files if the employee's name is removed from payroll.

**Q. What is a stack?**
Memory area for function calls – stores local variables, parameters and the **return address**. Works LIFO.

**Q. Stack overflow?**
Stack runs **out of space**, usually from infinite/very deep **recursion** → program crashes.

**Q. Buffer overflow?**
Program writes **more data into a buffer than its size**, overwriting neighbouring memory.
Cause: no input-length check (e.g., `gets()`, `strcpy()` in C).

**Q. How do attackers exploit a buffer overflow? (simple steps)**
1. Send input longer than the buffer.
2. Extra data overwrites the **return address** on the stack.
3. Return address now points to attacker's code (shellcode).
4. When the function returns, attacker's code runs → system control.

**Q. Stack overflow vs Buffer overflow?**
- Stack overflow → the **whole stack** is full (recursion). Usually a crash.
- Buffer overflow → data crosses the **limit of one buffer**. Can be exploited to run code.

**Q. Prevention of buffer overflow?**
Bounds checking / input validation, safe functions (`fgets`, `strncpy`), stack canaries, ASLR, DEP/NX bit, memory-safe languages.

---

## 5. System Threats – Intruders

**Q. What is a system threat?**
Misuse of system services and network connections. Ex: intruders, worms, port scanning, DoS.

**Q. Who is an intruder?**
A person who tries to gain **unauthorized access** to a system (a hacker/cracker).

**Q. Three types of intruders?**
| Type | Who | Example |
|---|---|---|
| **Masquerader** | Outsider pretending to be a valid user | Uses stolen password |
| **Misfeasor** | Insider (legit user) misusing privileges | Employee reading salary files |
| **Clandestine user** | Gets admin/supervisor control and hides tracks | Deletes audit logs |

Easy memory: **Masquerader = outsider, Misfeasor = insider, Clandestine = either, hides.**

**Q. Intrusion techniques?**
Password guessing/cracking, exploiting software bugs, social engineering, phishing, port scanning.

**Q. What is port scanning?**
Probing a system's ports to find open services and weaknesses before attacking.

**Q. What is DoS / DDoS?**
Flooding a system so legitimate users can't use it (attack on availability). DDoS = from many machines (botnet).

**Q. IDS vs IPS?**
- **IDS (Intrusion Detection System):** detects and **alerts**.
- **IPS (Intrusion Prevention System):** detects and **blocks**.

**Q. Types of IDS?**
- **Signature-based:** matches known attack patterns (can't catch new attacks).
- **Anomaly-based:** flags behaviour that differs from normal (can catch new attacks, more false alarms).

**Q. Intrusion prevention measures?**
Strong passwords + MFA, least privilege, patching, firewalls, IDS/IPS, audit logs.

---

## 6. Communication Threats – Tapping and Piracy

**Q. Communication threat?**
Threat to data **while it is being transmitted** over a network.

**Q. What is tapping (wiretapping)?**
**Secretly intercepting/listening** to communication on a network or line.
- Passive tapping → only listening (attack on confidentiality).
- Active tapping → listening + altering/injecting messages (also attacks integrity).

**Q. How to prevent tapping?**
Encryption (HTTPS/TLS, SSH, VPN), secure Wi-Fi (WPA2/WPA3), avoid sending data in plaintext.

**Q. What is piracy?**
**Unauthorized copying, distribution or use** of software or digital content (movies, music) violating its license/copyright.

**Q. Types of software piracy?**
Softlifting (installing one license on many PCs), counterfeiting, internet piracy (cracked downloads), hard-disk loading (seller pre-installs unlicensed copies).

**Q. Prevention of piracy?**
License keys/activation, DRM, watermarking, legal action, user awareness.

**Q. Tapping vs Piracy?**
Tapping → stealing **information in transit**. Piracy → illegally **copying software/content**.

---

## Last-Minute Recap (read this before going in)

- Protection = mechanism; Security = overall defence.
- CIA: Confidentiality (read), Integrity (change), Availability (access) + Privacy (personal data use).
- Identification → Authentication (who you are) → Authorization (what you can do).
- Factors: know / have / are. MFA = 2+ **different** factors.
- DAC (owner), MAC (labels), RBAC (roles). ACL = per object, Capability = per user.
- Virus = needs host. Worm = spreads alone. Trojan = disguise. Trap door = secret bypass.
- Stack overflow = recursion fills stack. Buffer overflow = input exceeds buffer → overwrite return address.
- Intruders: Masquerader (outsider), Misfeasor (insider), Clandestine (hides).
- Tapping = intercepting communication (passive). Piracy = illegal copying.
