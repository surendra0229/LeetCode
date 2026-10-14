class Solution:
    def reverse(self, x: int) -> int:
        num = abs(x)
        rev = 0
        min_value = -(2**31)
        max_value = 2**31 - 1
        while num > 0:
            digit = num % 10
            rev = rev * 10 + digit
            num = num // 10

        if x < 0:
            rev = -rev
        if rev < min_value or rev > max_value:
            return 0

        return rev
