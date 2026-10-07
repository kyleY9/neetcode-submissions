class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # Bucket sort solution
        # Create dictionary with key => num and value => # occurences of that num
        # Create an array r with n + 1 subarrays for our buckets
        # Loop through the items in our dictionary
        # Match each occurence count to its corresponding array index: append key to array at the index
        # Loop through r in reverse and add numbers from subarrays to a return array until its length is k

        d = {}
        for n in nums:
            d[n] = d.get(n, 0) + 1

        r = [[] for _ in range(len(nums) + 1)]
        for num, v in d.items():
            r[v].append(num)
        
        answer_arr = []
        for i in range(len(nums), 0, -1):
            for x in r[i]:
                answer_arr.append(x)
                if len(answer_arr) == k:
                    return answer_arr
