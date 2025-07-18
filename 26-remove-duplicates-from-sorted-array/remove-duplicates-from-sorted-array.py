class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        unique_numbers = set()
        for num in nums:
            unique_numbers.add(num)
    
        sorted_arrays = sorted(unique_numbers)
        nums[:] = sorted_arrays 
        return len(unique_numbers)
