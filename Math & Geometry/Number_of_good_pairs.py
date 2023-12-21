from collections import defaultdict
import math
class Solution:
    def numIdenticalPairs(self, nums):
        res = 0
        dic = defaultdict(int)
        for x in nums:
            dic[x] += 1
        for i in dic:
            if dic[i] > 1:
                res += math.comb(dic[i],2)
        return res
