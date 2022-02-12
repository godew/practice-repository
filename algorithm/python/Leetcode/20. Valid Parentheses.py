class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for c in s:
            if c in ("(","[","{"):
                stack.append(c)

            else:
                if not stack:
                    return False
                else:
                    if stack[-1] == "(":
                        if c == ")":
                            stack.pop()
                        else:
                            return False

                    elif stack[-1] == "[":
                        if c == "]":
                            stack.pop()
                        else:
                            return False
                    else:
                        if c == "}":
                            stack.pop()
                        else:
                            return False
        if stack:
            return False
        else:
            return True


