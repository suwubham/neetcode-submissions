class Solution:
    def isValid(self, s: str) -> bool:
        hashmap = {
            "(":")",
            "[":"]",
            "{": "}"
        }
        stack = []
        for i in s:
            if i in hashmap:
                stack.append(i)
            else:
                if not stack or (hashmap.get(stack.pop()) != i):
                    return False
        return len(stack) == 0


        