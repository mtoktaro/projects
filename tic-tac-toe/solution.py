def check_final_move(count):
    if count==9:
        print('Draw')
        return 0

def update_matrix(matrix, x,y,ch, count, correct_move):

    if matrix[x][y]=='.' and x<3 and y<3:

        matrix[x][y]=ch
        count+=1
            
        for i in matrix:
            print(i)
        
        correct_move=True

    return count, correct_move

def check_bingo(matrix, x,y, ch):

    if matrix[x][0]==matrix[x][1]==matrix[x][2]==ch:
        return True

    if matrix[0][y]==matrix[1][y]==matrix[2][y]==ch:
        return True
    
    if matrix[0][0]==matrix[1][1]==matrix[2][2]==ch:
        return True
    if matrix[0][2]==matrix[1][1]==matrix[2][0]==ch:
        return True
    
    return False
def main():
    print('hello')
    move=False
    
    matrix=[['.']*3 for i in range(3)]
    count=0
    while move==False:

        correct_move=False
        while correct_move==False:

            p1=input("Player 1 enter your coordinates: ")

            p1=p1.split(' ')
            x=int(p1[0])
            y=int(p1[1])
            
            count, correct_move = update_matrix(matrix, x,y,'X', count,correct_move)
            
        check_final_move(count)
            
        if check_bingo(matrix,x,y,'X')==True:
            print('Player 1 won')
            move=True
            return 0
                
        
        correct_move=False
        
        while correct_move==False:
            p2=input("Player 2 enter your coordinates: ")
            p2=p2.split(' ')
            x=int(p2[0])
            y=int(p2[1])
            
            count, correct_move = update_matrix(matrix, x, y,'O', count, correct_move)
                

        check_final_move(count)
        if check_bingo(matrix,x,y,'O')==True:
            print('Player 2 won')
            move=True
        



if __name__ == '__main__':
    main()