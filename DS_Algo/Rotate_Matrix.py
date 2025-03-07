def rotate(matrix):
    # TODO
    
    n=len(matrix)
    for i in range(n):
        for j in range(i+1,n):
            tmp=matrix[j][i]
            matrix[j][i]=matrix[i][j]
            matrix[i][j]=tmp

    for i in range(n):
        for j in range(int(n/2)):
            tmp=matrix[i][n-j-1]
            matrix[i][n-j-1]=matrix[i][j]
            matrix[i][j]=tmp




def main():

    matrix = [[1,2,3],[4,5,6],[7,8,9]]
    n=len(matrix)


    rotate(matrix)

    for i in range(n):
        print(matrix[i])
            

if __name__ == '__main__':
    main()