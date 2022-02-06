class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        stack = []
        for i in range(len(s)):
            if not stack:
                stack.append(s[i])
                continue

            if s[i] in stack:
                continue

            while stack:
                if stack[-1] >= s[i]:
                    if s[i:].count(stack[-1]) != 0:
                        stack.pop()
                    else:
                        break
                else:
                    break

            stack.append(s[i])
        return "".join(stack)
    



