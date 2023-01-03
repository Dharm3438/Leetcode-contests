class Solution:
    def minimumPartition(self, s: str, k: int) -> int:
        i = 0
        j = 0
        n = len(s)
        ct = 0
        while(j<n):
            if(int(s[i:j+1])<=k):
                j+=1
            else:
                ct+=1
                i = j
                if(i==j and int(s[i])>k):
                    return -1
        return ct+1