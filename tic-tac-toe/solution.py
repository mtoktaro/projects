def check(matrix, x,y, ch):

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
        p1=input("Player 1 enter your coordinates: ")
        p1=p1.split(' ')
        x=int(p1[0])
        y=int(p1[1])
        matrix[x][y]='X'
        count+=1
        
        for i in matrix:
            print(i)

        if count==9:
            print('Draw')
            return 0
        else: 
            
                
            if check(matrix,x,y,'X')==True:
                print('Player 1 won')
                return 0
                
            

        p2=input("Player 2 enter your coordinates: ")
        p2=p2.split(' ')
        x=int(p1[0])
        y=int(p1[1])
        matrix[x][y]='O'
        count+=1

        for i in matrix:
            print(i)
        
        if check(matrix,x,y,'X')==True:
            print('Player 1 won')
        return 0    



if __name__ == '__main__':
    main()