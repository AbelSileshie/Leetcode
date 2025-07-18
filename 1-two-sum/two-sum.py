class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        indexed_nums = [(num, index) for index, num in enumerate(nums)]
        indexed_nums.sort(key=lambda x: x[0])  # Sort based on the number
        
        left, right = 0, len(indexed_nums) - 1
        
        while left < right:
            current_sum = indexed_nums[left][0] + indexed_nums[right][0]
            if current_sum == target:
                return [indexed_nums[left][1], indexed_nums[right][1]]
            elif current_sum < target:
                left += 1
            else:
                right -= 1
        