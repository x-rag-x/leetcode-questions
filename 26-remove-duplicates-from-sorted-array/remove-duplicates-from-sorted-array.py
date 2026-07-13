class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        srt = sorted(set(nums))

        for i in range(len(srt)):
            nums[i] = srt[i]

        return len(srt)