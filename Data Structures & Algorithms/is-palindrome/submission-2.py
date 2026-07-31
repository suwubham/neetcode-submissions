class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()
        new_s = ""
        for letter in s:
            if letter.isalnum():
                new_s += letter
        return new_s == new_s[::-1]
        