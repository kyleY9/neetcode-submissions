class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        # Use dictionaries to count occurences
        # Go through each value in the dictionary, if any one of them is > 1, return True, otherwise return False
        # O(1) dictionary lookup

        my_dict = {}
        for n in nums:
            my_dict[n] = my_dict.get(n, 0) + 1
        
        for ct in my_dict.values():
            if ct != 1:
                return True
        return False