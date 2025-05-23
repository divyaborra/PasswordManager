import secrets  
import string   
import math    

def generate_password(length=12):
    characters = string.ascii_letters + string.digits + string.punctuation
    pwd = ''.join(secrets.choice(characters) for _ in range(length))
    return pwd

def calculate_security(password):
    char_pool = 0
    if any(c.islower() for c in password):
        char_pool += 26  # Lowercase letters
    if any(c.isupper() for c in password):
        char_pool += 26  # Uppercase letters
    if any(c.isdigit() for c in password):
        char_pool += 10  # Digits
    if any(c in string.punctuation for c in password):
        char_pool += len(string.punctuation)  # Special characters
    
    security = math.log2(char_pool ** len(password))
    return security

if __name__ == "__main__":
    print("===== Secure Password Generator =====")
    
    while True:
        length = int(input("Enter desired password length: "))
        
        pwd = generate_password(length)
        sec = calculate_security(pwd)

        print(f"\nGenerated Password: {pwd}")
        print(f"Password Entropy: {sec:.2f} bits")

        if sec < 50:
            print("Weak password! Consider using more characters.")
        elif sec < 80:
            print("Moderate password. Could be stronger.")
        else:
            print("Strong password! Very secure.")
        
        user_choice = input("Are you happy with this password? (yes/no): ").strip().lower()
        if user_choice == 'yes':
            print("Password finalized.")
            break
        else:
            print("Generating a new password...\n")
