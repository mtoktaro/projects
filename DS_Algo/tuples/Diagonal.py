
def get_diagonal(tup):
    # TODO
    ans=tuple()
    for i in range(len(tup)):
        ans+=(tup[i][i],)
            
    return ans
    



def main():
    


    input_tuple = (
    (1, 2, 3),
    (4, 5, 6),
    (7, 8, 9)
    )

    


    
    print(get_diagonal(input_tuple))

if __name__ == '__main__':  
    main()
