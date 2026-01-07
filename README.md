# Safety-Critical Code Compliance Auditor (SAST)

### Project Overview
As an Aeronautical Engineer, I understand that software in aviation must adhere to strict airworthiness standards (like **DO-178C**). This tool is a **Static Application Security Testing (SAST)** script that automates the detection of insecure coding practices in flight software.

### Security+ Concepts Applied
* **Secure Coding Practices:** Enforcing input validation and memory management.
* **Risk Mitigation:** Reducing the attack surface by eliminating functions prone to Buffer Overflows (`strcpy`) and Memory Leaks (`malloc`).
* **Automation:** Implementing "Compliance as Code" to reduce human error during code reviews.

### How it Works
The script scans C/C++ source files for signatures of banned functions commonly prohibited in **MISRA C** and **embedded safety standards**. It flags these violations so developers can remediate them before compilation.

### Example Detection
* **Violation:** `strcpy(dest, src)`
* **Security Risk:** Does not check buffer length, leading to potential stack smashing attacks.
* **Remediation:** Enforce usage of `strncpy` or `strlcpy`.

### Usage
1. Place `.c` files in the directory.
2. Run `python auditor.py`.
