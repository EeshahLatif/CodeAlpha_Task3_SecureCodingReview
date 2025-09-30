# Secure Coding Review - Task 3

## Problems in the Original Code
1. **SQL Injection** – attacker can type `' OR '1'='1` and bypass login.  
2. **Command Injection** – attacker can run dangerous commands via `os.system()`.  
3. **Plaintext Passwords** – stored without hashing, unsafe if database is stolen.  
4. **Hardcoded Credentials** – insecure practice.

## Fixes in Secure Version
1. Used **parameterized SQL queries**.  
2. Removed `os.system()` and avoided unsafe commands.  
3. Stored **hashed passwords** using bcrypt.  
4. No hardcoded passwords in real apps.

✅ Now the code follows **secure coding best practices**.
