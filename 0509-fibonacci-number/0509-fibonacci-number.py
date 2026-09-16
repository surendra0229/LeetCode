class Solution:
    def fib(self, n: int) -> int:
        def fn(n):
            if n==1:
                return 1
            elif n==0:
                return 0
            return fn(n-1)+fn(n-2)
        ans = fn(n)
        return ans