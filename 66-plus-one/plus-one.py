class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        _str = '' 
        for x in digits:
            _str += str(x)
        
        return list(map(int, (str(int(_str) + 1))))