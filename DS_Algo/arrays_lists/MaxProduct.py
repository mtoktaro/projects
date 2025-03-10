def max_product(arr):
    arr.sort()
    
    return arr[-1]*arr[-2]

def main():

    arr = [1, 7, 3, 4, 9, 1] 

    print(arr.count(1))
    print(arr[1:-1])
    print(max_product(arr))
    

if __name__ == '__main__':
    main()