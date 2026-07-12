class Solution:
    def romanToInt(self, s: str) -> int:
        sample = {'I': 1, 'V': 5, 'X':10, 'L':50, 'C': 100, 'D': 500, 'M': 1000}
        intt = 0
        for i in range(len(s)):
            if i < len(s) - 1 and sample[s[i]] < sample[s[i+1]]:
                intt -= sample[s[i]]
            else:
                intt += sample[s[i]]
        return intt