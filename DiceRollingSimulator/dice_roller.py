import random

def roll_dice(sides, num_rolls=1):
    """
    Rolls a dice with a specified number of sides.
    
    :param sides: Number of sides on the dice.
    :param num_rolls: Number of times to roll the dice.
    :return: A list of results for each roll.
    """
    return [random.randint(1, sides) for _ in range(num_rolls)]  # Roll the dice

def main():
    print("Welcome to the D&D Dice Rolling Simulator!")
    while True:
        user_input = input("Enter your roll (e.g., '2d20' to roll two 20-sided dice) or 'q' to quit: ")
        
        if user_input.lower() == 'q':
            print("Thanks for playing!")
            break
        
        try:
            # Parse user input for dice notation (e.g., 2d20)
            num_rolls, sides = map(int, user_input.split('d'))
            if num_rolls <= 0 or sides <= 0:
                raise ValueError("Both the number of dice and sides must be positive integers.")
            
            # Roll the dice
            rolls = roll_dice(sides, num_rolls)
            total = sum(rolls)  # Calculate the total of the rolls
            
            # Display results
            print(f"You rolled: {', '.join(map(str, rolls))} (Total: {total})")
        
        except ValueError as e:
            print(f"Invalid input: {e}. Please use the format 'NdM' (e.g., '2d20').")

if __name__ == "__main__":
    main()  # Run the main function
