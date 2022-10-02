# УГАДАЙКА ЧИСЕЛ
import random
import sys
from time import *

# an invitation to play
sleep(1.5)
print("HELLO, THIS IS ONE OF THE MOST SIMPLE BUT FUN OLD GAMES.")
sleep(1.2)
print("AND I INVITE YOU TO PLAY!")
sleep(1)
print("ARE YOU INTERESTED?")
sleep(1)
print()


# game rules
def game_rules():
    print('GREAT, YOU NEED TO GUESS THE NUMBER FROM "1" TO "100".')
    sleep(1.5)
    print('YOU HAVE "7" ATTEMPT.')
    sleep(1.3)
    print('WELL, THIS IS EVERYTHING!)')
    sleep(1)
    print()


# response check
if input('PRINT "YES" OR "NO": ').lower() in ["yes", "+", 'y']:
    print()
    sleep(0.6)
    game_rules()
else:
    sleep(1)
    print("WELL, SEE YOU LATER!")
    sleep(0.6)
    sys.exit()


# checking for number
def it_is_number(num):
    if num.isdigit():
        return int(num)
    else:
        print("INCORRECT, PLEASE ENTER A NUMBER.", "TRY AGAIN.", sep="\n")
        sleep(0.6)
        return it_is_number(input(f'{name} ENTER YOUR NUMBER: '))


# start the game
def start_game():
    num = random.randint(1, 100)
    counter = 0
    number_of_attempts = 7
    play_again = True
    while play_again:
        user_num = it_is_number(str(input(f'{name} ENTER YOUR NUMBER: ')))
        sleep(0.5)
        if 1 <= user_num <= 100:
            counter += 1
            if number_of_attempts == 0:
                print(f'THE ATTEMPTS ENDED. THE HIDDEN NUMBER IS "{num}"')
                sleep(0.7)
                print()
                break
            if user_num > num:
                number_of_attempts -= 1
                print("TOO MUCH, TRY AGAIN.")
                sleep(0.3)
            elif user_num < num:
                number_of_attempts -= 1
                print("TOO LITTLE, TRY AGAIN.")
                sleep(0.3)
            else:
                print(f'GREAT, YOU GUESSED IT!!! THIS NUMBER IS "{num}".')
                sleep(0.7)
                print()
                print(f'NUMBER OF ATTEMPTS IS "{counter}".')
                sleep(1.0)
                print("HOLD THE MEDAL!")
                sleep(0.7)
                print("       *")
                print("(о°∨°)╯╯")
                print()
                sleep(1.5)
                break
        else:
            print("YOU DIDN'T ENTER A NUMBER FROM THE SPECIFIED RANGE")
            sleep(1.0)
            continue


print(">>>GUESS THE NUMBER!<<<")
sleep(0.7)
name = input("HI, WHAT'S YOUR NAME? ").upper()
sleep(0.9)
print(f'NICE TO MEET YOU {name}. WE START!')
sleep(1)
print()
start_game()
again = True
while again:
    print("SHOULD WE PLAY AGAIN? ")
    play_again = input('PRINT "YES" OR "NO": ')
    sleep(0.65)
    if play_again.lower() in ["yes", "+", "y"]:
        play_again = True
        start_game()
    else:
        sleep(0.7)
        print(f'{name},THANKS FOR PLAYING!')
        sleep(0.7)
        print("WELL, SEE YOU LATER")
        break