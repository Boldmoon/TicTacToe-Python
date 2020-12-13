import time
import random
from os import system, name


def clear():
    if name == 'nt':
        _ = system('cls')
    else:
        _ = system('clear')


clear()


def udisplayplain():
    lineu1 = ["Line1 ----> ", "P1", "|", "P2", "|", "P3"]
    lineu2 = ["             ---|----|---"]
    lineu3 = ["Line2 ----> ", "P1", "|", "P2", "|", "P3"]
    lineu4 = ["             ---|----|---"]
    lineu5 = ["Line3 ----> ", "P1", "|", "P2", "|", "P3"]
    print("P = Position")
    print(" ".join(map(str, lineu1)))
    print(" ".join(map(str, lineu2)))
    print(" ".join(map(str, lineu3)))
    print(" ".join(map(str, lineu4)))
    print(" ".join(map(str, lineu5)))
    print(" ")


def understand():
    while True:

        def udisplay():
            lineu1 = ["Line1 ----> ", "P1", "|", "P2", "|", "P3"]
            lineu2 = ["             ---|----|---"]
            lineu3 = ["Line2 ----> ", "P1", "|", "P2", "|", "P3"]
            lineu4 = ["             ---|----|---"]
            lineu5 = ["Line3 ----> ", "P1", "|", "P2", "|", "P3"]
            print("Welcome To TicTacToe©")
            print("Here is a guide for the position.\n")
            print("P = Position")
            print(" ".join(map(str, lineu1)))
            print(" ".join(map(str, lineu2)))
            print(" ".join(map(str, lineu3)))
            print(" ".join(map(str, lineu4)))
            print(" ".join(map(str, lineu5)))
            print(" ")

        udisplay()
        check = input("Did you understand the guide for position?, Yes or No ")
        if (check == "Yes") or (check == "yes") or (check == "y") or (check == "Y"):
            clear()
            udisplayplain()
            break
        elif (check == "No") or (check == "no") or (check == "n") or (check == "N"):
            print("")
            print(
                "Kind clarify your doubts related to TicTacToe Positions by emailing your doubt to this email ID: "
                "boldmoon360@gmail.com")
            time.sleep(10000)
        else:
            print("")
            print("Please give a valid input")
            print("")
            time.sleep(3)
            clear()
            continue


understand()

