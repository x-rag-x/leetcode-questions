class Solution:
    def reverseBits(self, n: int) -> int:
        _n = format(n, "032b")
        n_rev = _n[::-1]

        return int(n_rev, 2)