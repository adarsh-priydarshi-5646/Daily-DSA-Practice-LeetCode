class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        r = 0
        a = 1
        c = 0
        while n > 0:
            r += n % 10
            a *= n % 10
            n = n // 10
        # print(r)
        # print(a)
        return a - r
        