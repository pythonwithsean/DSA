from collections import Counter
import math

class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        ex = Counter("ballon")
        c = Counter(text)
        single_one_freq = math.inf
        for char in ["a","b","n"]:
            single_one_freq = min(single_one_freq,c[char])
        double_char_freq = math.inf
        for char in ["l","o"]:
            double_char_freq = min(double_char_freq, c[char])
        double_char_freq = double_char_freq // 2
        if single_one_freq == 0 or double_char_freq == 0:
            return 0
        return min(single_one_freq, double_char_freq)
