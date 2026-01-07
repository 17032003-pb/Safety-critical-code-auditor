import os
import re

# --- CONFIGURATION: The "Rules of Engagement" ---
# Mapping banned functions to the reason why they are banned (Risk Management)
BANNED_FUNCTIONS = {
    "strcpy": "Buffer Overflow Risk (Use strncpy instead)",
    "strcat": "Buffer Overflow Risk (Use strncat instead)",
    "malloc": "Dynamic Memory Violation (Non-deterministic behavior)",
    "free":   "Dynamic Memory Violation (Memory leak risk)",
    "system": "Command Injection Risk (Arbitrary code execution)",
    "gets":   "Severe Buffer Overflow Risk (Deprecated and dangerous)"
}

def scan_file(filepath):
    """
    Reads a file line-by-line and checks for banned signatures.
    """
    violations_found = 0
    print(f"[*] Scanning file: {filepath}...")
    
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            lines = f.readlines()
            
        for line_num, line in enumerate(lines, 1):
            for func, reason in BANNED_FUNCTIONS.items():
                if re.search(rf"\b{func}\(", line):
                    print(f"    [!] CRITICAL VIOLATION at Line {line_num}: Found '{func}'")
                    print(f"        -> Risk: {reason}")
                    violations_found += 1
                    
    except Exception as e:
        print(f"Error reading file: {e}")

    return violations_found

def main():
    current_dir = os.getcwd()
    total_issues = 0
    
    print("--- AERONAUTICAL COMPLIANCE AUDITOR (SAST) ---\n")
    
    files_found = [f for f in os.listdir(current_dir) if f.endswith(('.c', '.cpp', '.h'))]
    
    if not files_found:
        print("No source code files found to scan.")
        return

    for filename in files_found:
        total_issues += scan_file(filename)
        
    print("\n--- AUDIT COMPLETE ---")
    if total_issues == 0:
        print("RESULT: PASSED (No violations found).")
    else:
        print(f"RESULT: FAILED ({total_issues} critical violations detected).")

if __name__ == "__main__":
    main()