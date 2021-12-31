import random

def add2(c):
    return( c + 1)
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

if __name__ == '__main__':
    guess(2)
