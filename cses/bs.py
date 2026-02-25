def maxAs(n):
    operations = ["A", "c-C", "c-V"]
    best = [0]
    best_string = [""]
    #3,3,2 ->
    n = 3
    [0,0,0,0,0,0,0]
            #  A
            # /  \
            # A   A
            # /    \
            #A

    # T(b) -> T()
    def sol(n,A,copy):
        if n <= 0:
            best[0] = max(best[0], len(A))
            if len(A) > len(best_string[0]):
                best_string[0] = "".join(A)
            return
        for op in operations:
            if op == "A":
                # Add an A
                sol(n - 1,A + ["A"],copy)
            elif op == "c-C":
                # Select and Copy
                sol(n - 2,A,copy + len(A))
            else:
                #  increment A by copies
                sol(n - 1,A + ["A" for i in range(copy)],copy)
    sol(n,[],0)
    print(best_string[0])
    return best[0]
print(maxAs(7))
