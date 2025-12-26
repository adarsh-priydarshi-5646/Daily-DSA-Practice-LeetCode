class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        s = 0
        a = 1
        while n > 0:
            r = n % 10
            s += r
            a *= r
            n = n // 10
        # print(r)
        # print(a)
        return a - s
        