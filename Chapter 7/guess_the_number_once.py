import random
secret_number = random.randint(1, 10)
print("I am thinking of a number between 1 and 10.")
guess = int(input("Can you guess it? "))
if guess == secret_number:
    print("You got it!")
elif guess < secret_number:
    print("Your guess is too low.")
else:
    print("Your guess is too high.")
