import random, time

def display_board(board):
    # The function accepts one parameter containing the board's current status
    # and prints it out to the console.
    print("+-------+-------+-------+")
    print("|       |       |       |")
    for i in (board[0:3]):
        print("|  ",i,"  ",end="")
    print("|")
    print("|       |       |       |")
    print("+-------+-------+-------+")
    print("|       |       |       |")
    for i in (board[3:6]):
        print("|  ",i,"  ",end="")
    print("|")
    print("|       |       |       |")
    print("+-------+-------+-------+")
    print("|       |       |       |")
    for i in (board[6:9]):
        print("|  ",i,"  ",end="")
    print("|")
    print("|       |       |       |")
    print("+-------+-------+-------+")

def enter_move(board):
    # The function accepts the board current status, asks the user about their move, 
    # checks the input and updates the board according to the user's decision.
    move = input("Enter your move : ")
    #print(move, board)
    while move not in board :
        move = input("Wrong entry. Enter your move : ")
    board = board[:board.index(move)] + ("O",) + board[board.index(move)+1:]
    return board

def make_list_of_free_fields(board):
    # The function browses the board and builds a list of all the free squares; 
    # the list consists of tuples, while each tuple is a pair of row and column numbers.
    global end
    end = False
    free_fields = []
    for i in board:
        if i not in ("X","O"):
            x = board.index(i)%3 +1
            y = board.index(i)//3 +1
            free_fields.append((x,y))
    if len(free_fields) == 0:
        end = True
        print("End with a tie...")
    victory_for(board)

def victory_for(board):
    # The function analyzes the board status in order to check if 
    # the player using 'O's or 'X's has won the game
    global end
    end = False
    X_fields = []
    counter = -1
    for i in board:
        counter += 1
        if i == "X":
            x = str(counter%3 +1)
            y = str(counter//3 +1)
            if (x,y) not in X_fields:
                X_fields.append((x+y))
    O_fields = []
    counter = -1
    for i in board:
        counter += 1
        if i == "O":
            x = str(counter%3 +1)
            y = str(counter//3 +1)
            if (x,y) not in O_fields:
                O_fields.append((x+y))

    if set(['11','12','13']).issubset(X_fields) or set(['21','22','23']).issubset(X_fields) \
        or set(['31','32','33']).issubset(X_fields) or set(['11','21','31']).issubset(X_fields) \
            or set(['12','22','32']).issubset(X_fields) or set(['13','23','33']).issubset(X_fields) \
                or set(['11','22','33']).issubset(X_fields) or set(['31','22','13']).issubset(X_fields):
        end = True
        print("Computer wins!")
    if set(['11','12','13']).issubset(O_fields) or set(['21','22','23']).issubset(O_fields) \
        or set(['31','32','33']).issubset(O_fields) or set(['11','21','31']).issubset(O_fields) \
            or set(['12','22','32']).issubset(O_fields) or set(['13','23','33']).issubset(O_fields) \
                or set(['11','22','33']).issubset(O_fields) or set(['31','22','13']).issubset(O_fields):
        end = True
        print("YOU WIN!!!")

def draw_move(board):
    # The function draws the computer's move and updates the board.
    choice_list = ()
    for i in board:
        if i not in ("X","O"):
            choice_list += (i,)
    choice = random.choice(choice_list)
    board = board[:board.index(choice)] + ("X",) + board[board.index(choice)+1:]
    return board

board = ("1","2","3","4","X","6","7","8","9")
display_board(board)
end = False

while end == False:
    board = enter_move(board)
    display_board(board)
    make_list_of_free_fields(board)
    print("Computer's turn -")
    time.sleep(2)
    board = draw_move(board)
    display_board(board)
    make_list_of_free_fields(board)
