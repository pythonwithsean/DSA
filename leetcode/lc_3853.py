class Solution:
    def mergeCharacters(self, s: str, k: int) -> str:

        N = len(s)

        stack = []
        s = list(s)

        for char in s:
            if not stack:
                stack.append(char)
                continue
            ok = True
            for i in range(max(0,len(stack)-k),len(stack)):
                if stack[i] == char:
                    ok = False
                    break
            if ok:
                stack.append(char)
        return "".join(stack)


"""
    Intution we merge chars within a certain range of k
    so basically we look back at what we have in the stack to check
    if we have the charcter k steps back if we do we skip that character in constant time
    else we add it because its more then k steps away from the next character
"""
