# This is Day 4 project : Number Comparison tool

print("------ Welcome to Number Comparison Tool ------")

while True:
    print("1. Compare 2 numbers")
    print("2. Compare 3 numbers")
    print("3. Exit")
    
    compare_input = input("\nChoose an option to compare? (1-3) : ")
    if compare_input == "1":
        print("\n------ Comparison of 2 numbers ------")
        num1 = float(input("\nEnter first number: "))
        num2 = float(input("Enter second number: "))

        print("\n------ Comparison Results ------\n")
        if num1 == num2:
            print(f"Both numbers are equal. They are {num1}.")
        elif num1 > num2 :
            print(f"{num1} is greater than {num2}.")
        else:
            print(f"{num2} is greater than {num1}.")
        
        print("\n------ Number Type Check ------")
        if num1 > 0:
            print("\nFirst number is positive.")
        elif num1 < 0:
            print("\nFirst number is negative.")
        else:
            print("\nFirst number is zero.")
           
            
        if num2 > 0:
            print("Second number is positive.")
        elif num2 < 0:
            print("Second number is negative.")
        else:
            print("Second number is zero.")
           
     
    elif compare_input == "2":
        print("\n------ Comparison of 3 numbers ------")
        num1 = float(input("\nEnter first number: "))
        num2 = float(input("Enter second number: "))
        num3 = float(input("Enter third number: "))
        
        print("\n------ Comparison Results ------\n")
        if num1 == num2 and num2 == num3:
            print(f"All three numbers are equal. They are {num1}")
        elif num1 == num2 and num1 > num3:
            print("Num1 and Num2 are equal and are greater than Num3")
            print(f"The largest number is {num1}")
            print(f"The smallest number is {num3}")
        elif num1 == num2 and num1 < num3:
            print("Num1 and Num2 are equal and are lesser than Num3")
            print(f"The largest number is {num3}")
            print(f"The smallest number is {num1}")
        elif num2 == num3 and num2 > num1:
            print("Num2 and Num3 are equal and are greater than Num1")
            print(f"The largest number is {num2}")
            print(f"The smallest number is {num1}")
        elif num2 == num3 and num2 < num1:
            print("Num2 and Num3 are equal and are lesser than Num1")
            print(f"The largest number is {num1}")
            print(f"The smallest number is {num2}")
        elif num1 == num3 and num1 > num2:
            print("Num1 and Num3 are equal and are greater than Num2")
            print(f"The largest number is {num1}")
            print(f"The smallest number is {num2}")
        elif num1 == num3 and num1 < num2:
            print("Num1 and Num3 are equal and are lesser than Num2")
            print(f"The largest number is {num2}")
            print(f"The smallest number is {num1}")
        elif num2 > num1 and num1 > num3:
            print("Num2 is greater than Num1 and Num3.")
            print(f"The largest number is {num2}")
            print(f"The smallest number is {num3}")
        elif num3 > num1 and num1 > num2:
            print("Num3 is greater than Num1 and Num2.")
            print(f"The largest number is {num3}")
            print(f"The smallest number is {num2}")
        elif num1 > num2 and num2 > num3:
            print("Num1 is greater than Num2 and Num3.")
            print(f"The largest number is {num1}")
            print(f"The smallest number is {num3}")
        elif num3 > num2 and num2 > num1:
            print("Num3 is greater than Num2 and Num1.")
            print(f"The largest number is {num3}")
            print(f"The smallest number is {num1}")
        elif num1 > num3 and num3 > num2:
            print("Num1 is greater than Num3 and Num2.")
            print(f"The largest number is {num1}")
            print(f"The smallest number is {num2}")
        elif num2 > num3 and num3 > num1:
            print("Num2 is greater than Num3 and Num1.")
            print(f"The largest number is {num2}")
            print(f"The smallest number is {num1}")
        

        print("\n------ Number Type Check ------")
        if num1 > 0:
            print("\nFirst number is positive.")
        elif num1 < 0:
            print("\nFirst number is negative.")
        else:
            print("\nFirst number is zero.")
            
        if num2 > 0:
            print("Second number is positive.")
        elif num2 < 0:
            print("Second number is negative.")
        else:
            print("Second number is zero.")
            
        if num3 > 0:
            print("Third number is positive.")
        elif num3 < 0:
            print("Third number is negative.")
        else:
            print("Third number is zero.")
            
            
    elif compare_input == "3":
        print("\nExiting the program. Goodbye!") 
        break   
    
    else:
        print("\nInvalid Choice! Please choose 1, 2 or 3")
        continue
        
    continue_input = input("\nDo you want to compare more numbers? Enter \"Yes\" or \"No\" : ").lower()
    if continue_input == 'yes':
        continue
    else:
        print("\nThankyou for using the Number Comparison Tool.")
        break
    
# Done