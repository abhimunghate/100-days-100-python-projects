# This is Day 6 project : Basic Math Quiz Game

import random

def generate_question():
    num1 = random.randint(1, 10)
    num2 = random.randint(1, 10)
    operator = random.choice(['+', '-', '*', '/'])
    
    if operator == '+':
        answer = num1 + num2
    elif operator == '-':
        answer = num1 - num2
    elif operator == '/':
        answer = num1 / num2
    else:
        answer = num1 * num2
        
    return f"{num1} {operator} {num2}", answer

def math_quiz():
    score = 0
    rounds = int(input("Enter the number of questions you want to answer : "))
    
    print("\n------ Welcome to the Math Quiz Game! ------")
    print(f"\nYou will be asked {rounds} questions. Try to answer them correctly!")
    
    for i in range(rounds):
        question, correct_answer  = generate_question()
        print(f"\nQuestion {i+1} : {question}")
        user_answer = float(input("Your answer : "))
        if user_answer == correct_answer:
            print("Correct!")
            score += 1
        else:
            print(f"Wrong! The correct answer was {correct_answer}.")
               
    print("\n------ Game Over! ------")
    print(f"Your final score is {score}/{rounds}.")
    
    if score == rounds:
        print("Excellent! You got all answers correct!")
    elif score >= rounds // 2 + 1:
        print("Good job! You did well.")
    else:
        print("Keep practicing! Better luck next time!")
        
math_quiz()

# Done