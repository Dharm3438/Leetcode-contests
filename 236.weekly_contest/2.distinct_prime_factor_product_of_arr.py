class Solution:
    def distinctPrimeFactors(self, nums: List[int]) -> int:
        primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31]
        ans = set()
        for val in nums:
            for p in primes:
                if(val%p==0):
                    ans.add(p)
                    while(val%p==0):
                        val/=p
            if(val!=1):
                ans.add(val)
        
        return len(ans)
        