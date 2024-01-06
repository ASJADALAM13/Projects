import random
import time

board={1:"1",2:"2",3:"3",
       4:"4",5:"5",6:"6",
       7:"7",8:"8",9:"9"}

#function for Checking score at each step
def check_score(board,pce,chck):
    #for rows
    if chck.upper()=="R":
        i=1          
        while i<10:
            lstr=[]  
            for j in range(i,i+3):   
                if board[j]==pce:
                    lstr.append(True)   
                else:
                    lstr.append(False)
            if  all(lstr):   
                return True
            i=i+3    
    #For Columns
    if chck.upper()=="C":
        for i in range(1,4):
            lstc=[]
            for j in range(i,10,3):
                if board[j]==pce:
                    lstc.append(True)
                else:
                    lstc.append(False)
            if all(lstc):   
                return True
            
    #For Diagonals
    if chck.upper()=="D":
        lstd1=[]
        for i in range(1,10,4):
            if board[i]==pce:
                lstd1.append(True)
            else:
                lstd1.append(False)
        lstd2=[]    
        for j in range(3,8,2):
            if board[j]==pce:
                lstd2.append(True)
            else:
                lstd2.append(False)
        if all(lstd1):
            return True
        elif all(lstd2):
            return True
        else:
            return False
        
#For Printing the board with numbers on it representing position 
def display_board(board):
    l=len(board)
    for i in range(1,l+1):
        if i==4 or i==7:
            print("\n",end="-+-+-+-")
            print(" ")
        print(board[i],end="|")
    print("\n\n")

display_board(board) #function call  #Initialy Displaying Board

#function VS PLAYER
def _compete_with_player(board):
    for i in range(1,10):
        if i%2!=0:
            print("Player's One Turn(O)")
            pos=int(input("Enter-position:"))
            board[pos]="O"
            p1r=check_score(board,"O","R")
            p1c=check_score(board,"O","C")
            p1d=check_score(board,"O","D")
            if p1r or p1c or p1d:          #if any of them is True
                print("Player One Wins")
                break
        else:
            print("Player's Two Turn(X)")
            pos=int(input("Enter-position:"))
            board[pos]="X"
            p2r=check_score(board,"X","R")
            p2c=check_score(board,"X","C")
            p2d=check_score(board,"X","D")
            if p2r or p2c or p2d :
                print("Player Two Wins")   #if any of them is True
                break
        display_board(board)

#Function VS Computer
def _compete_with_AI(board):
    lst=[1,2,3,4,5,6,7,8,9]
    for i in range(1,10):
        if i%2!=0:
            print("It's Your Turn")
            pos=int(input("Enter-position:"))
            board[pos]="O"
            lst.remove(pos)
            p1r=check_score(board,"O","R")
            p1c=check_score(board,"O","C")
            p1d=check_score(board,"O","D")
            if p1r or p1c or p1d:          #if any of them is True
                print("Player One Wins")
                break
        else:
            print("It's My Turn wait!")
            time.sleep(2)
            ch=random.choice(lst)
            board[ch]="X"
            lst.remove(ch)
            A1r=check_score(board,"X","R")
            A1c=check_score(board,"X","C")
            A1d=check_score(board,"X","D")
            if A1r or A1c or A1d:
                print("Yippie,Computer Wins")
                break
        display_board(board)
    
ch=int(input("Choose- VS_Computer(1) OR VS_Player(2):"))
if ch==1:
    _compete_with_AI(board)
    display_board(board)

elif ch==2:
    _compete_with_player(board)
    display_board(board)
else:
    print("Invalid Entry")


















