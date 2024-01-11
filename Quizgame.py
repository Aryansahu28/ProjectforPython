import random
def question():
    global points
    points = 0
    print("Who is the President of Bharat?")
    ans1 = input("Your Answer :- ")
    if ans1 == 'Draupati Murmu':
        print("Your answer is correct")
        points=+1
    else:
        print("Incorrect!")

    print("Who is the Prime Minister of India?")
    ans2 = input("Your Answer :- ")
    if ans2 == 'Narendra Modi':
        print("Your answer is correct")
        points=+1
    else:
        print("Incorrect!")

    print("Who is the External Affair Minister of India?")
    ans3 = input("Your Answer :- ")
    if ans3 == 'Dr. S. Jaishankar':
        print("Your answer is correct")
        points=+1
    else:
        print("Incorrect!")
    
    print("Who is the National Bird of India?")
    ans4 = input("Your Answer :- ")
    if ans4 == 'Peacock':
        print("Your answer is correct")
        points=+1
    else:
        print("Incorrect!")

    print("Who is the king khan?")
    ans5 = input("Your Answer :- ")
    if ans5 == 'Shahrukh Khan':
        print("Your answer is correct")
        points=+1
    else:
        print("Incorrect!")

ask_to_play = input("If you want to play enter Yes : ")
if ask_to_play == 'Yes' or 'yes':
    question()
    print(f"Your total points is {points} out of 5")
else:
    print("I'm looking forward for next time")
