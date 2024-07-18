from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs):
        # dic = {
        #     'a': 0, 'b': 1, 'c': 2, 'd': 3, 'e': 4, 'f': 5,
        #     'g': 6, 'h': 7, 'i': 8, 'j': 9, 'k': 10, 'l': 11,
        #     'm': 12, 'n': 13, 'o': 14, 'p': 15, 'q': 16, 'r': 17,
        #     's': 18, 't': 19, 'u': 20, 'v': 21, 'w': 22, 'x': 23,
        #     'y': 24, 'z': 25
        # }
        # hashmap = defaultdict(list)
        # for i in strs:
        #     count = [0]*26
        #     for j in i:
        #         count[dic[j]- dic['a']] += 1
        #     hashmap[tuple(count)].append(i)
        # return hashmap.values()
        
        dic = defaultdict(list)
        for s in strs:
            dic[tuple(sorted(s))].append(s)
        return dic.values()





                