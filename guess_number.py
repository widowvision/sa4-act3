number = 10
guess = 0
val = 'a'

print("I'm thinking of a number...\nPress 'q' to quit")
while(val != 'q'):
    guess = int(input("What number am I thinking of? "))

    if guess == number:
        print("Congratulations! You guessed the right number.")
        break
    elif guess < number:
        print("Too low!")
        val = input("Press q to quit or any key to continue ")
    elif guess > number:
        print("Too high!")
        val = input("Press q to quit or any key to continue ")
    else: 
        print("Wrong guess! Press q to quit, or any key to continue ")
        val = input()
      

print(f"Sorry! The number was {number}")
