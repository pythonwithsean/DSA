"""
Key Observation:

A monotone increasing binary string has the form:

    000000111111

At every position we only care about one thing:

    Have we already started the "1" section?

This becomes our DP state.

dp(i, seen_ones)

i          -> current index
seen_ones  -> whether we have already committed to the 1-section

If seen_ones == True:
    Every future character must be 1.

    Current char = 0:
        Must flip it to 1.
        Cost = 1 + dp(i + 1, True)

    Current char = 1:
        Keep it.
        Cost = dp(i + 1, True)

If seen_ones == False:
    We are still in the 0-section.

    Current char = 0:
        Option 1:
            Keep as 0 and remain in 0-section.

        Option 2:
            Flip to 1 and start the 1-section.

    Current char = 1:
        Option 1:
            Flip to 0 and remain in 0-section.

        Option 2:
            Keep as 1 and start the 1-section.

The answer is the minimum cost among all valid choices.

Why this works:

The only information from the past that affects future decisions is
whether we have already started placing 1s. Once the 1-section begins,
we can never place another 0 without performing a flip.

Time:  O(n)
Space: O(2*n)
"""

class Solution:
    def minFlipsMonoIncr(self, s: str) -> int:
        N = len(s)
        memo = {}
        def dp(i,seen_ones):
            if (i,seen_ones) in memo:
                return memo[(i,seen_ones)]
            if i == N:
                return 0
            # increasing now
            if seen_ones and s[i] == "0":
                memo[(i,seen_ones)] = 1 + dp(i + 1, seen_ones) # slip to 1
            elif seen_ones and s[i] == "1":
                memo[(i,seen_ones)] = dp(i + 1, seen_ones)
            elif not seen_ones and s[i] == "0":
                memo[(i,seen_ones)] = min(1 + dp(i + 1, seen_ones=True), dp(i + 1, seen_ones))
            else:
                memo[(i,seen_ones)] = min(1 + dp(i+1, seen_ones), dp(i + 1, seen_ones=True))
            return memo[(i,seen_ones)]

        return dp(0,False)
