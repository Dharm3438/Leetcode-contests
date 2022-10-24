class Solution:
    def decodeMessage(self, key: str, message: str) -> str:
        val=97
        store = dict()
        for i in key:
            if i==" ":
                pass
            elif i in store:
                pass
            else:
                store[i] = chr(val)
                val+=1
            
        ans=""
        for i in message:
            
            if i==" ":
                ans+=" "
            elif i in store:
                ans+=store[i]
        
        # print(store)
        print(ans)
        return ans