def main():
    print('hello')
    move=False
    
    matrix=[['.']*3 for i in range(3)]

    while move==False:
        p1=input("enter your coordinate: ")
        p1=p1.split(' ')
        matrix[int(p1[0])][int(p1[1])]='X'
        
        for i in matrix:
            print(i)

        p2=input("enter your coordinate: ")
        p2=p2.split(' ')
        matrix[int(p2[0])][int(p2[1])]='O'

        for i in matrix:
            print(i)
        
        return 0    



if __name__ == '__main__':
    main()