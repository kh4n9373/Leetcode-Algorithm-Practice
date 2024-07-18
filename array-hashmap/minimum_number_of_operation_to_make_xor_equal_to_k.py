from typing import List 
def minOperations(nums: List[int], k: int) -> int:
    total_xor = 0 
    for n in nums:
        total_xor = total_xor^n
    
    count = 0
    while k != total_xor:
        if k%2 != total_xor%2:
            count += 1
        k = k // 2 # take out the final bit
        total_xor = total_xor // 2 # take out the final bit
    return count 
    