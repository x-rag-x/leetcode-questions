class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        
        _a = str(x)
        a_ = str(x)[::-1]

        return _a == a_