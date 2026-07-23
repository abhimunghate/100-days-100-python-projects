# This is Day 12 project : Temperature Converter

def celsius_to_fahrenheit(celsius):
    return (celsius * 9/5) + 32

def celsius_to_kelvin(celsius):
    return celsius + 273.15

def fahrenheit_to_celsius(fahrenheit):
    return (fahrenheit - 32) * 5/9

def fahrenheit_to_kelvin(fahrenheit):
    return (fahrenheit - 32) * 5/9 + 273.15

def kelvin_to_celsius(kelvin):
    return kelvin - 273.15

def kelvin_to_fahrenheit(kelvin):
    return (kelvin - 273.15) * 9/5 + 32

def show_menu():
    print("\n------ Temperature Converter Menu ------\n")
    print("1. Celsius to Fahrenheit & Kelvin")
    print("2. Fahrenheit to Celsius & Kelvin")
    print("3. Kelvin to Celsius & Fahrenheit")
    print("4. Automatic conversion to all units.")
    print("5. Batch conversion (multiple temperatures)")
    print("6. Exit")
    
while True:
    show_menu()
    choice = input("\nEnter your choice (1/2/3/4/5/6) : ")
    
    if choice == "6":
        print("\nExiting the program. Goodbye!")
        break
    
    elif choice not in ["1", "2", "3", "4", "5"]:
        print("Invalid choice. Please select a valid option.")
        continue
    
    try:
        decimal_places = int(input("Enter the number of decimal places : "))
        
        if decimal_places < 0:
            print("Decimal places cannot be negative.")
            continue
    except ValueError:
        print("Please enter a valid whole number.")
        continue
    
    if choice == "1":
        try:
            celsius = float(input("\nEnter temperature in Celsius : "))
            print(f"Fahrenheit : {celsius_to_fahrenheit(celsius):.{decimal_places}f}")
            print(f"Kelvin : {celsius_to_kelvin(celsius):.{decimal_places}f}")
        except ValueError:
            print("Please enter a valid numeric temperature.")
        
    elif choice == "2":
        try:
            fahrenheit = float(input("\nEnter temperature in Fahrenheit : "))
            print(f"Celsius : {fahrenheit_to_celsius(fahrenheit):.{decimal_places}f}")
            print(f"Kelvin : {fahrenheit_to_kelvin(fahrenheit):.{decimal_places}f}")
        except ValueError:
            print("Please enter a valid numeric temperature.")
        
    elif choice == "3":
        try:
            kelvin = float(input("\nEnter temperature in Kelvin : "))
            if kelvin < 0:
                print("Kelvin cannot be negative")
            else:
                print(f"Celsius : {kelvin_to_celsius(kelvin):.{decimal_places}f}")
                print(f"Fahrenheit : {kelvin_to_fahrenheit(kelvin):.{decimal_places}f}")
        except ValueError:
            print("Please enter a valid numeric temperature.")
            
    elif choice == "4":
        try:
            value = float(input("\nEnter temperature value : "))
            unit = input("Enter unit (C/F/K) : ").upper()

            if unit == "C":
                celsius = value

            elif unit == "F":
                celsius = fahrenheit_to_celsius(value)

            elif unit == "K":
                if value < 0:
                    print("Kelvin cannot be negative.")
                    continue

                celsius = kelvin_to_celsius(value)

            else:
                print("Invalid unit. Please enter C, F, or K.")
                continue

            fahrenheit = celsius_to_fahrenheit(celsius)
            kelvin = celsius_to_kelvin(celsius)

            print("\n------ Converted Temperatures ------\n")
            print(f"Celsius    : {celsius:.{decimal_places}f} °C")
            print(f"Fahrenheit : {fahrenheit:.{decimal_places}f} °F")
            print(f"Kelvin     : {kelvin:.{decimal_places}f} K")

        except ValueError:
            print("Please enter a valid numeric temperature.")
            
    elif choice == "5":
        try:
            raw_values = input("\nEnter temperatures separated by commas : ")
            unit = input("Enter unit for all values (C/F/K) : ").upper()

            if unit not in ["C", "F", "K"]:
                print("Invalid unit. Please enter C, F, or K.")
                continue

            print("\n------ Batch Conversion Results ------\n")

            for item in raw_values.split(","):
                item = item.strip()

                try:
                    value = float(item)

                    if unit == "C":
                        celsius = value

                    elif unit == "F":
                        celsius = fahrenheit_to_celsius(value)

                    elif unit == "K":
                        if value < 0:
                            print(f"{value} K -> Invalid (Kelvin cannot be negative)")
                            continue

                        celsius = kelvin_to_celsius(value)

                    fahrenheit = celsius_to_fahrenheit(celsius)
                    kelvin = celsius_to_kelvin(celsius)

                    print(f"Input: {value} {unit}")
                    print(f"  Celsius    : {celsius:.{decimal_places}f} °C")
                    print(f"  Fahrenheit : {fahrenheit:.{decimal_places}f} °F")
                    print(f"  Kelvin     : {kelvin:.{decimal_places}f} K")
                    print("-" * 40)

                except ValueError:
                    print(f"'{item}' is not a valid number.")
                    print("-" * 40)

        except Exception as e:
            print(f"Unexpected batch error: {e}")
            
# Done