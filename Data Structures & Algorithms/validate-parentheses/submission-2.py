class Solution:
    def isValid(self, s: str) -> bool:
        stack_ = []

        for p in list(s):
            if p == "{" or p == "(" or p == "[":
                stack_.append(p)

            elif p == "}" and stack_ and stack_[-1] == "{":
                stack_.pop()
            elif p == ")" and stack_ and stack_[-1] == "(":
                stack_.pop()
            elif p == "]" and stack_ and stack_[-1] == "[":
                stack_.pop()
            else: 
                return False

        return not stack_
