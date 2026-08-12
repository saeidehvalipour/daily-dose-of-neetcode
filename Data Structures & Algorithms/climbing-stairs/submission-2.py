class Solution:
    def climbStairs(self, n: int) -> int:
        memo ={}

        def dp(i):
            if i<= 2:
                return i

            if i in memo:
                return memo[i]

            memo[i]=dp(i-1) + dp(i-2)

            return memo[i]
        return dp(n)                
        # if n <= 2:
        #     return n
        
        # a, b = 1, 2
        
        # for _ in range(3, n + 1):
        #     a, b = b, a + b
        
        # return b

        