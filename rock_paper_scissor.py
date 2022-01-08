#emojis may not work on all terminals!
from termcolor import colored
import random
import time
import os
import colorama
def who_won():
    sum1 = sum(point_table1)
    sum2 = sum(point_table2)
    print('Player Score: ',point_table1)
    print()
    print('Computer Score: ',point_table2)
    print()
    if sum1 > sum2:
        print("Player Won This Game!")
    elif sum1 < sum2:
        print("Computer Won This Game!")
    elif sum1 == sum2:
        print('This is a draw match!')
def clear():
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')
    colorama.init()
    print(colored('                                                                     ********************* ROCK , PAPER & SCISSORS ********************                                                                                        ','yellow'))
    print()
    print()
    string = "There will be three tries. you will be asked to enter your choice 3 times. Please enter the choice as instructed inside the brackets, as this game depends on those specific characters, plz... :)"
    string2 = string.upper()
    string3 = 'Rock(Enter as "R" or "r") , Paper (Enter as "P" or "p"), Scissors (Enter as "S" or "s")'
    print(colored(string2,'green'))
    print()
    print()
    print(colored('+----------------------------------------------------------------------------------------------------------------+','red'))
    print(colored('| INSTRUCTIONS:                                                                                                  |','red'))
    print(colored('|                                                                                                                |','red'))
    print(colored('|Rock(Enter as "R" or "r") , Paper (Enter as "P" or "p"), Scissors (Enter as "S" or "s")                         |','red'))
    print(colored('|                                                                                                                |','red'))
    print(colored('|2 points will be awarded to the winner of a round. In case of draw,1 point will be awarded to both the parties. |','red'))
    print(colored('|                                                                                                                |','red'))
    print(colored('|At the end, player with maximum number of points wins!                                                          |','red'))
    print(colored('+----------------------------------------------------------------------------------------------------------------+','red')) 
    print()
    print()
    colorama.deinit()
colorama.init()
print(colored('                                                                     ********************* ROCK , PAPER & SCISSORS ********************                                                                                        ','yellow'))
print()
print()
string = "There will be three tries. you will be asked to enter your choice 3 times. Please enter the choice as instructed inside the brackets, as this game depends on those specific characters, plz... :)"
string2 = string.upper()
string3 = 'Rock(Enter as "R" or "r") , Paper (Enter as "P" or "p"), Scissors (Enter as "S" or "s")'
print(colored(string2,'green'))
print()
print()
print(colored('+----------------------------------------------------------------------------------------------------------------+','red'))
print(colored('| INSTRUCTIONS:                                                                                                  |','red'))
print(colored('|                                                                                                                |','red'))
print(colored('|Rock(Enter as "R" or "r") , Paper (Enter as "P" or "p"), Scissors (Enter as "S" or "s")                         |','red'))
print(colored('|                                                                                                                |','red'))
print(colored('|2 points will be awarded to the winner of a round. In case of draw,1 point will be awarded to both the parties. |','red'))
print(colored('|                                                                                                                |','red'))
print(colored('|At the end, player with maximum number of points wins!                                                          |','red'))
print(colored('+----------------------------------------------------------------------------------------------------------------+','red')) 
print()
print()
colorama.deinit()
time.sleep(2)

while True:
    point_table1 = [] #for player
    point_table2 = [] #for computer
    for i in range(1,4):
        choice = input('                              ROCK,PAPER OR SCISSORS? : ')
        comp_choice = random.randint(1,3)
        if comp_choice == 1:
            comp = 'r'
        elif comp_choice == 2:
            comp = 'p'
        elif comp_choice == 3:
            comp = 's'
        if choice == 'r' or choice == 'R':
            if comp == 'r':
                print("                              Draw! \U0001F91D")
                print()
                point_table1.append(1)
                point_table2.append(1)
            elif comp == 'p':
                print('                              \U0000270A    ROCK!')
                print('                              \U0001F91A    PAPER!')
                print('                              Computer Wins! \U0001F91A')
                print()
                point_table1.append(0)
                point_table2.append(2)
            elif comp == 's':
                print('                              \U0000270A    ROCK!')
                print('                              \U0000270C    SCISSORS!')
                print('                              You Win! \U0000270A')
                print()
                point_table1.append(2)
                point_table2.append(0)
        elif choice == 'p' or choice == 'P':
            if comp == 'p':
                print("                              Draw! \U0001F91D")
                print()
                point_table1.append(1)
                point_table2.append(1)
            elif comp == 'r':
                print('                              \U0001F91A   PAPER!') #paper - user
                print('                              \U0000270A   ROCK!') #rock - comp
                print('                              You Win! \U0001F91A')
                print()
                point_table1.append(2)
                point_table2.append(0)
            elif comp == 's':
                print('                              \U0001F91A    PAPER!') #paper -user
                print('                              \U0000270C    SCISSORS!') #sciss - comp
                print('                              Computer Wins! \U0000270C')
                print()
                point_table1.append(0)
                point_table2.append(2)
        elif choice == 's' or choice == 'S':
            if comp == 's':
                print("                              Draw! \U0001F91D")
                print()
                point_table1.append(1)
                point_table2.append(1)
            elif comp == 'r':
                print('                              \U0000270C   SCISSORS!') #scissor - user
                print('                              \U0000270A   ROCK!') #rock - comp
                print('                              Computer Wins! \U0000270A')
                print()
                point_table1.append(0)
                point_table2.append(2)
            elif comp == 'p':
                print('                              \U0000270C   SCISSORS!') #scissor -user
                print('                              \U0001F91A   PAPER!') #paper - comp
                print('                              You Win! \U0000270C')
                print()
                point_table1.append(2)
                point_table2.append(0)
        else:
            colorama.init()
            print(colored('      FOLLOW THE INSTRUCTIONS!!!!!','red'),'\U0001F624')
            colorama.deinit()
            break
        i+=1
    if choice == 'R' or choice == 'r' or choice == 'p' or choice == 'P' or choice == 's' or choice == 'S':
        who_won()   
    print()
    print()
    cont = input('Do you want to play again? (reply in "y" or "n" only): ')
    if cont == 'y' or cont == 'Y':
        clear()
        continue
    elif cont == 'n' or cont == 'N':
        print('Bye! \U0001F44B')
        time.sleep(1)
        break
    else:
        colorama.init()
        print(colored('INVALID ENTRY!\nFATAL ERROR \U00002620','red'))
        colorama.deinit()
        time.sleep(1)
        break
              
