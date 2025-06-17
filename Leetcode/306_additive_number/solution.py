# 1. use 2 for loops to get different combos of 1st & 2nd numbers
# 2. while loop till end of string 
# 3. for each combo add the next digits together until the number is = num1+num2
# 4. if int(digits_added) > combo: break
# 5. if loop reaches the end return True

class Solution:
    def isAdditiveNumber(self, num: str) -> bool:

        n = len(num)
        if n < 3:
            return False
        
        if num[0] == '0':
            n_num1 = 1
        else:
            n_num1 = n // 2

        for i in range(n_num1 ):
            num1 = int(num[ : i + 1])
            if num[i + 1] == '0': 
                m = i + 2
            else:
                m = (n // 3) * 2
            
            for j in range(i + 1, m):
                num2 = int(num[i + 1 : j + 1])
                
                
               
                k = j + 1
                num3 = '-1'
                seq1 = num1
                seq2 = num2
                while k < n :
                    if num[k] == '0'  and num1 + num2 != 0:
                        break
                    num3 = ''
                    
                    while k < n:
                        num3 += num[k]
                        k += 1
                        if int(num3) >= (seq1 + seq2):
                            break
                    
                    print(num3)
                    
                    if int(num3) != (seq1 + seq2):
                        
                        # print(seq1, ' ', seq2)
                        break
                    elif k < n:
                        seq1 = seq2
                        seq2 = int(num3)
                        num3 = '-1'
                    
                
                if int(num3) == (seq1 + seq2) and k == n:
                    return True
        

        return False
                
        