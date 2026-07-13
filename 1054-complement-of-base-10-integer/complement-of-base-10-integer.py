class Solution:
    def bitwiseComplement(self, n: int) -> int:
        _n = str(bin(n)[2:])
        a = _n.replace('1', '2')
        b = a.replace('0', '1')
        c = b.replace('2', '0')

        return int(c, 2)