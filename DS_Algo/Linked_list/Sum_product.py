
def sum_product(input_tuple):
    # TODO
    sum=0
    prod=1
    for i in input_tuple:
        sum+=i
        prod*=i
        
        
    return sum, prod

    



def main():
    


    input_tuple = (1, 2, 3, 4)

    


    sum_result, product_result = sum_product(input_tuple)
    print(sum_result, product_result)

if __name__ == '__main__':  
    main()