while True:

    def single():
        while True:
            holder = 0
            line1 = [" ", "|", " ", "|", " "]
            line2 = ["--|---|--"]
            line3 = [" ", "|", " ", "|", " "]
            line4 = ["--|---|--"]
            line5 = [" ", "|", " ", "|", " "]
            print("")
            playerName = input("Enter your name: ")
            ai = "Sparky"
            print(f"{playerName}, you will be playing with our intelligent AI, {ai} \n")
            print(f"You will be x for this game.")
            print(f"{ai} will be o for this game.\n")

            aiLine = 0
            aiPosition = 0

            def display_game():
                print(" ".join(map(str, line1)))
                print(" ".join(map(str, line2)))
                print(" ".join(map(str, line3)))
                print(" ".join(map(str, line4)))
                print(" ".join(map(str, line5)))

            def game():
                count = 9
                while True:
                    global aim1, aim2, aim4, aim5, aim6, aim7, aim8, aiLine, aiPosition, aiLine, aim3, holder
                    player1line = input(f"{playerName} Enter line number for x ")
                    player1linecopy = player1line
                    if player1line.isdigit() and (player1line == "1" or player1line == "2" or player1line == "3"):
                        pass
                    else:
                        print("Enter a valid line number!!")
                        print("You are lucky for line number!!!! No punishment!!!!")
                        continue
                    player1position = input(f"{playerName} Enter position number for x ")
                    player1positioncopy = player1position
                    if player1position.isdigit() and (
                            player1position == "1" or player1position == "2" or player1position == "3"):
                        pass
                    else:
                        print("Enter a valid position")
                        print("Your PUNISHMENT is to Enter line number again!!!")
                        continue
                    player1position = int(player1position)
                    if player1position == 1:
                        player1position = 0
                    elif player1position == 2:
                        player1position = 2
                    elif player1position == 3:
                        player1position = 4
                    if player1line == "1":
                        if line1[player1position] == "x" or line1[player1position] == "o":
                            print(
                                f"Line number {player1linecopy}, Position number {player1positioncopy} already has a "
                                f"letter, "
                                f"Rule Has Been Broken!!!!!!")
                            continue
                        else:
                            pass
                        line1[player1position] = "x"
                    elif player1line == "2":
                        if line3[player1position] == "x" or line3[player1position] == "o":
                            print(
                                f"Line number {player1linecopy}, Position number {player1positioncopy} already has a "
                                f"letter, "
                                f"Rule Has Been Broken!!!!!!")
                            continue
                        else:
                            pass
                        line3[player1position] = "x"
                    elif player1line == "3":
                        if line5[player1position] == "x" or line5[player1position] == "o":
                            print(
                                f"Line number {player1linecopy}, Position number {player1positioncopy} already has a "
                                f"letter, "
                                f"Rule Has Been Broken!!!!!!")
                            continue
                        else:
                            pass
                        line5[player1position] = "x"
                    else:
                        if player1line == "1":
                            if line1[player1position] == "x" or line1[player1position] == "o":
                                print(
                                    f"Line number {player1linecopy}, Position number {player1positioncopy} already "
                                    f"has a "
                                    f"letter, Rule Has Been Broken!!!!!!")
                                continue
                            else:
                                pass
                            line1[player1position] = "x"
                        elif player1line == "2":
                            if line3[player1position] == "x" or line3[player1position] == "o":
                                print(
                                    f"Line number {player1linecopy}, Position number {player1positioncopy} already "
                                    f"has a "
                                    f"letter, Rule Has Been Broken!!!!!!")
                                continue
                            else:
                                pass
                            line3[player1position] = "x"
                        elif player1line == "3":
                            if line5[player1position] == "x" or line5[player1position] == "o":
                                print(
                                    f"Line number {player1linecopy}, Position number {player1positioncopy} already "
                                    f"has a "
                                    f"letter, Rule Has Been Broken!!!!!!")
                                continue
                            else:
                                pass
                            line5[player1position] = "x"
                    display_game()
                    if (line1[0] == "x" and line1[2] == "x" and line1[4] == "x") or (
                            line3[0] == "x" and line3[2] == "x" and line3[4] == "x") or (
                            line5[0] == "x" and line5[2] == "x" and line5[4] == "x") or (
                            line1[0] == "x" and line3[0] == "x" and line5[0] == "x") or (
                            line1[2] == "x" and line3[2] == "x" and line5[2] == "x") or (
                            line1[4] == "x" and line3[4] == "x" and line5[4] == "x") or (
                            line1[0] == "x" and line3[2] == "x" and line5[4] == "x") or (
                            line1[4] == "x" and line3[2] == "x" and line5[0] == "x"):
                        holder = 1
                        break
                    elif (line1[0] == "x" or line1[0] == "o") and (line1[2] == "x" or line1[2] == "o") and (
                            line1[4] == "x" or line1[4] == "o") and (line3[0] == "x" or line3[0] == "o") and (
                            line3[2] == "x" or line3[2] == "o") and (line3[4] == "x" or line3[4] == "o") and (
                            line5[0] == "x" or line5[0] == "o") and (line3[2] == "x" or line3[2] == "o") and (
                            line3[4] == "x" or line3[4] == "o"):
                        holder = 4
                        break

                    while True:
                        if line1[2] == " ":
                            if (line1[0] == "o") and (line1[4] == "o"):
                                line1[2] = "o"
                                aiLine = 1
                                aiPosition = 2
                                break
                        if line1[4] == " ":
                            if (line1[0] == "o") and (line1[2] == "o"):
                                line1[4] = "o"
                                aiLine = 1
                                aiPosition = 3
                                break
                        if line1[0] == " ":
                            if (line1[4] == "o") and (line1[2] == "o"):
                                line1[0] = "o"
                                aiLine = 1
                                aiPosition = 1
                                break
                        if line5[0] == " ":
                            if (line1[0] == "o") and (line3[0] == "o"):
                                line5[0] = "o"
                                aiLine = 3
                                aiPosition = 1
                                break
                        if line1[0] == " ":
                            if (line5[0] == "o") and (line3[0] == "o"):
                                line1[0] = "o"
                                aiLine = 1
                                aiPosition = 1
                                break
                        if line3[0] == " ":
                            if (line1[0] == "o") and (line5[0] == "o"):
                                line3[0] = "o"
                                aiLine = 2
                                aiPosition = 1
                                break
                        if line5[4] == " ":
                            if (line5[0] == "o") and (line5[2] == "o"):
                                line5[4] = "o"
                                aiLine = 3
                                aiPosition = 3
                                break
                        if line5[0] == " ":
                            if (line5[2] == "o") and (line5[4] == "o"):
                                line5[0] = "o"
                                aiLine = 3
                                aiPosition = 1
                                break
                        if line5[2] == " ":
                            if (line5[0] == "o") and (line5[4] == "o"):
                                line5[2] = "o"
                                aiLine = 3
                                aiPosition = 2
                                break
                        if line5[4] == " ":
                            if (line1[4] == "o") and (line3[4] == "o"):
                                line5[4] = "o"
                                aiLine = 3
                                aiPosition = 3
                                break
                        if line1[4] == " ":
                            if (line3[4] == "o") and (line5[4] == "o"):
                                line1[4] = "o"
                                aiLine = 1
                                aiPosition = 3
                                break
                        if line3[4] == " ":
                            if (line1[4] == "o") and (line5[4] == "o"):
                                line3[4] = "o"
                                aiLine = 2
                                aiPosition = 3
                                break
                        if line3[4] == " ":
                            if (line3[0] == "o") and (line3[2] == "o"):
                                line3[4] = "o"
                                aiLine = 2
                                aiPosition = 3
                                break
                        if line3[0] == " ":
                            if (line3[2] == "o") and (line3[4] == "o"):
                                line3[0] = "o"
                                aiLine = 2
                                aiPosition = 1
                                break
                        if line3[2] == " ":
                            if (line3[0] == "o") and (line3[4] == "o"):
                                line3[2] = "o"
                                aiLine = 2
                                aiPosition = 2
                                break
                        if line5[2] == " ":
                            if (line1[2] == "o") and (line3[2] == "o"):
                                line5[2] = "o"
                                aiLine = 3
                                aiPosition = 2
                                break
                        if line1[2] == " ":
                            if (line3[2] == "o") and (line5[2] == "o"):
                                line1[2] = "o"
                                aiLine = 1
                                aiPosition = 2
                                break
                        if line3[2] == " ":
                            if (line1[2] == "o") and (line5[2] == "o"):
                                line3[2] = "o"
                                aiLine = 2
                                aiPosition = 2
                                break
                        if line5[4] == " ":
                            if (line1[0] == "o") and (line3[2] == "o"):
                                line5[4] = "o"
                                aiLine = 3
                                aiPosition = 3
                                break
                        if line1[0] == " ":
                            if (line5[4] == "o") and (line3[2] == "o"):
                                line1[0] = "o"
                                aiLine = 1
                                aiPosition = 1
                                break
                        if line3[2] == " ":
                            if (line5[4] == "o") and (line1[0] == "o"):
                                line3[2] = "o"
                                aiLine = 2
                                aiPosition = 2
                                break
                        if line3[2] == " ":
                            if (line5[0] == "o") and (line1[4] == "o"):
                                line3[2] = "o"
                                aiLine = 2
                                aiPosition = 2
                                break
                        if line1[4] == " ":
                            if (line5[0] == "o") and (line3[2] == "o"):
                                line1[4] = "o"
                                aiLine = 1
                                aiPosition = 3
                                break
                        if line5[0] == " ":
                            if (line1[4] == "o") and (line3[2] == "o"):
                                line5[0] = "o"
                                aiLine = 3
                                aiPosition = 1
                                break
                        if player1line == "1":
                            if player1position == 0:
                                if line1[4] == " ":
                                    if line1[2] == "x":
                                        line1[4] = "o"
                                        aiLine = 1
                                        aiPosition = 3
                                        break
                                if line1[2] == " ":
                                    if line1[4] == "x":
                                        line1[2] = "o"
                                        aiLine = 1
                                        aiPosition = 2
                                        break
                                if line5[0] == " ":
                                    if line3[0] == "x":
                                        line5[0] = "o"
                                        aiLine = 3
                                        aiPosition = 1
                                        break
                                if line3[0] == " ":
                                    if line5[0] == "x":
                                        line3[0] = "o"
                                        aiLine = 2
                                        aiPosition = 1
                                        break
                                if line5[4] == " ":
                                    if line3[2] == "x":
                                        line5[4] = "o"
                                        aiLine = 3
                                        aiPosition = 3
                                if line3[2] == " ":
                                    if line5[4] == "x":
                                        line3[2] = "o"
                                        aiLine = 2
                                        aiPosition = 2
                                        break

                            if player1position == 2:
                                if line5[2] == " ":
                                    if line3[2] == "x":
                                        line5[2] = "o"
                                        aiLine = 3
                                        aiPosition = 2
                                        break
                                if line3[2] == " ":
                                    if line5[2] == "x":
                                        line3[2] = "o"
                                        aiLine = 2
                                        aiPosition = 2
                                        break
                                if line1[4] == " ":
                                    if line1[0] == "x":
                                        line1[4] = "o"
                                        aiLine = 1
                                        aiPosition = 3
                                        break
                                if line1[0] == " ":
                                    if line1[4] == "x":
                                        line1[0] = "o"
                                        aiLine = 1
                                        aiPosition = 1
                                        break

                            if player1position == 4:
                                if line1[2] == " ":
                                    if line1[0] == "x":
                                        line1[2] = "o"
                                        aiLine = 2
                                        aiPosition = 2
                                        break
                                if line1[0] == " ":
                                    if line1[2] == "x":
                                        line1[0] = "o"
                                        aiLine = 1
                                        aiPosition = 1
                                        break
                                if line5[4] == " ":
                                    if line3[4] == "x":
                                        line5[4] = "o"
                                        aiLine = 3
                                        aiPosition = 3
                                        break
                                if line5[4] == " ":
                                    if line5[4] == "x":
                                        line3[4] = "o"
                                        aiLine = 2
                                        aiPosition = 3
                                        break
                                if line5[0] == " ":
                                    if line3[2] == "x":
                                        line5[0] = "o"
                                        aiLine = 3
                                        aiPosition = 1
                                        break
                                if line3[2] == " ":
                                    if line5[0] == "x":
                                        line3[2] = "o"
                                        aiLine = 2
                                        aiPosition = 2
                                        break

                        if player1line == "2":
                            if player1position == 0:
                                if line5[0] == " ":
                                    if line1[0] == "x":
                                        line5[0] = "o"
                                        aiLine = 3
                                        aiPosition = 1
                                        break
                                if line1[0] == " ":
                                    if line5[0] == "x":
                                        line1[0] = "o"
                                        aiLine = 1
                                        aiPosition = 1
                                        break
                                if line3[4] == " ":
                                    if line3[2] == "x":
                                        line3[4] = "o"
                                        aiLine = 2
                                        aiPosition = 3
                                        break
                                if line3[2] == " ":
                                    if line3[4] == "x":
                                        line3[2] = "o"
                                        aiLine = 2
                                        aiPosition = 2
                                        break

                            if player1position == 2:
                                if line5[2] == " ":
                                    if line1[2] == "x":
                                        line5[2] = "o"
                                        aiLine = 3
                                        aiPosition = 2
                                        break
                                if line1[2] == " ":
                                    if line5[2] == "x":
                                        line1[2] = "o"
                                        aiLine = 1
                                        aiPosition = 2
                                        break
                                if line3[4] == " ":
                                    if line3[0] == "x":
                                        line3[4] = "o"
                                        aiLine = 2
                                        aiPosition = 3
                                        break
                                if line3[0] == " ":
                                    if line3[4] == "x":
                                        line3[0] = "o"
                                        aiLine = 2
                                        aiPosition = 1
                                        break
                                if line1[4] == " ":
                                    if line5[0] == "x":
                                        line1[4] = "o"
                                        aiLine = 1
                                        aiPosition = 3
                                        break
                                if line5[0] == " ":
                                    if line1[4] == "x":
                                        line5[0] = "o"
                                        aiLine = 3
                                        aiPosition = 1
                                        break
                                if line5[4] == " ":
                                    if line1[0] == "x":
                                        line5[4] = "o"
                                        aiLine = 3
                                        aiPosition = 3
                                        break
                                if line1[0] == " ":
                                    if line5[4] == "x":
                                        line1[0] = "o"
                                        aiLine = 1
                                        aiPosition = 1
                                        break

                            if player1position == 4:
                                if line5[4] == " ":
                                    if line1[4] == "x":
                                        line5[4] = "o"
                                        aiLine = 3
                                        aiPosition = 3
                                        break
                                if line1[4] == " ":
                                    if line5[4] == "x":
                                        line1[4] = "o"
                                        aiLine = 1
                                        aiPosition = 3
                                        break
                                if line3[2] == " ":
                                    if line3[0] == "x":
                                        line3[2] = "o"
                                        aiLine = 2
                                        aiPosition = 2
                                        break
                                if line3[0] == " ":
                                    if line3[2] == "x":
                                        line3[0] = "o"
                                        aiLine = 2
                                        aiPosition = 1
                                        break

                        if player1line == "3":
                            if player1position == 0:
                                if line5[2] == " ":
                                    if line5[4] == "x":
                                        line5[2] = "o"
                                        aiLine = 3
                                        aiPosition = 2
                                        break
                                if line5[4] == " ":
                                    if line5[2] == "x":
                                        line5[4] = "o"
                                        aiLine = 3
                                        aiPosition = 3
                                        break
                                if line3[0] == " ":
                                    if line1[0] == "x":
                                        line3[0] = "o"
                                        aiLine = 2
                                        aiPosition = 1
                                        break
                                if line1[0] == " ":
                                    if line3[0] == "x":
                                        line1[0] = "o"
                                        aiLine = 1
                                        aiPosition = 1
                                        break
                                if line3[2] == " ":
                                    if line1[4] == "x":
                                        line3[2] = "o"
                                        aiLine = 2
                                        aiPosition = 2
                                        break
                                if line1[4] == " ":
                                    if line3[2] == "x":
                                        line1[4] = "o"
                                        aiLine = 1
                                        aiPosition = 3
                                        break

                            if player1position == 2:
                                if line5[4] == " ":
                                    if line5[0] == "x":
                                        line5[4] = "o"
                                        aiLine = 3
                                        aiPosition = 3
                                        break
                                if line5[0] == " ":
                                    if line5[4] == "x":
                                        line5[0] = "o"
                                        aiLine = 3
                                        aiPosition = 1
                                        break
                                if line3[2] == " ":
                                    if line1[2] == "x":
                                        line3[2] = "o"
                                        aiLine = 2
                                        aiPosition = 2
                                        break
                                if line1[2] == " ":
                                    if line3[2] == "x":
                                        line1[2] = "o"
                                        aiLine = 1
                                        aiPosition = 2
                                        break

                            if player1position == 4:
                                if line5[2] == " ":
                                    if line5[0] == "x":
                                        line5[2] = "o"
                                        aiLine = 3
                                        aiPosition = 2
                                        break
                                if line5[0] == " ":
                                    if line5[2] == "x":
                                        line5[0] = "o"
                                        aiLine = 3
                                        aiPosition = 1
                                        break
                                if line3[4] == " ":
                                    if line1[4] == "x":
                                        line3[4] = "o"
                                        aiLine = 2
                                        aiPosition = 3
                                        break
                                if line1[4] == " ":
                                    if line3[4] == "x":
                                        line1[4] = "o"
                                        aiLine = 1
                                        aiPosition = 3
                                        break
                                if line3[2] == " ":
                                    if line1[0] == "x":
                                        line3[2] = "o"
                                        aiLine = 2
                                        aiPosition = 2
                                        break
                                if line1[0] == " ":
                                    if line3[2] == "x":
                                        line1[0] = "o"
                                        aiLine = 1
                                        aiPosition = 1
                                        break

                        if count == 9:
                            aim1 = line1[0] == " " and line1[2] == " " and line1[4] == " "
                            aim2 = line3[0] == " " and line3[2] == " " and line3[4] == " "
                            aim3 = line5[0] == " " and line5[2] == " " and line5[4] == " "
                            aim4 = line1[0] == " " and line3[0] == " " and line5[0] == " "
                            aim5 = line1[2] == " " and line3[2] == " " and line5[2] == " "
                            aim6 = line1[4] == " " and line3[4] == " " and line5[4] == " "
                            aim7 = line1[0] == " " and line3[2] == " " and line5[4] == " "
                            aim8 = line1[4] == " " and line3[2] == " " and line5[0] == " "
                            count = 0
                        if aim1:
                            count = count + 1
                            if count == 1:
                                if line1[0] == " ":
                                    line1[0] = "o"
                                    aiLine = 1
                                    aiPosition = 1
                                    aim1 = line1[0] == "o" and line1[2] == " " and line1[4] == " "
                                    break
                                else:
                                    count = count + 1
                            elif count == 2:
                                if line1[2] == " ":
                                    line1[2] = "o"
                                    aiLine = 1
                                    aiPosition = 2
                                    aim1 = line1[0] == "o" and line1[2] == "o" and line1[4] == " "
                                    break
                                else:
                                    count = 0
                        if aim2:
                            count = count + 1
                            if count == 1:
                                if line3[0] == " ":
                                    line3[0] = "o"
                                    aiLine = 2
                                    aiPosition = 1
                                    aim2 = line3[0] == "o" and line3[2] == " " and line3[4] == " "
                                    break
                                else:
                                    count = count + 1
                            elif count == 2:
                                if line3[2] == " ":
                                    line3[2] = "o"
                                    aiLine = 2
                                    aiPosition = 2
                                    aim2 = line3[0] == "o" and line3[2] == "o" and line3[4] == " "
                                    break
                                else:
                                    count = 0
                        if aim3:
                            count = count + 1
                            if count == 1:
                                if line5[0] == " ":
                                    line5[0] = "o"
                                    aiLine = 3
                                    aiPosition = 1
                                    aim3 = line5[0] == "o" and line5[2] == " " and line5[4] == " "
                                    break
                                else:
                                    count = count + 1
                            if count == 2:
                                if line5[2] == " ":
                                    line5[2] = "o"
                                    aiLine = 3
                                    aiPosition = 2
                                    aim3 = line5[0] == "o" and line5[2] == "o" and line5[4] == " "
                                    break
                                else:
                                    count = 0
                        if aim4:
                            count = count + 1
                            if count == 1:
                                if line1[0] == " ":
                                    line1[0] = "o"
                                    aiLine = 1
                                    aiPosition = 1
                                    aim4 = line1[0] == "o" and line3[0] == " " and line5[0] == " "
                                    break
                                else:
                                    count = count + 1
                            elif count == 2:
                                if line3[0] == " ":
                                    line3[0] = "o"
                                    aiLine = 2
                                    aiPosition = 1
                                    aim4 = line1[0] == "o" and line3[0] == "o" and line5[0] == " "
                                    break
                                else:
                                    count = 0
                        if aim5:
                            count = count + 1
                            if count == 1:
                                if line1[2] == " ":
                                    line1[2] = "o"
                                    aiLine = 1
                                    aiPosition = 2
                                    aim5 = line1[2] == "o" and line3[2] == " " and line5[2] == " "
                                    break
                                else:
                                    count = count + 1
                            elif count == 2:
                                if line3[2] == " ":
                                    line3[2] = "o"
                                    aiLine = 2
                                    aiPosition = 2
                                    aim5 = line1[2] == "o" and line3[2] == "o" and line5[2] == " "
                                    break
                                else:
                                    count = 0
                        if aim6:
                            count = count + 1
                            if count == 1:
                                if line1[4] == " ":
                                    line1[4] = "o"
                                    aiLine = 1
                                    aiPosition = 3
                                    aim6 = line1[4] == "o" and line3[4] == " " and line5[4] == " "
                                    break
                                else:
                                    count = count + 1
                            elif count == 2:
                                if line3[4] == " ":
                                    line3[4] = "o"
                                    aiLine = 2
                                    aiPosition = 3
                                    aim6 = line1[4] == "o" and line3[4] == "o" and line5[4] == " "
                                    break
                                else:
                                    count = 0
                        if aim7:
                            count = count + 1
                            if count == 1:
                                if line1[0] == " ":
                                    line1[0] = "o"
                                    aiLine = 1
                                    aiPosition = 1
                                    aim7 = line1[0] == "o" and line3[2] == " " and line5[4] == " "
                                    break
                                else:
                                    count = count + 1
                            elif count == 2:
                                if line3[2] == " ":
                                    line3[2] = "o"
                                    aiLine = 2
                                    aiPosition = 2
                                    aim7 = line1[0] == "o" and line3[2] == "o" and line5[4] == " "
                                    break
                                else:
                                    count = 0
                        if aim8:
                            count = count + 1
                            if count == 1:
                                if line1[4] == " ":
                                    line1[4] = "o"
                                    aiLine = 1
                                    aiPosition = 3
                                    aim8 = line1[4] == "o" and line3[2] == " " and line5[0] == " "
                                    break
                            elif count == 2:
                                if line3[2] == " ":
                                    line3[2] = "o"
                                    aiLine = 2
                                    aiPosition = 2
                                    aim8 = line1[4] == "o" and line3[2] == "o" and line5[0] == " "
                                    break
                                else:
                                    count = 0

                        if line1[0] == " ":
                            line1[0] = "o"
                            aiLine = 1
                            aiPosition = 1
                            break
                        elif line1[2] == " ":
                            line1[2] = "o"
                            aiLine = 1
                            aiPosition = 2
                            break
                        elif line1[4] == " ":
                            line1[4] = "o"
                            aiLine = 1
                            aiPosition = 3
                            break
                        elif line3[0] == " ":
                            line3[0] = "o"
                            aiLine = 2
                            aiPosition = 1
                            break
                        elif line3[2] == " ":
                            line3[2] = "o"
                            aiLine = 2
                            aiPosition = 2
                            break
                        elif line3[4] == " ":
                            line3[4] = "o"
                            aiLine = 2
                            aiPosition = 3
                            break
                        elif line5[0] == " ":
                            line5[0] = "o"
                            aiLine = 3
                            aiPosition = 1
                            break
                        elif line5[2] == " ":
                            line5[2] = "o"
                            aiLine = 3
                            aiPosition = 2
                            break
                        elif line5[4] == " ":
                            line5[4] = "o"
                            aiLine = 3
                            aiPosition = 3
                            break

                    print(f"{ai} Enter line number for o ", end=' ')
                    time.sleep(0.7)
                    print(aiLine)
                    print(f"{ai} Enter position number for o ", end=' ')
                    time.sleep(0.7)
                    print(aiPosition)
                    time.sleep(0.3)
                    display_game()
                    if (line1[0] == "o" and line1[2] == "o" and line1[4] == "o") or (
                            line3[0] == "o" and line3[2] == "o" and line3[4] == "o") or (
                            line5[0] == "o" and line5[2] == "o" and line5[4] == "o") or (
                            line1[0] == "o" and line3[0] == "o" and line5[0] == "o") or (
                            line1[2] == "o" and line3[2] == "o" and line5[2] == "o") or (
                            line1[4] == "o" and line3[4] == "o" and line5[4] == "o") or (
                            line1[0] == "o" and line3[2] == "o" and line5[4] == "o") or (
                            line1[4] == "o" and line3[2] == "o" and line5[0] == "o"):
                        holder = 2
                        break
                    elif (line1[0] == "x" or line1[0] == "o") and \
                            (line1[2] == "x" or line1[2] == "o") and \
                            (line1[4] == "x" or line1[4] == "o") and \
                            (line3[0] == "x" or line3[0] == "o") and \
                            (line3[2] == "x" or line3[2] == "o") and \
                            (line3[4] == "x" or line3[4] == "o") and \
                            (line5[0] == "x" or line5[0] == "o") and \
                            (line3[2] == "x" or line3[2] == "o") and \
                            (line3[4] == "x" or line3[4] == "o"):
                        holder = 4
                        break

                if holder == 1:
                    print(f"\nGood Job {playerName}!!!!!!, You are The Winner!!!")
                    print("Play Again Confirmation Will Be Asked In 15 Seconds ")
                    time.sleep(15)
                elif holder == 2:
                    print(f"\nGood Job {ai}!!!!!!, You are The Winner!!!")
                    print("Play Again Confirmation Will Be Asked In 15 Seconds ")
                    time.sleep(15)
                elif holder == 4:
                    print(f"\nIts a draw match!!!")
                    print("Play Again Confirmation Will Be Asked In 15 Seconds ")
                    time.sleep(15)
                else:
                    print("\nThis is a cheat game!!!")
                    print("Play Again Confirmation Will Be Asked In 15 Seconds ")
                    time.sleep(15)

            game()
            break


    def multi():
        while True:
            holder = 0
            line1 = [" ", "|", " ", "|", " "]
            line2 = ["--|---|--"]
            line3 = [" ", "|", " ", "|", " "]
            line4 = ["--|---|--"]
            line5 = [" ", "|", " ", "|", " "]
            print("")
            player1name = input("Name of Player One: ")
            player2name = input("Name of Player Two: ")
            print(" ")
            randomUser = random.choice([player2name, player1name])
            print(f"{randomUser} will be x for this game. \n")
            if randomUser == player1name:
                anotherUser = player2name
            else:
                anotherUser = player1name

            def display_game():
                print(" ".join(map(str, line1)))
                print(" ".join(map(str, line2)))
                print(" ".join(map(str, line3)))
                print(" ".join(map(str, line4)))
                print(" ".join(map(str, line5)))

            def game():
                while True:
                    global holder
                    player1line = input(f"{randomUser} Enter line number for x ")
                    player1linecopy = player1line
                    if player1line.isdigit() and (player1line == "1" or player1line == "2" or player1line == "3"):
                        pass
                    else:
                        print("Enter a valid line number!!")
                        print("You are lucky for line number!!!! No punishment!!!!")
                        continue
                    player1position = input(f"{randomUser} Enter position number for x ")
                    player1positioncopy = player1position
                    if player1position.isdigit() and (
                            player1position == "1" or player1position == "2" or player1position == "3"):
                        pass
                    else:
                        print("Enter a valid position")
                        print("Your PUNISHMENT is to Enter line number again!!!")
                        continue
                    player1position = int(player1position)
                    if player1position == 1:
                        player1position = 0
                    elif player1position == 2:
                        player1position = 2
                    elif player1position == 3:
                        player1position = 4
                    if player1line == "1":
                        if line1[player1position] == "x" or line1[player1position] == "o":
                            print(
                                f"Line number {player1linecopy}, Position number {player1positioncopy} already has a "
                                f"letter, Rule Has Been Broken!!!!!!")
                            continue
                        else:
                            pass
                        line1[player1position] = "x"
                    elif player1line == "2":
                        if line3[player1position] == "x" or line3[player1position] == "o":
                            print(
                                f"Line number {player1linecopy}, Position number {player1positioncopy} already has a "
                                f"letter, Rule Has Been Broken!!!!!!")
                            continue
                        else:
                            pass
                        line3[player1position] = "x"
                    elif player1line == "3":
                        if line5[player1position] == "x" or line5[player1position] == "o":
                            print(
                                f"Line number {player1linecopy}, Position number {player1positioncopy} already has a "
                                f"letter, Rule Has Been Broken!!!!!!")
                            continue
                        else:
                            pass
                        line5[player1position] = "x"
                    else:
                        if player1line == "1":
                            if line1[player1position] == "x" or line1[player1position] == "o":
                                print(
                                    f"Line number {player1linecopy}, Position number {player1positioncopy} already "
                                    f"has a letter, Rule Has Been Broken!!!!!!")
                                continue
                            else:
                                pass
                            line1[player1position] = "x"
                        elif player1line == "2":
                            if line3[player1position] == "x" or line3[player1position] == "o":
                                print(
                                    f"Line number {player1linecopy}, Position number {player1positioncopy} already "
                                    f"has a letter, Rule Has Been Broken!!!!!!")
                                continue
                            else:
                                pass
                            line3[player1position] = "x"
                        elif player1line == "3":
                            if line5[player1position] == "x" or line5[player1position] == "o":
                                print(
                                    f"Line number {player1linecopy}, Position number {player1positioncopy} already "
                                    f"has a letter, Rule Has Been Broken!!!!!!")
                                continue
                            else:
                                pass
                            line5[player1position] = "x"
                    display_game()
                    if (line1[0] == "x" and line1[2] == "x" and line1[4] == "x") or (
                            line3[0] == "x" and line3[2] == "x" and line3[4] == "x") or (
                            line5[0] == "x" and line5[2] == "x" and line5[4] == "x") or (
                            line1[0] == "x" and line3[0] == "x" and line5[0] == "x") or (
                            line1[2] == "x" and line3[2] == "x" and line5[2] == "x") or (
                            line1[4] == "x" and line3[4] == "x" and line5[4] == "x") or (
                            line1[0] == "x" and line3[2] == "x" and line5[4] == "x") or (
                            line1[4] == "x" and line3[2] == "x" and line5[0] == "x"):
                        holder = 1
                        break
                    elif (line1[0] == "x" or line1[0] == "o") and (line1[2] == "x" or line1[2] == "o") and (
                            line1[4] == "x" or line1[4] == "o") and (line3[0] == "x" or line3[0] == "o") and (
                            line3[2] == "x" or line3[2] == "o") and (line3[4] == "x" or line3[4] == "o") and (
                            line5[0] == "x" or line5[0] == "o") and (line3[2] == "x" or line3[2] == "o") and (
                            line3[4] == "x" or line3[4] == "o"):
                        holder = 4
                        break
                    player2line = input(f"{anotherUser} Enter line number for o ")
                    player2linecopy = player2line
                    if player1line.isdigit() and (player1line == "1" or player1line == "2" or player1line == "3"):
                        pass
                    else:
                        print("Enter a valid line number!!")
                        print("Your PUNISHMENT is to skip your chance!!!")
                        continue
                    player2position = input(f"{anotherUser} Enter position number for o ")
                    player2positioncopy = player2position
                    if player2position.isdigit() and (
                            player2position == "1" or player2position == "2" or player2position == "3"):
                        pass
                    else:
                        print("Enter a valid position")
                        print("Your PUNISHMENT is to skip your chance!!!")
                        continue
                    player2position = int(player2position)
                    if player2position == 1:
                        player2position = 0
                    elif player2position == 2:
                        player2position = 2
                    elif player2position == 3:
                        player2position = 4
                    if player2line == "1":
                        if line1[player2position] == "x" or line1[player2position] == "o":
                            print(
                                f"Line number {player2linecopy}, Position number {player2positioncopy} already has a "
                                f"letter, Rule Has Been Broken!!!!!!")
                            continue
                        else:
                            pass
                        line1[player2position] = "o"
                    elif player2line == "2":
                        if line3[player2position] == "x" or line3[player2position] == "o":
                            print(
                                f"Line number {player2linecopy}, Position number {player2positioncopy} already has a "
                                f"letter, Rule Has Been Broken!!!!!!")
                            continue
                        else:
                            pass
                        line3[player2position] = "o"
                    elif player2line == "3":
                        if line5[player2position] == "x" or line5[player2position] == "o":
                            print(
                                f"Line number {player2linecopy}, Position number {player2positioncopy} already has a "
                                f"letter, Rule Has Been Broken!!!!!!")
                            continue
                        else:
                            pass
                        line5[player2position] = "o"
                    else:
                        if player2line == "1":
                            if line1[player2position] == "x" or line1[player2position] == "o":
                                print(
                                    f"Line number {player2linecopy}, Position number {player2positioncopy} already "
                                    f"has a letter, Rule Has Been Broken!!!!!!")
                                continue
                            else:
                                pass
                            line1[player2position] = "o"
                        elif player2line == "2":
                            if line3[player2position] == "x" or line3[player2position] == "o":
                                print(
                                    f"Line number {player2linecopy}, Position number {player2positioncopy} already "
                                    f"has a letter, Rule Has Been Broken!!!!!!")
                                continue
                            else:
                                pass
                            line3[player2position] = "o"
                        elif player2line == "3":
                            if line5[player2position] == "x" or line5[player2position] == "o":
                                print(
                                    f"Line number {player2linecopy}, Position number {player2positioncopy} already "
                                    f"has a letter, Rule Has Been Broken!!!!!!")
                                continue
                            else:
                                pass
                            line5[player2position] = "o"
                    display_game()
                    if (line1[0] == "o" and line1[2] == "o" and line1[4] == "o") or (
                            line3[0] == "o" and line3[2] == "o" and line3[4] == "o") or (
                            line5[0] == "o" and line5[2] == "o" and line5[4] == "o") or (
                            line1[0] == "o" and line3[0] == "o" and line5[0] == "o") or (
                            line1[2] == "o" and line3[2] == "o" and line5[2] == "o") or (
                            line1[4] == "o" and line3[4] == "o" and line5[4] == "o") or (
                            line1[0] == "o" and line3[2] == "o" and line5[4] == "o") or (
                            line1[4] == "o" and line3[2] == "o" and line5[0] == "o"):
                        holder = 2
                        break
                    elif (line1[0] == "x" or line1[0] == "o") and \
                            (line1[2] == "x" or line1[2] == "o") and \
                            (line1[4] == "x" or line1[4] == "o") and \
                            (line3[0] == "x" or line3[0] == "o") and \
                            (line3[2] == "x" or line3[2] == "o") and \
                            (line3[4] == "x" or line3[4] == "o") and \
                            (line5[0] == "x" or line5[0] == "o") and \
                            (line3[2] == "x" or line3[2] == "o") and \
                            (line3[4] == "x" or line3[4] == "o"):
                        holder = 4
                        break

                if holder == 1:
                    print(f"\nGood Job {randomUser}!!!!!!, You are The Winner!!!")
                    print("Play Again Confirmation Will Be Asked In 15 Seconds ")
                    time.sleep(15)
                elif holder == 2:
                    print(f"\nGood Job {anotherUser}!!!!!!, You are The Winner!!!")
                    print("Play Again Confirmation Will Be Asked In 15 Seconds ")
                    time.sleep(15)
                elif holder == 4:
                    print(f"\nIts a draw match!!!")
                    print("Play Again Confirmation Will Be Asked In 15 Seconds ")
                    time.sleep(15)
                else:
                    print("\nThis is a cheat game!!!")
                    print("Play Again Confirmation Will Be Asked In 15 Seconds ")
                    time.sleep(15)

            game()
            break


    while True:
        print(" ")
        option = input("Multiplayer Or Single Player? (m or s) : ")
        if (option == "s") or (option == "S"):
            single()
            break
        elif (option == "m") or (option == "M"):
            multi()
            break
        else:
            print("Enter Valid Option!")
    clear()
    ask = input("\nDo you want to play again? (Yes or No) : ")
    if (ask == "Yes") or (ask == "yes") or (ask == "y") or (ask == "Y"):
        clear()
        udisplayplain()
        continue
    elif (ask == "No") or (ask == "no") or (ask == "n") or (ask == "N"):
        clear()
        print("\nA project developed and maintained by Harish Ashokkumar")
        print("\nIf you found any bugs please email to email ID: boldmoon360@gmail.com")
        print("\nThank you for playing TicTacToe© :)")
        time.sleep(120)
        break
    else:
        print(
            "\nInvalid Input, Give a proper input last chance one more invalid input then you will be thrown out "
            "of "
            "the game!!!!!!!!!!! ")
        ask = input("\nDo you want to play again? (Yes or No) : ")
        if (ask == "Yes") or (ask == "yes") or (ask == "y") or (ask == "Y"):
            clear()
            udisplayplain()
            continue
        elif (ask == "No") or (ask == "no") or (ask == "n") or (ask == "N"):
            clear()
            print("\nA project developed and maintained by Harish Ashokkumar")
            print("\nIf you found any bugs please email to email ID: boldmoon360@gmail.com")
            print("\nThank you for playing TicTacToe© :)")
            time.sleep(120)
            break
        else:
            print("\nYou are a very bad person!!!!!!!!!!!!!!!!!")
            print("\nI am throwing you out!!!!!!!!!!!!!!!!!!!")
            time.sleep(10)
            break
