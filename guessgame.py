import random
 
rand = random.randint(1,100)

guesses = [0]
print("WELCOME TO 'GUESS THE NUMBER!'")
print("I'm thinking of a number between 1 and 100")
print("If your guess is more than 10 away from my number, I'll tell you you're COLD")
print("If your guess is within 10 of my number, I'll tell youyou're WARM")
print("If your guess is farther than your most recent guess, I'll say you're getting COLDER")
print("If your guess is closer than your most recent guess, I'll say you're getting WARMER")
print("LET'S PLAY!")
print(int(rand))
while True:
    guess = int(input('Guess the number: '))

    if guess == int(rand):
        print("Your choice is correct")
        break

    elif guess + 10 < int(rand):
        print("COLD")

    elif guess-10 > int(rand) :
        print("You're WARM")

    
