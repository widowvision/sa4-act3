number = 10
guess = 0

print("I'm thinking of a number...\nPress 'q' to quit")
while(guess != 'q'):
    guess = input("What number am I thinking of? ")

    if guess == number:
        print("Congratulations! You guessed the right number.")
        break
    else: 
        print("Wrong guess!")
      

print(f"Sorry! The number was {number}")
