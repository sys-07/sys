# Information Security – Unit I Viva Questions with Answers

**MCA – Information Security Practical Examination**

**Unit I: Overview of Security and Security Threats and Models**

This viva sheet follows the Unit I syllabus topics:

- Protection versus security
- Confidentiality, data integrity, availability and privacy
- User authentication and access controls
- Program threats: worms, viruses, Trojan horses, trap doors, stack overflow and buffer overflow
- System threats: intruders
- Communication threats: tapping and piracy

Answers are concise, technically accurate, and organized for practical-exam revision.

---

# Category 1: Overview of Security

**Q1. What is information security?**

Information security is the protection of information and information systems against unauthorized access, use, disclosure, modification, disruption or destruction.

**Q2. What is the difference between protection and security?**

- **Protection** refers to the mechanisms and controls used to regulate access to system resources.
- **Security** is the broader goal of protecting a system and its information against threats and attacks. It includes protection mechanisms as well as policies, procedures and other safeguards.

**Q3. What are the main aspects of information security in this unit?**

- Confidentiality
- Data integrity
- Availability
- Privacy

**Q4. What is confidentiality?**

Confidentiality ensures that information is accessible only to authorized users or entities.

**Example:** Encrypting a confidential file so unauthorized people cannot read it.

**Q5. What is data integrity?**

Data integrity ensures that information remains accurate, complete and unaltered except through authorized actions.

**Example:** Detecting whether someone has modified a stored file without permission.

**Q6. What is availability?**

Availability ensures that information and services are accessible to authorized users when they are needed.

**Example:** Keeping a web server operational and accessible to legitimate users.

**Q7. What is privacy?**

Privacy concerns the proper collection, use, storage and sharing of personal information, according to applicable rules, permissions and expectations.

**Q8. What is the difference between confidentiality and privacy?**

- Confidentiality controls who can access information.
- Privacy concerns how personal information is collected, used, stored and shared.

Confidentiality is one important part of protecting privacy, but the two terms are not identical.

**Q9. What is the CIA triad?**

The CIA triad is a basic information-security model consisting of:

- **Confidentiality:** Prevent unauthorized disclosure.
- **Integrity:** Prevent unauthorized or improper modification.
- **Availability:** Ensure authorized access when required.

**Q10. Give one example of a security failure for each CIA principle.**

- Confidentiality failure: An attacker reads private user records.
- Integrity failure: An attacker changes a bank account balance.
- Availability failure: A denial-of-service attack makes a website unavailable.

---

# Category 2: User Authentication and Access Controls

**Q1. What is user authentication?**

Authentication is the process of verifying the identity of a user, device or other entity.

**Q2. What is authorization?**

Authorization determines what an authenticated user or entity is permitted to access or do.

**Q3. What is the difference between authentication and authorization?**

| Authentication | Authorization |
|---|---|
| Verifies identity | Determines permissions |
| Answers: "Who are you?" | Answers: "What are you allowed to do?" |
| Usually occurs before access is granted | Uses identity and policy to decide access |

**Q4. What is access control?**

Access control is the process of restricting access to resources so that users can perform only the actions they are permitted to perform.

**Q5. What are the main factors used for authentication?**

1. **Something you know:** Password or PIN.
2. **Something you have:** Smart card, security token or registered device.
3. **Something you are:** Biometric characteristic, such as a fingerprint.

**Q6. What is multi-factor authentication (MFA)?**

MFA requires two or more different authentication factors to verify a user's identity.

**Example:** A password plus a one-time code from an authenticator app.

**Q7. Is using a password and a PIN always MFA?**

Not necessarily. Both are generally knowledge factors. MFA requires different types of factors.

**Q8. What is a password-based authentication system?**

It is a system in which a user proves identity by providing a password associated with their account.

**Q9. What is the principle of least privilege?**

A user or process should receive only the minimum permissions necessary to perform its required tasks.

**Q10. What is the difference between identification and authentication?**

- Identification is claiming an identity, such as entering a username.
- Authentication is proving that the claimed identity is genuine, such as entering the correct password.

---

# Category 3: Program Threats

**Q1. What is a program threat?**

A program threat is malicious or unintended code that can misuse a program's privileges, damage data, disrupt operation or compromise system security.

**Q2. What is a computer virus?**

A virus is malicious code that attaches itself to a host file or program and replicates when the infected host is executed or otherwise activated.

