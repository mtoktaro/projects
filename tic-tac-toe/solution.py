def main():
    print('hello')
    move=False
    
    matrix=[['.']*3 for i in range(3)]
    count=0
    while move==False:
        p1=input("enter your coordinate: ")
        p1=p1.split(' ')
        matrix[int(p1[0])][int(p1[1])]='X'
        count+=1
        
        for i in matrix:
            print(i)
            
        if count==9:
            print('Draw')
            return 0

        

        p2=input("enter your coordinate: ")
        p2=p2.split(' ')
        matrix[int(p2[0])][int(p2[1])]='O'
        count+=1

        for i in matrix:
            print(i)
        
        
        return 0    



if __name__ == '__main__':
    main()