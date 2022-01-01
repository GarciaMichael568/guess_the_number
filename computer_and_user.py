import random

def guess(x):
    random_number = random.randint(1,x)
    guess = 0
    while guess != random_number:
        guess = int(input(f"Guess a number between 1 and {x}: "))
        if guess < random_number:
            print(":( guess again. Too low.")
        elif guess > random_number:
            print(":| guess again. Too high.")
        
    print(f"WINNER WINNER CHICKEN DINNER! You have guessed the\
 number {random_number}.")

def computer_guess(x):
    low = 1
    high = x
    feedback = ''
    while feedback != 'c':
        if low != high:
            guess = random.randint(low,high)
        else:
            guess = low
        feedback = input(f'Is {guess} too high (H), too low (L), or correct (C)? ').lower()
        if feedback == 'h':
            high = guess - 1
        if feedback == 'l':
            low = guess + 1
    
    print(f'Processing...your number is {guess}')
        
if __name__ == '__main__':
    print('Welcome Gamer!')
    game_mode = int(input('Press 1: User guess, Press 2: Computer guess: '))
    if game_mode == 1:
        x = int(input('Enter Max number (above 1): '))
        guess(x)
    elif game_mode == 2:
        x = int(input('Enter Max Number (above 1): '))
        computer_guess(x)