**Q3. What is a computer worm?**

A worm is standalone malicious software that can self-replicate and spread between systems, often over a network, without needing to attach itself to a host program.

**Q4. What is a Trojan horse?**

A Trojan horse is malicious software that disguises itself as legitimate or useful software to trick a user into executing it.

**Q5. Does a Trojan horse replicate itself?**

Not by definition. Its defining feature is deception or disguise. It may deliver other malware, but self-replication is not required.

**Q6. What is a trap door or backdoor?**

A trap door, also called a backdoor, is a hidden method of bypassing normal authentication or security controls to gain access to a system or program.

**Q7. Why is a trap door dangerous?**

It can allow unauthorized access while bypassing the normal security mechanisms.

**Q8. What is the difference between a virus, worm and Trojan horse?**

| Threat | Main characteristic |
|---|---|
| Virus | Attaches to a host file or program and replicates through it |
| Worm | Standalone malware that self-replicates and spreads |
| Trojan horse | Disguises itself as legitimate software to deceive users |

**Q9. What is a stack?**

A stack is a memory region used to manage function calls, local variables and return information. It typically follows last-in, first-out (LIFO) behavior.

**Q10. What is stack overflow?**

A stack overflow occurs when stack usage exceeds the available stack space. It can happen because of excessively deep or infinite recursion, or because too much stack memory is used.

**Q11. What is a buffer?**

A buffer is a temporary memory area used to hold data while it is being transferred or processed.

**Q12. What is a buffer overflow?**

A buffer overflow occurs when a program writes more data into a buffer than the buffer can hold, potentially overwriting adjacent memory.

**Q13. What can a buffer overflow cause?**

It can cause program crashes, data corruption, unexpected behavior or, in some cases, allow an attacker to execute code or gain control.

**Q14. What is the difference between stack overflow and buffer overflow?**

- Stack overflow means the stack has exceeded its available capacity.
- Buffer overflow means data has exceeded the boundaries of a buffer.

A buffer overflow can occur in stack memory, but the two terms do not mean the same thing.

**Q15. How can buffer overflows be prevented?**

- Validate input lengths.
- Use memory-safe programming languages where practical.
- Use bounds-checked functions and safe libraries.
- Enable protections such as stack canaries, address-space layout randomization (ASLR) and data execution prevention (DEP/NX).

---

# Category 4: System Threats – Intruders

**Q1. What is a system threat?**

A system threat targets the operation, resources or security of a computer system. It may compromise system availability, integrity or confidentiality.

**Q2. Who is an intruder?**

An intruder is a person or entity that attempts to gain unauthorized access to a computer system or its resources.

**Q3. What are common categories of intruders?**

A commonly used classification is:

- **Masquerader:** An outsider who gains access by pretending to be an authorized user.
- **Misfeasor:** A legitimate user who misuses their authorized privileges.
- **Clandestine user:** Someone who gains supervisory control and hides their activity or bypasses auditing and access controls.

**Q4. What is a masquerader?**

A masquerader is an unauthorized person who impersonates a legitimate user, often by using stolen credentials.

**Q5. What is a misfeasor?**

A misfeasor is a legitimate user who misuses their access privileges.

**Q6. What is a clandestine user?**

A clandestine user obtains supervisory control and attempts to hide their actions or avoid security monitoring.

**Q7. What is the difference between an insider and an outsider threat?**

- An insider threat comes from someone with legitimate access who misuses it, intentionally or unintentionally.
- An outsider threat comes from someone outside the organization or system's authorized user group.

**Q8. How can intrusions be prevented or detected?**

- Strong authentication and MFA.
- Least-privilege access controls.
- Regular software updates and patching.
- System logs and security monitoring.
- Intrusion detection and prevention systems.
- Regular review of user accounts and permissions.

**Q9. What is an Intrusion Detection System (IDS)?**

An IDS monitors system or network activity for suspicious behavior and generates alerts when potential intrusions are detected.

**Q10. What is an Intrusion Prevention System (IPS)?**

An IPS monitors activity and can take action to block or prevent detected malicious activity.

---

# Category 5: Communication Threats – Tapping and Piracy

**Q1. What is a communication threat?**

A communication threat targets information while it is being transmitted or communicated between systems or users.

**Q2. What is tapping?**

Tapping is the unauthorized interception or monitoring of communication to obtain information being transmitted.

**Q3. Give an example of tapping.**

