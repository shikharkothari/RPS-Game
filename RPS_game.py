import sys
import random
import time
import os
os.system("cls")
a = '\033[95m'#purple
b = '\033[94m'#indigo
c = '\033[96m'#blue
d = '\033[92m'#green
e = '\033[93m'#yellow
f = '\033[91m'#red
g = '\033[0m'#end
h = '\033[1m'#bold
u = '\033[4m'#underline
print(f"{a}Welcome to ROCK, PAPER, SCISSORS game (+_+){g}")
while True:
    point_game = input("Enter how many rounds you want to play:")
    try:
        point_game = int(point_game)
    except Exception as exeption_e:
        print(f"{u}{f}{h}Please enter integer{g}")
    else:
        break
comp_score = 0
your_score = 0
for i in range(point_game):
    input1 = str(input("\n\nRock..Paper..Scissors..:"))
    if input1 == 'r':
        mr_list = ["Rock", "Paper", "Scissors", "Paper", "Scissors", "Paper", "Scissors", "Scissors"]
        comp_choice = random.choice(mr_list)
        print(f"Computer chose {u}{comp_choice}{g}")
        if comp_choice == 'Rock':
            comp_score += 1
            your_score += 1
            print(f"{e}Tied#{g}  {b}Your Score:{your_score} and Comp Score:{comp_score}{g}\n")
        elif comp_choice == 'Paper':
            comp_score += 1
            print(f"{f}You Lose :({g}  {b}Your Score:{your_score} and Comp Score:{comp_score}{g}\n")
        elif comp_choice == 'Scissors':
            your_score += 1
            print(f"{c}You Won! :){g}  {b}Your Score:{your_score} and Comp Score:{comp_score}{g}\n")
        else:
            print(f"{u}{h}{f}AN ERROR OCCURED{g}")
    elif input1 == 'p':
        mr_list2 = ["Paper", "Rock", "Scissors", "Rock", "Scissors", "Rock", "Scissors", "Rock"]
        comp_choice = random.choice(mr_list2)
        print(f"Computer chose {u}{comp_choice}{g}")
        if comp_choice == 'Paper':
            comp_score += 1
            your_score += 1
            print(f"{e}Tied#{g}  {b}Your Score:{your_score} and Comp Score:{comp_score}{g}\n")
        elif comp_choice == 'Scissors':
            comp_score += 1
            print(f"{f}You Lose :({g}  {b}Your Score:{your_score} and Comp Score:{comp_score}{g}\n")
        elif comp_choice == 'Rock':
            your_score += 1
            print(f"{c}You Won! :){g}  {b}Your Score:{your_score} and Comp Score:{comp_score}{g}\n")
        else:
            print(f"{u}{h}{f}AN ERROR OCCURED{g}")
    elif input1 == 's':
        mr_list2 = ["Scissors", "Rock", "Paper", "Rock", "Paper", "Rock", "Paper", "Paper"]
        comp_choice = random.choice(mr_list2)
        print(f"Computer chose {u}{comp_choice}{g}")
        if comp_choice == 'Scissors':
            comp_score += 1
            your_score += 1
            print(f"{e}Tied#{g}  {b}Your Score:{your_score} and Comp Score:{comp_score}{g}\n")
        elif comp_choice == 'Rock':
            comp_score += 1
            print(f"{f}You Lose :({g}  {b}Your Score:{your_score} and Comp Score:{comp_score}{g}\n")
        elif comp_choice == 'Paper':
            your_score += 1
            print(f"{c}You Won! :){g}  {b}Your Score:{your_score} and Comp Score:{comp_score}{g}\n")
        else:
            print(f"{u}{h}{f}AN ERROR OCCURED{g}")
    else:
        print(f"{u}{h}{f}--PLEASE CHOOSE VALID KEY--{g}")
if your_score>=comp_score:
    print("You won the game!!")
elif your_score<=comp_score:
    print("You lose! Better luck next time..")
time.sleep(0.90)
words1 = "nice to play with you"
for char in words1:
    time.sleep(0.15)
    sys.stdout.write(char)
    sys.stdout.flush()
time.sleep(0.5)
words2 = "\nOkay, I have to leave now, see you soon.."
for char in words2:
    time.sleep(0.15)
    sys.stdout.write(char)
    sys.stdout.flush()
time.sleep(0.50)