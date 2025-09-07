import math
board=[' ',' ',' ',' ',' ',' ',' ',' ',' ']
def clear():
    global board
    board = [' ' for _ in range(9)]

def print_board():
    for i in range(0,9,3):
        print(f' {board[i]}| {board[i+1]}| {board[i+2]}|')

def is_ful(board):
    for i in range(9):
        if(board[i]==' '):
            return False
    else:
        return True

def is_winned(board,player):
    conditions=[[0,1,2],[3,4,5],[6,7,8],
                [0,3,6],[1,4,7],[2,5,8],
                [0,4,8],[2,4,6]
                ]

    for i in conditions:
        if board[i[0]] == board[i[1]]==board[i[2]]==player:
            return True
    return False

def usermove():
    move=int(input("Enter 1 to 9 :"))-1
    if(board[move]==' '):
        board[move]="X"
        print_board()
    else:
         print("Envalid move")
         usermove()


def minmax(board,ai_move,deft):
    if(is_winned(board, 'O')):
        return 10-deft
    elif(is_winned(board, 'X')):
        return -10+deft
    elif(is_ful(board)):
        return 0
    if ai_move:
        best_score=-2
        for i in range(9):
            if(board[i]==' '):
                board[i]="O"
                score=minmax(board,False,deft+1)
                board[i]=" "
                if(score>=best_score):
                    best_score=score

        return best_score      
    else:
        best_score=2
        for i in range(9):
            if(board[i]==' '):
                board[i]="X"
                score=minmax(board,True,deft+1)
                board[i]=" "
                if(score<=best_score):
                    best_score=score

        return best_score      

def best_move_ai(board):
    move=0
    best_score=-2

    for i in range(9):
        if(board[i]==' '):
           board[i]="O"
           score=minmax(board,False,0)
           board[i]=" "
           if(score>=best_score):
               best_score=score
               move=i
    return move




def main():
    userscore=0
    aiscore=0
    while True:
        print("ai score is",aiscore)
        print("user score is",userscore)
        clear()
        a=input("'exit' for brak and 1 for start you 2 for ai :=> ")
        print("welcome  .. ")
        print("User X and ai O ")
        if(a=='1'):
            while True:
                print_board()    
                usermove()
                if(is_ful(board)):
                    print("tie .. !")
                    break
                if(is_winned(board, 'X')):
                    print("You Win!..")
                    userscore+=1
                    break
                print("Ai thinking...")
                move=best_move_ai(board)
                board[move]="O"

                if(is_ful(board)):
                    print("tie .. !")
                    clear()
                    break
                if(is_winned(board, 'O')):
                    print_board()
                    print("AI Win!..")
                    aiscore+=1
                    clear()
                    break
        if(a=='2'):
            while True:

                print("Ai thinking...")
                move=best_move_ai(board)
                board[move]="O"
                print_board()  
                if(is_ful(board)):
                    print("tie .. !")
                    clear()
                    break
                if(is_winned(board, 'O')):
                    #print_board()
                    print("AI Win!..")
                    aiscore+=1
                    clear()
                    break
                usermove()
                if(is_ful(board)):
                    print("tie .. !")
                    break
                if(is_winned(board, 'X')):
                    print("You Win!..")
                    userscore+=1
                    break

        elif(a=='exit'):
            print("Thank for useing")
            break

main()    
