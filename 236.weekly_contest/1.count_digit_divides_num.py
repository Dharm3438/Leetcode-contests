class Solution:
    def countDigits(self, num: int) -> int:
        tmp = num
        rem = 0
        store = dict()
        while(num):
            rem = num%10
            if(rem in store):
                store[rem]+=1
            else:
                store[rem]=1
            num = num//10
        
        
        factors = []
        for i in range(1,10):
            if(tmp%i==0):
                factors.append(i)
        
        
        ct = 0
        for val in factors:
            if(val in store):
                ct+=store[val]
        
        print(store)
        print(factors)
        
        return ct
        