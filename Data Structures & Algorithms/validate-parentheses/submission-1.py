class Solution:
    def isValid(self, s: str) -> bool:
        arr = []
        mapping = {')': '(', ']': '[', '}': '{'}

        for char in s:
            if char in "([{":
                arr.append(char)
            else:
                if not arr:
                    return False
                top = arr.pop()
                if mapping[char] != top:  # Fixed this line
                    return False

        return not arr