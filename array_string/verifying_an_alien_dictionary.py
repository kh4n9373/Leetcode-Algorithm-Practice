class Solution:
    def isAlienSorted(self, words, order: str) -> bool:
        dic = {c:i for i,c in enumerate(order)}
        for i in range(len(words)-1):
            w1, w2 = words[i],words[i+1]
            for j in range(len(w1)):
                if j == len(w2): 
                    return False
                if w1[j] != w2[j]:
                    if dic[w1[j]] > dic[w2[j]]:
                        return False
                    break
        return True