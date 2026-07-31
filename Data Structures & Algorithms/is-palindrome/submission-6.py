class Solution:
    def isPalindrome(self, s: str) -> bool:
        left, right = 0, len(s) - 1
        while left < right:
            if s[left].isalnum():
                if s[right].isalnum():
                    if s[left].lower() != s[right].lower():
                        return False
                else:
                    right -= 1
                    continue
            else:
                left += 1
                continue
            left += 1
            right -= 1
        return True
        