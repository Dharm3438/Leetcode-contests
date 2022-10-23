from math import gcd
class Solution:
    def subarrayGCD(self, nums: List[int], k: int) -> int:
        n = len(nums)
        ct=0
        for i in range(n):
            g = 0
            for j in range(i,n):
                g = gcd(g,nums[j])
                if(g==k):
                    ct+=1
                    # print(nums[i:j+1])
        
        return ct