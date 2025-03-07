def missing_number(arr,n):
    
    for i in range(len(arr)-1):
        if (arr[i+1]-arr[i])>1:
            return(arr[i]+1)
        
    return('Nothing')





def main():

    print(missing_number([1,2,3,4,6],6))

if __name__ == '__main__':
    main()