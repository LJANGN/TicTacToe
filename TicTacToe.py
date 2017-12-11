import random
#the basis of the actual board is a <list> 
board = ["   " for i in range (9)] 
#you print the board inserting the formatted items with their positions 
# i.e. 0-8 from the list  

print("Instructions: The spots on the table are numbered as follows: ")
print()
print("| 1 | 2 | 3 |")
print("--------------" )
print("| 4 | 5 | 6 |")
print("--------------" )
print("| 7 | 8 | 9 |")
print()
print('--------------------------------------')
print()
print("Let's play!")
def print_board():
    row1 = "|{}|{}|{}|".format(board[0],board[1],board[2])
    row2 = "--------------" 
    row3 = "|{}|{}|{}|".format(board[3],board[4],board[5]) 
    row4 = "--------------" 
    row5 = "|{}|{}|{}|".format(board[6],board[7],board[8])
    print() 
    print(row1) 
    print(row2) 
    print(row3) 
    print(row4) 
    print(row5) 
    print() 
   
def player_move(icon):
    #icon = input("Type in X or 0: ").lower()
    if icon == " X ": #spaces added to put it in the middle of the column on board
        number =1 
    elif icon == " O ":
        number =2 
    print("Your move player {}".format(number)) 
    #if number == 2:
            #print("Computer is player 2")
            
     
#choice needs to be described as int() 
    choice = int(input("Enter your move: ").strip()) 
    if board[choice-1]=="   ":
        board[choice-1]= icon 
    else:
        print() #exra row added for clarity 
        print("That spot is taken!")
        choice = int(input("Enter your move: ").strip()) ##!f spot taken same player to try again
    if board[choice-1]=="   ":
        board[choice-1]= icon
    
        

"""
def computer_move(icon):
    if icon == " X ": #spaces added to put it in the middle of the column on board
        number =2 
    elif icon == " O ":
        number =1 
    print("Computer inserts {}".format(number))     
    
#trying to add simple AI...:
    compChoice = random.randint(1,9) 
    if board[compChoice-1]=="   ":
        board[compChoice-1]= icon
""" 
        
def is_victory(icon):
    if (board[0]==icon and board[1]==icon and board[2]==icon) or \
    (board[3]==icon and board[4]==icon and board[5]==icon) or \
    (board[6]==icon and board[7]==icon and board[8]==icon) or \
    (board[0]==icon and board[3]==icon and board[6]==icon) or \
    (board[1]==icon and board[4]==icon and board[7]==icon) or \
    (board[2]==icon and board[5]==icon and board[8]==icon) or \
    (board[0]==icon and board[4]==icon and board[8]==icon) or \
    (board[2]==icon and board[4]==icon and board[6]==icon): 
    
        return True
    else:
        return False 
 
def is_draw(): 
    if "  " in board:
        return True 
    else:
        return False 

#while True is a "game loop" telling the game keeps on running for now 
#board printed in each loop with the added input, i.e. choice 
while True:
    print_board()
    player_move(" X ") 
    print_board() 
    if is_victory (" X "):
        print("X wins! Congratulations")
        break
    elif is_draw():
        print("It's a draw")
        break
    player_move(" O ")
    if is_victory (" O "): 
        print_board() 
        print("O wins! Congratulations") 
        break
    elif is_draw(): 
        print("It's a draw") 
        break 



