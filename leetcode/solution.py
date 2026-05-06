import collections
from typing import List

class Solution:
    def commonChars(self, words: List[str]) -> List[str]:
        cnt = collections.Counter(words[0])

        for word in words:
            curr_cnt = collections.Counter(word) 
            for char in cnt: 
                cnt[char] = min(cnt[char], curr_cnt[char])
        

        result = []
        for char in cnt: 
            for i in range(cnt[char]): 
                result.append(char)
        return result
        