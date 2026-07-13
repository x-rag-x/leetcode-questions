class Solution:
    def addBinary(self, a: str, b: str) -> str:
        _a = int(a, 2)
        _b = int(b, 2)
        _c = _a + _b

        c = bin(_c)[2:]

        return c