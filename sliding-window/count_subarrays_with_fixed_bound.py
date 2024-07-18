class Solution:
    def countSubarrays(self, nums: List[int], minK: int, maxK: int) -> int:
        # res = 0
        # consider = []
        # l,r = 0,0
        # while r < len(nums):
        #     if nums[r] < minK or nums[r] > maxK:
        #         consider.append(nums[l:r])
        #         l,r = r+1,r+1 
        #     if r == len(nums) - 1:
        #         consider.append(nums[l:])
        #         break
        #     else:
        #         r += 1
        # def find(cand, minK, maxK):
        #     if not minK in cand and maxK in cand:
        #         return 0
        #     res = 0
        #     dq = deque()  
        #     n = len(cand)  
        #     for i in range(n):
        #         dq.append(i)
        #         while dq and cand[dq[0]] < minK:
        #             dq.popleft()
        #         while dq and cand[dq[-1]] > maxK:
        #             dq.pop()
        #         if dq and (minK <= cand[i] <= maxK or cand[i] in (minK, maxK)):
        #             for j in range(dq[0], i + 1):
        #                 if minK in nums[j:i + 1] and maxK in cand[j:i + 1]: 
        #                     res += 1
        #     return res
        # for can in consider:
        #     res += find(can, minK, maxK)
        # return res
                
        res = 0
        imin = imax = ibad = -1
        for i,n in enumerate(nums):
            if not minK <= n <= maxK: ibad = i
            if n == minK: imin = i
            if n == maxK: imax = i
            # this function is > 0 if and only if both imax > ibad and imin > ibad
            # and both >= 0 indicating a valid subarray
            res += max(0, min(imin, imax) - ibad) 
        return res