class Solution:
    """
    @param coins: a list of integer
    @param amount: a total amount of money amount
    @return: the fewest number of coins that you need to make up
    """
    def coinChange(self, coins, amount):
        # write your code here
        f= [sys.maxsize]*(amount+1)
        f[0]= 0
<<<<<<< HEAD
        
	for coin in coins:
       	    for i in range(1, amount+1):
=======
  
        for coin in coins:
            for i in range(1, amount+1):
>>>>>>> 1a021df35ed43dda49ffc79c3c085944b2a05160
                if coin< amount:
                    f[i]= min(f[i], f[i-coin]+1)
        
        return f[amount] if f[amount]!= sys.maxsize else -1
