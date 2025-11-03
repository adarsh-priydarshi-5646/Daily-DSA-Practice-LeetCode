class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        n = len(s)
        seen = set()          # Set to store unique characters in current window
        left = 0              # Left pointer of the window
        max_len = 0           # Final answer

        for curr_ele in range(n):
            # Agar character repeat hai toh left ko aage badhao aur set se remove karo
            while s[curr_ele] in seen:
                seen.remove(s[left])
                left += 1

            # Unique character mil gaya, add karo
            seen.add(s[curr_ele])

            # Window ka size check karo
            max_len = max(max_len, curr_ele - left + 1)

        return max_len
        