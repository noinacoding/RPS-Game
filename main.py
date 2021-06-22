# โมดูลที่ต้องใช้
import random
import time


# เล่นอีกรอบ


def replay():
    # ตัวเกมหลัก

    def rps():
        if answer == 1:
            return "Rock"
        elif answer == 2:
            return "Paper"
        elif answer == 3:
            return "Scissors"

    # เปลี่ยนตัวเลือกย่อยเป็นคำหลัก
    def rename():
        if choice == "R" or choice == "r" or choice == "Rock" or choice == "rock":
            return "Rock"
        if choice == "P" or choice == "p" or choice == "Paper" or choice == "paper":
            return "Paper"
        if choice == "S" or choice == "s" or choice == "Scissors" or choice == "scissors":
            return "Scissors"

    # กระบวนการของตัวเลือกค้อน
    def rock():
        if rps() == "Rock":
            print("Tie")
            print("Since it was tie you need to pick again")
            replay()
        elif rps() == "Paper":
            print("You lost")
        elif rps() == "Scissors":
            print("You won")

    # กระบวนการของตัวเลือกกระดาษ
    def paper():
        if rps() == "Paper":
            print("Tie")
            print("Since it was tie you need to pick again")
            replay()
        elif rps() == "Scissors":
            print("You lost")
        elif rps() == "Rock":
            print("You won")

    # กระบวนการของตัวเลือกกรรไกร
    def scissors():
        if rps() == "Scissors":
            print("Tie")
            print("Since it was tie you need to pick again")
            replay()
        elif rps() == "Rock":
            print("You lost")
        elif rps() == "Paper":
            print("You won")

    # ประมวลผลลัพธ์
    def result():
        if rename() == "Rock":
            rock()
        elif rename() == "Paper":
            paper()
        elif rename() == "Scissors":
            scissors()

    # รับข้อมูลตัวเลือกจากผู้เล่นและทำการประมวลผลลัพธ์
    choice = str(input("Please choose between Rock (R), Paper (P), Scissors (S) "))
    answer = random.randint(1, 3)
    rps()
    rename()

    if rename() == "Rock" or rename() == "Paper" or rename() == "Scissors":
        print("You have choose", rename())
        time.sleep(1)
        print("The bot is now picking their choice..")
        time.sleep(3)
        print("The bot have choose", rps())
        print("So the result is..")
        result()
        time.sleep(1.2)
        # เล่นอีกรอบ
        again = str(input("Would you like to play again? Yes (Y) or No (N) "))
        if again == "Yes" or again == "Y" or again == "y" or again == "yes":
            print("Creating a new game..")
            print("-------------------------------------------------")
            replay()
        elif again == "No" or again == "N" or again == "n" or again == "no":
            print("Ending process..")
        else:
            print("Invalid answer")
            time.sleep(1)
            print("Ending process..")
    else:
        print("Invalid choice")
        replay()


# เริ่มเกม

replay()
