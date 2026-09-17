class Solution:
    def getFinalState(self, nums: List[int], k: int,
                      multiplier: int) -> List[int]:

        for _ in range(k):
            smallest = min(nums)
            index = nums.index(smallest)
            nums[index] *= multiplier

        return nums