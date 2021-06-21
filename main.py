import random
import time


def replay():
    # Main Game Section 1
    def rps():
        if answer == 1:
            return "Rock"
        elif answer == 2:
            return "Paper"
        elif answer == 3:
            return "Scissors"

    # Player choice, Bot choice
    choice = str(input("Please choose between Rock (R), Paper (P), Scissors (S) "))
    answer = random.randint(1, 3)
    rps()

    # Main Game Section 2
    def rename():
        if choice == "R" or choice == "r" or choice == "Rock":
            return "Rock"
        if choice == "P" or choice == "p" or choice == "Paper":
            return "Paper"
        if choice == "S" or choice == "s" or choice == "Scissors":
            return "Scissors"

    # Rename player choice
    rename()

    def rock():
        if rps() == "Rock":
            print("Tie")
        elif rps() == "Paper":
            print("You lost")
        elif rps() == "Scissors":
            print("You won")

    def paper():
        if rps() == "Paper":
            print("Tie")
        elif rps() == "Scissors":
            print("You lost")
        elif rps() == "Rock":
            print("You won")

    def scissors():
        if rps() == "Scissors":
            print("Tie")
        elif rps() == "Rock":
            print("You lost")
        elif rps() == "Paper":
            print("You won")

    # Compile Results
    def result():
        if rename() == "Rock":
            rock()
        elif rename() == "Paper":
            paper()
        elif rename() == "Scissors":
            scissors()

    if rename() == "Rock" or rename() == "Paper" or rename() == "Scissors":
        print("You have choose", rename())
        time.sleep(1)
        print("The bot is now picking their choice..")
        time.sleep(3)
        print("The bot have choose", rps())
        print("So the result is..")
        result()
        time.sleep(1.2)
        again = str(input("Would you like to play again? Yes (Y) or No (N) "))
        if again == "Yes" or again == "Y" or again == "y":
            again = "Finish"
            print("Creating a new game..")
            print("-------------------------------------------------")
            replay()
        elif again == "No" or again == "N" or again == "n":
            print("Ending process..")
        else:
            print("Invalid answer")
            time.sleep(1)
            print("Ending process")
    else:
        print("Invalid choice")


replay()
