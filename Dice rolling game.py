import random

while True:
    choice = input("Roll the dice? (y/n): ").lower()  # Correct spelling and lowercase conversion
    if choice == 'y':
        die1 = random.randint(1, 6)  # Simulates rolling a six-sided die
        die2 = random.randint(1, 6)
        print(f'{die1}, {die2}')  # Prints the result of rolling two dice
    elif choice == 'n':
        print("Thanks for playing")
        break  # Added break to exit the loop when user chooses 'n'
    else:
        print("Invalid choice")  # Corrected spelling from "chice" to "choice"
