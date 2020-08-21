from random import randint
import sys

# Run command: python3 first number second number
# ex: python3 1 10 guessing game is set from range of 1 through 10

# Generate a number
num1 = sys.argv[1]
num2 = sys.argv[2]
answer = randint(int(num1), int(num2))


# Check that input is a number 1 -10
while True:
    try:
        # input from user
        guess = int(input(f'Guess a number from {num1} through {num2}: '))
        if 0 < guess < int(num2):
            if guess == answer:
                print('You guessed right!')
                break
            elif guess < answer:
                print('Try guessing higher.')
            else:
                print('Try guessing lower.')
        else:
            print(f'Between {num1} and {num2}, please.')
    # handle error is a string is entered
    except ValueError:
        print('Please enter a number!')
