# This is Day 2 project : Personalized Greeting Program

from datetime import datetime
current_year = datetime.now().year
name = input("What is your name? : ").upper()
birth_year = int(input("What is your birth year? : "))
current_age = current_year - birth_year
age_in_months = current_age * 12
age_in_weeks = current_age * 52
age_in_days = current_age * 365
age = int(input("How old are you? : "))
color = input("What is your favorite color? : ")

print("\n------ Personalized Greeting ------\n")
print(f"Hello {name}!🙂")
print(f"You were born in {birth_year}, so you are {current_age} years old.")
print(f"""You are {age_in_months} months old.
      You are {age_in_weeks} weeks old.
      You are {age_in_days} days old.""")
print(f"You are {age} years old and {color} is a beautiful color! 🌈")
print("You're ready to start your Python journey! 🚀")

# Done