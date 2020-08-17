import random

number  = random.randint(1, 10)
player_name = input("Hey! What's your name? \n")
print('Aii ' + player_name + '. Your guess range is between 1 and 10. Leggoooo!\n')
number_of_guesses = 0
correct_answer = False

while number_of_guesses < 3:
    guess = int(input())
    number_of_guesses += 1
    if guess < number:
        print("Uhh. That's lower than the number. Try again")
    elif guess > number:
        print("Whew. That's higher than the number. Try again")
    else:
        print('Yo gotti!')
        correct_answer = True
        break

if not correct_answer:
    print("Oh! You've run out of guesses")
