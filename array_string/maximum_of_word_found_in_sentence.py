class Solution:
    def mostWordsFound(self, sentences) -> int:
        res = 0
        for sentence in sentences:
            res = max(res,len(sentence.split()))
        return res