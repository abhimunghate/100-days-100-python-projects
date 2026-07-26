# This is Day 15 project : Recipe Viewer App

def load_recipes(file_path):
    try:
        with open(file_path, 'r') as file:
            content = file.read().strip()
            
            if not content:
                return {}
            
            recipes = content.split("\n\n")
            recipe_dict = {}
            for recipe in recipes:
                lines = recipe.split("\n")
                if len(lines) >= 3:
                    name = lines[0].strip()
                    ingredients = lines[1].replace('Ingredients : ', '').strip()
                    instructions = lines[2].replace('Instructions : ', '').strip()
                    recipe_dict[name] = {"Ingredients" : ingredients, "Instructions" : instructions}
            return recipe_dict
    except FileNotFoundError:
        print("File not found.")
        return {}
    
def show_menu():
    print("\n------ Recipe Viewer Menu ------\n")
    print("1. View Recipe by Name.")
    print("2. View Recipe by Ingredients.")
    print("3. Add New Recipe.")
    print("4. List All Recipes.")
    print("5. Exit.")
    
def view_recipe(recipes):
    name = input("Enter the name of the recipe : ").strip().title()
    if name in recipes:
        print(f"\n------ Recipe {name} Details ------\n")
        print(f"Ingredients : {recipes[name] ['Ingredients']}")
        print(f"Instructions : {recipes[name] ['Instructions']}")
    else:
        print("Recipe not found.")
        
def view_recipe_ingredients(recipes):
    ingredient = input("Enter the name of the ingredients : ").strip().lower()
    
    found = False
    
    print(f"\n------ Recipes containing {ingredient} ------\n")
    for name, details in recipes.items():
        ingredients = details["Ingredients"].lower()
        
        if ingredient in ingredients:
            print(f"Recipe : {name}")
            print(f"Ingredients : {details['Ingredients']}")
            print(f"Instructions : {details['Instructions']}\n")
            print("-" * 40)
            found = True
            
    if not found:
        print("No recipes found with that ingredient.")
        
def add_recipe(recipes):
    name = input("\nEnter the recipe name : ").strip().title()
    
    if not name:
        print("Recipe name cannot be empty.")
        return
    
    if name in recipes:
        print("Recipe already exists.")
        return
    else:
        ingredients = input(f"Enter the ingredients to add for {name} (comma separated) : ").strip()
        
        if not ingredients:
            print("Ingredients cannot be empty.")
            return
        
        instructions = input(f"Enter the instructions for the recipe {name} : ").strip()
        
        if not instructions:
            print("Instructions cannot be empty.")
            return
        
        with open(recipe_file, 'a') as file:
            file.write(f"\n\n{name}")
            file.write(f"\nIngredients : {ingredients}")
            file.write(f"\nInstructions : {instructions}")
            
        recipes[name] = {"Ingredients" : ingredients, "Instructions" : instructions}
        
        print(f"\n{name} added successfully!")

recipe_file = "recipes.txt"
recipes = load_recipes(recipe_file)

while True:
    show_menu()
    
    choice = input("\nEnter your choice (1/2/3/4/5) : ")
    
    if choice == "1":
        view_recipe(recipes)
        
    elif choice == "2":
        view_recipe_ingredients(recipes)
        
    elif choice == "3":
        add_recipe(recipes)
    
    elif choice == "4":
        print("\n------ All Recipes ------\n")
        for index, name in enumerate(recipes):
            print(f"{index + 1}. {name}")
        
    elif choice == "5":
        print("\nExiting the program.")
        break
    
    else:
        print("\nInvalid choice. Please try again.")
        
# Done