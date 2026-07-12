class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        ans = ""

        s = min(len(st) for st in strs)

        for i in range(s):
            a = strs[0][i]

            for x in strs:
                if x[i] != a:
                    return ans

            ans += a

        return ans