An attacker secretly intercepts unencrypted network traffic to read usernames, messages or other transmitted information.

**Q4. Is tapping a passive or active attack?**

Tapping is generally a passive attack because the attacker observes or intercepts communication without necessarily changing it.

**Q5. What is piracy in information security?**

In this syllabus context, piracy refers to unauthorized copying, distribution or use of software or digital content.

**Q6. What is software piracy?**

Software piracy is the unauthorized copying, installation, distribution or use of software in violation of its license or applicable law.

**Q7. What is the difference between tapping and piracy?**

- Tapping involves unauthorized interception or monitoring of communication.
- Piracy involves unauthorized copying, distribution or use of software or digital content.

**Q8. How can tapping be prevented?**

- Use encrypted communication protocols such as HTTPS and SSH.
- Use secure Wi-Fi configurations.
- Use a VPN when appropriate on untrusted networks.
- Avoid transmitting sensitive information over unencrypted channels.

**Q9. How can software piracy be reduced?**

- Use genuine, properly licensed software.
- Apply license management and software audits.
- Use access controls and software activation mechanisms where appropriate.
- Educate users about legal and security risks.

---

# Category 6: Important Comparisons for Quick Revision

## 1. Confidentiality, Integrity, Availability and Privacy

| Aspect | Main concern |
|---|---|
| Confidentiality | Prevent unauthorized disclosure |
| Integrity | Prevent unauthorized or improper modification |
| Availability | Ensure access when needed |
| Privacy | Ensure personal information is handled appropriately |

## 2. Authentication, Authorization and Access Control

| Term | Meaning |
|---|---|
| Identification | Claiming an identity |
| Authentication | Verifying the claimed identity |
| Authorization | Deciding what the identity may do |
| Access control | Enforcing permitted and denied access |

## 3. Virus, Worm and Trojan Horse

| Feature | Virus | Worm | Trojan Horse |
|---|---|---|---|
| Attaches to host program | Yes | No | Not required |
| Self-replicates | Yes | Yes | Not by definition |
| Spreads automatically over networks | Not necessarily | Often | Not by definition |
| Uses disguise to trick users | Not its defining feature | Not its defining feature | Yes |

## 4. Stack Overflow vs Buffer Overflow

| Stack Overflow | Buffer Overflow |
|---|---|
| Stack exceeds its available capacity | Data exceeds a buffer's capacity |
| Often caused by deep recursion or excessive stack use | Often caused by missing bounds checks |
| Can crash a program | Can corrupt memory or crash a program |
| Specifically concerns stack capacity | Can occur in different memory regions |

## 5. IDS vs IPS

| IDS | IPS |
|---|---|
| Detects suspicious activity | Detects and can block suspicious activity |
| Primarily alerts | Can take preventive action |
| Usually monitors traffic or events | Often placed inline or integrated to enforce blocking |

---

# Category 7: Top 20 Questions to Prepare First

If you have limited revision time, prepare these questions first:

1. What is information security?
2. What is the difference between protection and security?
3. Explain confidentiality, integrity, availability and privacy.
4. What is the difference between confidentiality and privacy?
5. What is the CIA triad?
6. What is user authentication?
7. What is the difference between authentication and authorization?
8. What is access control?
9. What is multi-factor authentication?
10. What is the principle of least privilege?
11. What is a virus?
12. What is a worm?
13. What is a Trojan horse?
14. What is a trap door or backdoor?
15. What is the difference between stack overflow and buffer overflow?
16. What is an intruder? Explain masquerader, misfeasor and clandestine user.
17. What is tapping?
18. What is piracy in information security?
19. What is the difference between IDS and IPS?
20. How can communication threats and intrusions be prevented?

---

## Final Revision Tips

1. Learn the four security aspects: confidentiality, integrity, availability and privacy.
2. Clearly distinguish identification, authentication, authorization and access control.
3. Remember the differences between virus, worm and Trojan horse.
4. Understand that stack overflow and buffer overflow are related but different concepts.
5. Learn the three intruder categories: masquerader, misfeasor and clandestine user.
6. Remember that tapping is generally a passive communication attack.
7. Be able to give one real-world example for each threat.

**Practical viva tip:** Examiners may ask you to distinguish similar terms. Pay particular attention to confidentiality vs privacy, authentication vs authorization, virus vs worm vs Trojan horse, and stack overflow vs buffer overflow.
