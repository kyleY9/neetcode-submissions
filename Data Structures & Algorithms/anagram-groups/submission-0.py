class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # Bro this is so hard
        # Sort the letters! 

        my_dict = {}
        if strs:
            for string in strs:
                str_sorted = "".join(sorted(string))
                if str_sorted not in my_dict:
                        my_dict[str_sorted] = [string]
                else:
                    my_dict[str_sorted].append(string)
            return [val for val in my_dict.values()]
        return [['']]

