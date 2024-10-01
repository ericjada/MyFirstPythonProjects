import json  # Import the json module to handle JSON file operations

# Define the filename where recipes will be stored
RECIPE_FILE = 'recipes.json'

def load_recipes():
    """Load recipes from the JSON file."""
    try:
        with open(RECIPE_FILE, 'r') as file:
            return json.load(file)  # Load and return recipes
    except FileNotFoundError:
        return []  # Return an empty list if the file doesn't exist
    except json.JSONDecodeError:
        return []  # Return an empty list if the file is corrupted

def save_recipes(recipes):
    """Save recipes to the JSON file."""
    with open(RECIPE_FILE, 'w') as file:
        json.dump(recipes, file, indent=4)  # Write recipes to the file

def add_recipe(name, ingredients, instructions):
    """Add a new recipe to the collection."""
    recipes = load_recipes()  # Load existing recipes
    recipe = {
        'name': name,
        'ingredients': ingredients,
        'instructions': instructions
    }
    recipes.append(recipe)  # Add new recipe to the list
    save_recipes(recipes)  # Save updated recipes

def view_recipes():
    """Display all recipes."""
    recipes = load_recipes()  # Load existing recipes
    if not recipes:
        print("No recipes found.")
    else:
        for index, recipe in enumerate(recipes):
            print(f"{index + 1}. {recipe['name']}")
            print("   Ingredients:", ", ".join(recipe['ingredients']))
            print("   Instructions:", recipe['instructions'])
            print()

def search_recipes(query):
    """Search for recipes by name or ingredient."""
    recipes = load_recipes()  # Load existing recipes
    found_recipes = [
        recipe for recipe in recipes if query.lower() in recipe['name'].lower() or
        any(query.lower() in ingredient.lower() for ingredient in recipe['ingredients'])
    ]
    
    if not found_recipes:
        print("No recipes found for your search.")
    else:
        for recipe in found_recipes:
            print(f"Name: {recipe['name']}")
            print("   Ingredients:", ", ".join(recipe['ingredients']))
            print("   Instructions:", recipe['instructions'])
            print()

def main():
    """Main function to run the Recipe App."""
    while True:
        print("Welcome to the Recipe App!")
        print("1. Add Recipe")
        print("2. View Recipes")
        print("3. Search Recipes")
        print("4. Exit")
        
        choice = input("Choose an option (1-4): ")
        
        if choice == '1':
            name = input("Enter recipe name: ")
            ingredients = input("Enter ingredients (comma-separated): ").split(',')
            instructions = input("Enter instructions: ")
            add_recipe(name, [ingredient.strip() for ingredient in ingredients], instructions)
            print("Recipe added!\n")
        
        elif choice == '2':
            view_recipes()  # Display all recipes
        
        elif choice == '3':
            query = input("Enter recipe name or ingredient to search: ")
            search_recipes(query)  # Search for recipes
        
        elif choice == '4':
            print("Goodbye!")
            break  # Exit the loop and end the program
        
        else:
            print("Invalid choice. Please try again.\n")

if __name__ == "__main__":
    main()  # Run the main function
