# This is Day 14 project : Random Password Generator

import random, string, time

FILENAME = "saved_passwords.txt"

def save_password(password):
    timestamp = time.strftime("%d/%m/%Y %H:%M:%S")

    with open(FILENAME, "a") as file:
        file.write(f"[{timestamp}] Password: {password}\n")

    print("Password saved successfully!")
    
def get_choice(message):
    while True:
        choice = input(message).upper()

        if choice in ["Y", "N"]:
            return choice

        print("\nPlease enter only Y or N.")

def generate_password(length, uppercase, lowercase, digits, special_chars):
    password = []
    
    all_chars = ""
    
    if uppercase == "Y":
        all_chars += string.ascii_uppercase
        password.append(random.choice(string.ascii_uppercase))
        
    if lowercase == "Y":
        all_chars += string.ascii_lowercase
        password.append(random.choice(string.ascii_lowercase))
        
    if digits == "Y":
        all_chars += string.digits
        password.append(random.choice(string.digits))
        
    if special_chars == "Y":
        all_chars += string.punctuation
        password.append(random.choice(string.punctuation))
        
    if all_chars == "":
        raise ValueError("You must select at least one character type.")
    
    if length < len(password):
        raise ValueError(f"Password length must be at least {len(password)}")
    
    password += random.choices(all_chars, k = length - len(password))
    
    random.shuffle(password)
    
    return ''.join(password)


try:
    length = int(input("Enter the desired password length : "))
    
    if length <= 0:
        raise ValueError("Password length must be greater than 0.")
    
    count = int(input("How many passwords do you want to generate? : "))
    
    uppercase = get_choice("\nInclude uppercase letters? (Y/N): ")
    lowercase = get_choice("Include lowercase letters? (Y/N): ")
    digits = get_choice("Include digits? (Y/N): ")
    special_chars = get_choice("Include special characters? (Y/N): ")
    
    if count <= 0:
        raise ValueError("\nNumber of passwords must be at least 1.")
    else:
        print("\nGenerated Passwords:\n")
        for i in range(count):
            password = generate_password(length, uppercase, lowercase, digits, special_chars)
            print("-" * 40)
            print(f"\nPassword {i + 1} : {password}")
            
            choice = get_choice("\nDo you want to save this password? (Y/N): ")
            if choice == "Y":
                save_password(password)
            else:
                print("Password not saved.")

except ValueError as e:
    print(e)
    
# Done