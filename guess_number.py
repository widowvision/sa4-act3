number = 10
guess = 0
chances = 3

print("I'm thinking of a number...\nPress 'q' to quit")
while(guess != 'q' and chances > 0):
    guess = input("What number am I thinking of? ")

    if guess == number:
        print("Congratulations! You guessed the right number.")
        break
    else: 
        print("Wrong guess!")
        chances = chances - 1
      

print(f"Sorry! The number was {number}")
