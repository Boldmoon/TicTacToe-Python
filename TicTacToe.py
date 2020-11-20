import random
import time
while True:
    holder = 0
    line1 = [" ", "|", " ", "|", " "]
    line2 = ["--|---|--"]
    line3 = [" ", "|", " ", "|", " "]
    line4 = ["--|---|--"]
    line5 = [" ", "|", " ", "|", " "]
    player1name = input("Name of Player One: ")
    player2name = input("Name of Player Two: ")
    randomUser = random.choice([player2name, player1name])
    print(f"{randomUser} will be x for this game.")
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
            if player1position.isdigit() and (player1position == "1" or player1position == "2" or player1position == "3"):
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
                        f"Line number {player1linecopy}, Position number {player1positioncopy} already has a letter, Rule Has Been Broken!!!!!!")
                    continue
                else:
                    pass
                line1[player1position] = "x"
            elif player1line == "2":
                if line3[player1position] == "x" or line3[player1position] == "o":
                    print(
                        f"Line number {player1linecopy}, Position number {player1positioncopy} already has a letter, Rule Has Been Broken!!!!!!")
                    continue
                else:
                    pass
                line3[player1position] = "x"
            elif player1line == "3":
                if line5[player1position] == "x" or line5[player1position] == "o":
                    print(
                        f"Line number {player1linecopy}, Position number {player1positioncopy} already has a letter, Rule Has Been Broken!!!!!!")
                    continue
                else:
                    pass
                line5[player1position] = "x"
            else:
                if player1line == "1":
                    if line1[player1position] == "x" or line1[player1position] == "o":
                        print(
                            f"Line number {player1linecopy}, Position number {player1positioncopy} already has a letter, Rule Has Been Broken!!!!!!")
                        continue
                    else:
                        pass
                    line1[player1position] = "x"
                elif player1line == "2":
                    if line3[player1position] == "x" or line3[player1position] == "o":
                        print(
                            f"Line number {player1linecopy}, Position number {player1positioncopy} already has a letter, Rule Has Been Broken!!!!!!")
                        continue
                    else:
                        pass
                    line3[player1position] = "x"
                elif player1line == "3":
                    if line5[player1position] == "x" or line5[player1position] == "o":
                        print(
                            f"Line number {player1linecopy}, Position number {player1positioncopy} already has a letter, Rule Has Been Broken!!!!!!")
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
            elif (line1[0] == "x" or line1[0] == "o") and (line1[2] == "x" or line1[2] == "o") and (line1[4] == "x" or line1[4] == "o") and (line3[0] == "x" or line3[0] == "o") and (line3[2] == "x" or line3[2] == "o") and (line3[4] == "x" or line3[4] == "o") and (line5[0] == "x" or line5[0] == "o") and (line3[2] == "x" or line3[2] == "o") and (line3[4] == "x" or line3[4] == "o"):
                holder = 4
                break
            player2line = input(f"{anotherUser} Enter line number for o ")
            player2linecopy = player2line
            if player1line.isdigit() and (player1line == "1" or player1line == "2" or player1line == "3"):
                pass
            else:
                print("Enter a valid line number!!")
                print("Your PUNISHMENT is to skip youur chance!!!")
                continue
            player2position = input(f"{anotherUser} Enter position number for o ")
            player2positioncopy = player2position
            if player2position.isdigit() and (player2position == "1" or player2position == "2" or player2position == "3"):
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
                        f"Line number {player2linecopy}, Position number {player2positioncopy} already has a letter, Rule Has Been Broken!!!!!!")
                    continue
                else:
                    pass
                line1[player2position] = "o"
            elif player2line == "2":
                if line3[player2position] == "x" or line3[player2position] == "o":
                    print(
                        f"Line number {player2linecopy}, Position number {player2positioncopy} already has a letter, Rule Has Been Broken!!!!!!")
                    continue
                else:
                    pass
                line3[player2position] = "o"
            elif player2line == "3":
                if line5[player2position] == "x" or line5[player2position] == "o":
                    print(
                        f"Line number {player2linecopy}, Position number {player2positioncopy} already has a letter, Rule Has Been Broken!!!!!!")
                    continue
                else:
                    pass
                line5[player2position] = "o"
            else:
                if player2line == "1":
                    if line1[player2position] == "x" or line1[player2position] == "o":
                        print(
                            f"Line number {player2linecopy}, Position number {player2positioncopy} already has a letter, Rule Has Been Broken!!!!!!")
                        continue
                    else:
                        pass
                    line1[player2position] = "o"
                elif player2line == "2":
                    if line3[player2position] == "x" or line3[player2position] == "o":
                        print(
                            f"Line number {player2linecopy}, Position number {player2positioncopy} already has a letter, Rule Has Been Broken!!!!!!")
                        continue
                    else:
                        pass
                    line3[player2position] = "o"
                elif player2line == "3":
                    if line5[player2position] == "x" or line5[player2position] == "o":
                        print(
                            f"Line number {player2linecopy}, Position number {player2positioncopy} already has a letter, Rule Has Been Broken!!!!!!")
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
        elif holder == 2:
            print(f"\nGood Job {anotherUser}!!!!!!, You are The Winner!!!")
        elif holder == 4:
            print(f"\nIts a draw match!!!")
        else:
            print("\nThis is a cheat game!!!")
    game()
    ask = input("\nDo you want to play again? Yes or No ")
    if (ask == "Yes") or (ask == "yes") or (ask == "y") or (ask == "Y"):
        continue
    elif (ask == "No") or (ask == "no") or (ask == "n") or (ask == "N"):
        print("\nA project developed and maintained by Harish")
        print("\nFor more information visit www.goldmoon.in")
        print("\nThank you for playing TicTackleToe© :)")
        time.sleep(60)
        break
    else:
        print("\nInvalid Input, Give a proper input last chance one more invalid input then you will be thrown out of the game!!!!!!!!!!! ")
        ask = input("\nDo you want to play again? Yes or No!!! ")
        if (ask == "Yes") or (ask == "yes") or (ask == "y") or (ask == "Y"):
            continue
        elif (ask == "No") or (ask == "no") or (ask == "n") or (ask == "N"):
            break
        else:
            print("\nYou are a very bad person!!!!!!!!!!!!!!!!!")
            print("\nI am throwing you out!!!!!!!!!!!!!!!!!!!")
            break