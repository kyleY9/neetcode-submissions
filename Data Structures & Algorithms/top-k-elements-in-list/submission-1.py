class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # Make a dictionary where key => number and value => # of occurences
        # Take each (key, value) from the dictionary as a tuple and sort them by value. Put the result in a list
        # Take the first k keys and return them as a list

        d = {}
        for n in nums:
            d[n] = d.get(n, 0) + 1

        l = list(d.items())
        l.sort(key=lambda t: t[1], reverse=True) # Sort by num occurences
        return [x[0] for x in l[:k]]