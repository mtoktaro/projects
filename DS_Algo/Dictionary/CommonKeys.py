
def merge_dicts(dict1, dict2):
    # TODO
    my_dict={}
    
    my_dict = dict1.copy()
    
    for k,v in dict2.items():
        if k in my_dict:
            my_dict[k]+=dict2[k]
        else:
            my_dict[k]=dict2[k]


    return my_dict
    


    



def main():
    dict1 = {'a': 1, 'b': 2, 'c': 3}
    dict2 = {'b': 3, 'c': 4, 'd': 5}

    


    print(merge_dicts(dict1, dict2))

if __name__ == '__main__':
    main()