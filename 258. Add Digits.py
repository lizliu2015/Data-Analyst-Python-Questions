class Solution:
    def addDigits(self, num: int) -> int:
        n = 0
        while len(str(num)) > 1:
            for i in str(num):
                n = n + int(i)
            num = n
            n = 0  #reset n
        return num
