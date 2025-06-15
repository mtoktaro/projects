class Solution:
    def getHint(self, secret: str, guess: str) -> str:
        n = len(secret)
        A = 0
        B = 0
        d_secret = {}
        d_guess = {}
        for i in range(n):
            d_secret[secret[i]] = d_secret.get(secret[i], 0) + 1
            d_guess[guess[i]] = d_guess.get(guess[i], 0) + 1

        # guess_ch = list(guess)
        # secret_ch = list(secret)

        for i in range(n):
            if secret[i] == guess[i]:
                A += 1
                d_guess[guess[i]] -= 1
                d_secret[secret[i]] -= 1
                # secret_ch[i] = 'x'
                # guess_ch[i] = 'x'

        for i in range(n):    
            if guess[i] != secret[i] and guess[i] in d_secret and d_secret[guess[i]] > 0:
                d_secret[guess[i]] -= 1
                B += 1
            
        return str(A)+ 'A'+str(B)+ 'B'