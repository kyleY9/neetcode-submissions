class Solution:
    # Thought Process
    # Maybe we can use some sort of dictionary here?
    # Build dictionary with index as key and number as value
    # Make a for loop, for each value in nums, subtract it from the target
    # Store the difference in a variable
    # Use the dictionary to lookup the difference, if it exists, take its key,
    # Otherwise keep on lookng
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        my_dict = {}
        for i in range(len(nums)):
            my_dict[i] = nums[i]
        
        for i in range(len(nums)):
            diff = target - nums[i]
            match = [key for (key, val) in my_dict.items() if val == diff and key > i]
            if len(match) >= 1:
                return [i, match[0]] 

        return []