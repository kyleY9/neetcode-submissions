class Solution:

    # Thought process
    # Create two dictionaries, one for s and one for t
    # Use a for loop to store each letter as a key and its occurences as a value
    # Use another for loop afterwards to see if the dictionaries match (can use == for equality)
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) == len(t): # Anagram strings must be of the same length
            s_dict = {}
            t_dict = {}
            for i in range(len(s)):
                s_char = s[i]
                t_char = t[i]
                s_dict[s_char] = s_dict.get(s_char, 0) + 1
                t_dict[t_char] = t_dict.get(t_char, 0) + 1

            return s_dict == t_dict
        return False

        