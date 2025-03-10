
def highest_value(dict1):
    # TODO
    my_dict={}
    
    
    
    return(sorted(dict1.items(), key=lambda item:item[1])[-1][0])


    



def main():
    dict1 = {'a': 1, 'b': 2, 'd':10, 'c': 3}
    dict2 = {'b': 3, 'c': 4, 'd': 5}

    


    print(highest_value(dict1))

if __name__ == '__main__':
    main()