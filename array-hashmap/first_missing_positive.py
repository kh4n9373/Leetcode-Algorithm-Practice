class Solution:
    def firstMissingPositive(self, nums) -> int:
        # 1 hour, beat the hard one !!
        
        # Key Intuitive : if a value in the array is not in range [1,n], then it CANT NOT BE THE RESULT.
        # After proving the above Key Intuitive, I just considered the value in range [1,n] locating in the array
        # If the value in range [1,n], it means we can map that value to the identical index in the array right ?
        # So call the value I'm considering in each iteration is A,
        # And the value in the identical-to-A index in array is B,
        # Because A has been in array, so A can not be the result 
        # so I changed B to float (hashing), indicating that A has been in the array
        # If B is in range [1,n] and I consider it in another iteration, I only need to recover it to int by + 0.5, so it doesnt have any bad effect to the value B if it might be considered
        # Starting the result from 0, if the result already in the array (checking by the index array[result] float or int), gradually increment it by 1
        # Until we find the result value that not in the array, return the result + 1
        # time : O(n), space : O(1)

        n = len(nums)
        for num in nums:
            if type(num) == float:
                consider_num = int(num + 0.5) # recover the initial value
            elif type(num) == int:
                consider_num = num
            if consider_num <= n and consider_num > 0:
                if type(nums[consider_num-1]) == int: 
                    # hash the identical index to another value to identify that value has been existing in the array
                    nums[consider_num-1] = nums[consider_num-1] - 0.5 
        res = 0
        while res < n and type(nums[res]) == float:
            res += 1
        return res+1
        
                

        