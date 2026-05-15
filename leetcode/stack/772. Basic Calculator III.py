"""
    Problem i am given a string and i need to evaluate the string

    integers
    +,-,*,/ and "(" and ")"

    Division truncates toward zero
    Expression is valid
    No need to handle invalid input


    -------------------------------------

    process * and / immediately
    process + and - delayed
    handle what is in the brackets first


    14-3/2
    10-(2+3*2)


    10-(2+3*2)
    (2+3)*4
    ((2+3))


    res = 0
    curr = 2
    prev_sign = +


    stack1 = [10,"-"]
    stack2 = [2,6]

    when we see a bracket
    stack1 = stack1 + stack2[:]
    stack2 = []


    past_sign = stack1.pop()
    past_val = stack1.pop()
    prev = sum(stack2)
    stack2 = []
    stack2.append(past_val > past_sign > prev)



    (2+3)*4

    res=0
    curr=0
    prev_op = "+"
    stack1 = [0,+]
    stack2 = []
















"""

class Solution:
    def calculate(self, s: str) -> int:
        s = s.replace(" ", "")
        stack1 = []
        stack2 = []
        curr = 0
        last_op = "+"
        i = 0
        #[10,-]
        #10-(2+3*2)
        #(2+3)*4
        for d in s:
            if d.isdigit():
                curr *= 10
                curr += int(d)
            if d == "(":
                if(len(stack2) == 0 or (len(stack2) > 0 and str(stack2[-1]) in "+/-*")):
                    stack2.append(0)
                stack2.append(last_op)
                stack1.extend(stack2)
                stack2.clear()
                curr = 0
                last_op = "+"
            if d == ")":
                past_sign = stack1.pop()
                past_val = stack1.pop()
                c = sum(stack2)
                stack2.clear()
                if past_sign == "+":
                    past_val += c
                elif past_sign == "-":
                    past_val -= c
                elif past_sign == "*":
                    past_val *= c
                else:
                    past_val = int(past_val / c)
                stack2.append(past_val)
                curr = 0
                last_op = "+"
            if d in "+-/*" or (i == len(s)-1) or s[i+1] == ")":
                if curr != 0:
                    if last_op == "+":
                        stack2.append(curr * 1)
                    elif last_op == "-":
                        stack2.append(curr * -1)
                    elif last_op == "*":
                        stack2.append(stack2.pop() * curr)
                    else:
                        stack2.append(int(stack2.pop() / curr))
                curr = 0
                if d in "+/-*":
                    last_op = d
            i += 1
        l = sum(stack2)
        return l



if __name__ == "__main__":
    sol = Solution()
    tests = [
        # Basic operations
        ("1+1", 2),
        ("2-1", 1),
        ("2*3", 6),
        ("8/4", 2),

        # Mixed precedence
        ("3+2*2", 7),
        (" 3/2 ", 1),
        (" 3+5 / 2 ", 5),
        ("14-3/2", 13),

        # Parentheses basics
        ("(1+1)", 2),
        ("2*(1+1)", 4),
        ("(2+3)*4", 20),

        # Nested parentheses
        ("((2+3))", 5),
        ("2*(3+(4-1))", 12),

        # Complex mixes
        ("(1+(4+5+2)-3)+(6+8)", 23),
        ("(2+3)*(5-2)", 15),
        ("10-(2+3*2)", 2),

        # Division edge cases (truncate toward zero)
        ("-3/2", -1),
        ("14/3", 4),
        ("-14/3", -4),

        # Harder mixes
        ("(8+2*5)/(1+3*2-4)", 6),
        ("(6-4)/(1+1)", 1),
        ("2*(5+5*2)/3+(6/2+8)", 21),
    ]

    for expr, expected in tests:
        result = sol.calculate(expr)
        print(f"{expr} = {result} | expected = {expected} | {'PASS' if result == expected else 'FAIL'}")
