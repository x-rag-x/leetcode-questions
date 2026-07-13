class Solution:
    def sequentialDigits(self, low: int, high: int) -> List[int]:
        digits = '123456789'
        otpt = []
        l, h = len(str(low)), len(str(high))

        for i in range(l, h + 1):
            for j in range(10 - i):
                pair = int(digits[j:j + i])
                if low <= pair <= high:
                   otpt.append(pair)
        return otpt