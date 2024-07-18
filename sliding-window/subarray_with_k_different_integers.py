
def subarraysWithKDistinct(nums, k):
    # # Keep track of 3 pointers : cd (chan duoi), ct (chan tren), r 
    # r = 0
    # res = 0
    # cnt = 0
    # for r in range(len(nums)):
    #     if save.get(nums[r],0) == 0:
    #         cnt += 1
    #     print(cnt)
    #     save[nums[r]] = save.get(nums[r],0) + 1
    #     if cnt < k: 
    #         continue
    #     else:
    #         temp = cnt
    #         save1 = save.copy()
    #         cd, ct = 0, r
    #         while temp > k:
    #             for i in range(r+1):
    #                 save1[nums[i]] -= 1
    #                 if save1[nums[i]] == 0:
    #                     temp -= 1
    #                     cd = i + 1
    #                     break
    #         while temp == k:
    #             for i in range(cd,r+1):
    #                 save1[nums[i]] -= 1
    #                 if save1[nums[i]] == 0:
    #                     temp -= 1
    #                     ct = i + 1
    #                     break
    #         print(cd,ct)
    #         res += (ct - cd)
    # return res
    save = {}
    res = 0 
    cd,ct = 0,0 
    for r in range(len(nums)):
        save[nums[r]] = save.get(nums[r],0) + 1

        while len(save) > k:
            save[nums[ct]] -= 1
            if save[nums[ct]] == 0:
                save.pop(nums[ct])
            ct += 1
            cd = ct
        while save[nums[ct]] > 1:
            save[nums[ct]] -= 1
            ct += 1
        
        if len(save) == k:
            res += (ct - cd + 1)
    return res
nums = [2,1,1,1,2]
k = 1
print(subarraysWithKDistinct(nums,k))