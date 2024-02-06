from random import randint

ATTEMPTS = 10
LOWER_BOUND = 1
UPPER_BOUND = 10000

secret_number = randint(LOWER_BOUND, UPPER_BOUND)
print(f"A secret number between {LOWER_BOUND} and {UPPER_BOUND} has been generated!\n"
      f"Try to guess in {ATTEMPTS} attempts!!")

attempts_left = ATTEMPTS
guess = 0
while attempts_left > 0:
    print("---------------------------------------")
    print(f"Attempts left: {attempts_left}")
    guess = int(input("Your guess: "))
    if guess == secret_number:
        print("CONGRATULATIONS!!\nYOU'VE GUESSED THE SECRET NUMBER!!")
        break
    if guess > secret_number:
        print("LESS!!")
    else:
        print("GREATER!!")
    attempts_left -= 1
else:
    print(f"No attempts left...\nThe secret number was {secret_number}")
