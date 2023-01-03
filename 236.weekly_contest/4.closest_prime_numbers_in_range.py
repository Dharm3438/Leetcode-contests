class Solution:
    
    def seive(self,left,n):
        store = [True]*(n+1)
        store[0] = False
        store[1] = False
        for i in range(2,int(math.ceil(math.sqrt(n+1)))):
            if(store[i]==True):
                j = 2
                while(i*j<=n):
                    store[i*j]=False
                    j+=1
        
        primes = []
        # print(store)
        for i in range(len(store)):
            if(store[i]==True and i>=left):
                primes.append(i)
        return primes
            
    def closestPrimes(self, left: int, right: int) -> List[int]:
        
        ans = self.seive(left,right)
        # print(ans)
        mini = 1E9
        if(len(ans)<2):
            return [-1,-1]
        else:
            for i in range(len(ans)-1):
                if(ans[i+1]-ans[i]<mini):
                    mini = ans[i+1] - ans[i]
                    tmp = [ans[i], ans[i+1]]
            return tmp