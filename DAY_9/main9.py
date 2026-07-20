# This is Day 9 project : Ingredient Checker

recipe_ingredients = {"flour", "sugar", "butter", "eggs", "milk"}

substitutes = {
    "milk": {"almond milk", "soy milk", "oat milk"},
    "butter": {"margarine", "coconut oil"},
    "eggs": {"banana", "flaxseed"}
}

recipes = {
    "Pancakes": {"flour", "milk", "eggs", "butter"},
    "Cookies": {"flour", "sugar", "butter"},
    "Omelette": {"eggs", "milk", "butter"},
    "French Toast": {"bread", "eggs", "milk"},
    "Cake": {"flour", "sugar", "eggs", "butter", "milk"}
}

user_input = input("Enter the ingredients you have (separated by commas) : ")
user_ingredients = set(item.strip().lower() for item in user_input.split(","))

effective_ingredients = user_ingredients.copy()

missing_ingredients = recipe_ingredients - user_ingredients
extra_ingredients = user_ingredients - recipe_ingredients

print("\n------ Ingredient Check Results ------\n")

for ingredient in list(missing_ingredients):
    if ingredient in substitutes:
        common = substitutes[ingredient].intersection(user_ingredients)

        if common:
            substitute_used = common.pop()
            print(f"Using '{substitute_used}' as a substitute for '{ingredient}'.")
            effective_ingredients.add(ingredient)
            missing_ingredients.remove(ingredient)
        else:
            print(f"No substitute available for '{ingredient}'.")
          
if missing_ingredients:
    print(f"You are still missing the following ingredients : {', '.join(missing_ingredients)}")
else:
    print("You have all the ingredients needed for the main recipe!")
    
if extra_ingredients:
    print(f"You also have extra ingredients : {', '.join(extra_ingredients)}")

print("\n------ Recipe Suggestions ------")

possible_recipes = []
almost_recipes = []

for recipe_name, required in recipes.items():
    if required.issubset(effective_ingredients):
        possible_recipes.append(recipe_name)
    else:
        missing = required - effective_ingredients

        if len(missing) == 1:
            almost_recipes.append((recipe_name, missing))

if possible_recipes:
    print("Recipes you can make:")
    for recipe in possible_recipes:
        print(f"- {recipe}")
else:
    print("No recipe can be made completely with the available ingredients.")

if almost_recipes:
    print("\nRecipes you are very close to making:")
    for recipe_name, missing in almost_recipes:
        print(f"- {recipe_name} (missing: {', '.join(missing)})")  
        
# Done