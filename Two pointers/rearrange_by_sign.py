class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        # If we have to modify nums
        # def find(pointer):
        #     for i in range(pointer+1,len(nums)):
        #         if nums[pointer]*nums[i] > 0:
        #             return i
        # p,n = 0,0
        # if nums[p] < 0:
        #     n = p
        #     p += 1
        #     while p < len(nums)//2:
        #         if nums[p] < 0:
        #             p += 1
        #         else:
        #             break

        # else:
        #     n += 1
        #     while n < len(nums)//2:
        #         if nums[n] > 0:
        #             n += 1
        #         else:
        #             break
        # def execute(p,n):
        #     cur = 0
        #     while cur < len(nums):

        #         if cur%2 == 0:
        #             if nums[cur] > 0:
        #                 p = find(p)
        #             else:
        #                 stay = p
        #                 p = find(p)
        #                 cache = nums[stay]
        #                 for temp in range(stay,cur,-1):
        #                     nums[temp] = nums[temp-1]
        #                 nums[cur] = cache
        #                 if n in range(cur,stay):
        #                     n += 1

        #         elif cur%2 != 0:
        #             if nums[cur] < 0:
        #                 n = find(n)
        #             else:
        #                 stay = n
        #                 n = find(n)
        #                 cache = nums[stay]
        #                 for temp in range(stay,cur,-1):
        #                     nums[temp] = nums[temp-1]
        #                 nums[cur] = cache
        #                 if p in range(cur,stay):
        #                     p += 1
        #         cur += 1
        # execute(p,n)
        # return nums
        
        i,j = 0,1
        res = [0]*len(nums)
        for k in range(len(nums)):
            if nums[k] > 0:
                res[i] = nums[k]
                i += 2
            elif nums[k] < 0:
                res[j] = nums[k]
                j += 2
        return res

            
            
        