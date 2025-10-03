#Function to print the board
def print_board(board):
    for row in board:
        print(" ".join(row))
    print()
#check if its safe to place queen
def is_safe(board,row,col,n):
        #check column
    for i in range(row):
        if board[i][col]=='Q':
            return False
            
        #check upper-left diagnol
    i,j=row,col
    while i>=0 and j>=0:#within the top row i,
            #within the left most column j
        if board[i][j]=='Q':
            return False
        i-=1
        j-=1
    i,j=row,col
    while i>=0 and j>=n:#within the top row i,
            #within the left most column j
        if board[i][j]=='Q':
            return False
        i-=1
        j+=1
    return True
#Backtracking function
def solve_queens(board,row,n):
    if row==n:
        print_board(board)
        return True #Return true if one solution is enough
    for col in range(n):
        if is_safe(board,row,col,n):
            board[row][col]='Q'#place queen
            if solve_queens(board,row+1,n):
                #Recur to next row
                return True
            board[row][col]='.'#Backtrack (remove queen)
    return False
#Main function
def four_queens():
    n=4
    board=[['.'for _ in range(n)]for _ in range(n)]
    #_ IS THROWBACK VARIABLE
    if not solve_queens(board,0,n):
        print("No Solution found")
        #Run the program
four_queens()
