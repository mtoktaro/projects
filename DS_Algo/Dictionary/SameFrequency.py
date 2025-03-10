def check_same_frequency(list1, list2):
    # TODO
    d1={}
    d2={}
    for i in list1:
        d1[i]=d1.get(i,0)+1
    
    for i in list2:
        d2[i]=d2.get(i,0)+1
    
    if d1==d2:
        return True
    else:
        return False
    



def main():
    


    list1 = [1, 2, 3, 2, 1]
    list2 = [3, 1, 2, 1, 3]

    


    print(check_same_frequency(list1, list2))

if __name__ == '__main__':
    main()
