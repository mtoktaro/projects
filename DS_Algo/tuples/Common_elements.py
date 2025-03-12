def common_elements(tuple1, tuple2):
    # TODO
    
    ans=tuple()
    for i in tuple1:
        if i in tuple2:
            ans+=(i,)
            
    return ans



def main():
    


    tuple1 = (1, 2, 3, 4, 5)
    tuple2 = (4, 5, 6, 7, 8)

    


    
    print(common_elements(tuple1, tuple2))

if __name__ == '__main__':  
    main()
