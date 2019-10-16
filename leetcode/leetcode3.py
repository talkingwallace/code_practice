"""
3. Longest Substring Without Repeating Characters
"""
class Solution:
    def lengthOfLongestSubstring(self, s):

        if len(s) == 0:
            return 0

        if len(s) == 1:
            return 1

        max_len = 0
        record = {}

        left,right = 0,0
        while right < len(s):

            if s[right] not in record:
                record[s[right]] = right

            elif s[right] in record and record[s[right]] >= left:
                left = record[s[right]] + 1
                record[s[right]] = right

            if right - left + 1 > max_len:
                max_len = right - left + 1

            right += 1

        return max_len


class Solution_:

    def lengthOfLongestSubstring(self, s):

        if len(s) == 0:
            return 0
        elif len(s) == 1:
            return 1

        record = [-1]*256
        left,right = 0,0
        max_len = 0
        while right < len(s):

            if record[ord(s[right])] == -1:
                record[ord(s[right])] = right

            else:
                left = record[ord(s[right])] + 1
                record[ord(s[right])] = right
                for i in range(len(record)):
                    if record[i] < left:
                        record[i] = -1

            if right - left + 1 > max_len:
                max_len = right - left + 1

            right += 1

        return max_len

print(Solution().lengthOfLongestSubstring("abcabcbb"))