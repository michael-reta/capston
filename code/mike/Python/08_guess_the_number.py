import random 

# version 1
guess_count = 0
guess_limit = 10
correct_number = random.randint(1,10)

while guess_count < guess_limit:
    guess = int(input('Guess an number bewteen 1-10:'))
    guess_count += 1
    if guess == correct_number:
        print('You guessed it! You Win!')
        break
    elif guess != correct_number:
        print('Incorrect! Guess again!')
        if guess_count == guess_limit:
            print ('Whomp whomp. Out of attempts!')

# version 2
while True:
    guess = int(input('Guess an number bewteen 1-10:'))
    guess_count += 1
    if guess == correct_number:
        print(f'Correct! You guessed {guess_count} times')
        break
    elif guess != correct_number:
        print('Incorrect! Guess again!')



# version 3
while True:
    guess = int(input('Guess an number bewteen 1-10:'))
    guess_count += 1
    if guess == correct_number:
        print(f'Correct! You guessed {guess_count} times')
        break
    elif guess > correct_number:
        print('Too high!')
    elif guess < correct_number:
        print('Too low!')