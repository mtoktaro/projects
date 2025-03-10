def pair_sum(myList, sum):
    # TODO
    
    s=set()
    for i in myList:
        s.add(i)
        
        
    ans=[]
    for i in range(len(myList)):
        for j in range(i, len(myList)):
            if (myList[i]+myList[j])==sum:
                ans.append(f'{myList[i]}+{myList[j]}')   
            
    return ans 

def main():

    arr = [2, 4, 3, 5, 6, -2, 4, 7, 8, 9] 
    
    print(pair_sum(arr,7))
    

if __name__ == '__main__':
    main()