class Solution:
    def reverse(self, x: int) -> int:
        result = 0
        sign = 1
        min_value = -(2**31)
        max_value = 2**31 - 1
        if x < 0:
            sign = -1
            x = -x
        while x != 0:
            last_digit = x % 10
            result = result * 10 + last_digit
            x = x // 10
        result = result * sign

        if result < min_value or result > max_value:
            return 0

        return result