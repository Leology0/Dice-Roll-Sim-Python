# Dice Roll Simulator
import random

def main():
    loop = True
    while loop:
        # Print Menu
        print("\nDice Roll Simulator Menu")
        print("1. Roll Dice Once")
        print("2. Roll Dice 5 Times")
        print("3. Roll Dice 'n' Times")
        print("4. Roll Dice until Snake Eyes")
        print("5. Exit")
        # Get Menu Selection
        selection = input("Select An Option (1-5): ")

        # Carry out input from menu
        # Roll Dice Once
        if selection == "1":
            roll2Dice()
        # Roll Dice 5 times
        elif selection == "2":
            n = 0
            for n in range(5):
                roll2Dice()
        # Roll Dice 'n' times
        elif selection == "3":
            i = 0
            n = int(input("Choose a value for 'n' "))
            for i in range(n):
                roll2Dice()
                i += 1
        # Roll Dice until Snake Eyes
        elif selection == "4":
            amount_Of_Rolls = 0
            roll = True
            while roll:
                amount_Of_Rolls += 1
                roll2Dice()
                if dice_total == 2:
                    print("SNAKE EYES! It took " + str(amount_Of_Rolls) + "rolls to get snake eyes.")
                    roll = False
        # Exit
        elif selection == "5":
            loop = False

          
# Roll Dice Function
def roll2Dice():
    dice1 = random.randrange(1, 7)
    dice2 = random.randrange(1, 7)
    global dice_total
    dice_total = dice1 + dice2
    print(str(dice1) + "," + str(dice2) + "(sum: " + str(dice_total) + ")")
    return dice_total


main()
