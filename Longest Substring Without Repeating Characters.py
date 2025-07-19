# Sliding Window is used.
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        dup = set()
        left = 0
        max_length = 0

        for right in range (len(s)):
            while s[right] in dup:
                dup.remove(s[left])
                left += 1
            dup.add(s[right])
            max_length = max(max_length, right - left + 1) 
        return max_length
