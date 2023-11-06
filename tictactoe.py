import random
print("This is tic tac toe game , I'm assuming you know the rules already")
print("For the first person his sign is X and for the second person the sign is O")


def name():
    global player_names,x1,x2
    x1 = input("Enter first player name : ")
    x2 = input("Enter second player name : ")
    player_names = [x1,x2]

def choices():
    global Player_1, Player_2
    Player_1 = random.choice(player_names)
    if Player_1 == x1:
        global Player_2
        Player_2 = x2
    else:
        Player_2 = x1
    print(f"{Player_1} will go first")

global A
count_player_1 = 0
count_player_2 = 0
A = ["1","2","3","4","5","6","7","8","9"]
print(f"{A[0]}|{A[1]}|{A[2]}\n-----\n{A[3]}|{A[4]}|{A[5]}\n-----\n{A[6]}|{A[7]}|{A[8]}")
def game_on():
    while True:
        print(f"{Player_1} choose anyone in the pattern")
        input_1 = str(input("Enter the choice: "))
        for i in range(1,9):
            if str(i) == "X" or str(i) == "O":
                continue
            else:
                if input_1 == str(i):
                    A[int(i)-1] = "X"

        print(f"{Player_2} is your turn")
        input_2 = str(input("Enter your choice: "))
        for j in range(1,9):
            if str(j) == "X" or str(j) == "O":
                continue
            else:
                if input_2 == str(j):
                    A[int(j)-1] = "O"

        if (A[0]==A[1]==A[2] or A[0]==A[4]==A[8]or A[1]==A[3]==A[6]or A[2]==A[5]==A[8]or A[6]==A[7]==A[8]or A[1]==A[4]==A[7]or A[2]==A[4]==A[6]) == "X":
            print(f"{Player_1} won !!!")
            count_player_1+=1
        elif (A[0]==A[1]==A[2] or A[0]==A[4]==A[8]or A[1]==A[3]==A[6]or A[2]==A[5]==A[8]or A[6]==A[7]==A[8]or A[1]==A[4]==A[7]or A[2]==A[4]==A[6]) == "O":
            print(f"{Player_2} won !!!")
            count_player_2+=1

             

def Display():
    for i in range(9):
        if A[i]=="X" or A[i]=="O":
            continue
        else:
            A[i] = " "
    print(f"{A[0]}|{A[1]}|{A[2]}\n-----\n{A[3]}|{A[4]}|{A[5]}\n-----\n{A[6]}|{A[7]}|{A[8]}")
    print(f"{count_player_1}")
    print(f"{count_player_2}")
    
name()
choices()
game_on()
Display()        








    
