class Solution:
    def haveConflict(self, event1: List[str], event2: List[str]) -> bool:
        start1 = event1[0].split(':')
        end1 = event1[1].split(':')
        start2 = event2[0].split(':')
        end2 = event2[1].split(':')
        start1[0] = int(start1[0])
        start1[1] = int(start1[1])
        start2[0] = int(start2[0])
        start2[1] = int(start2[1])
        end1[0] = int(end1[0])
        end1[1] = int(end1[1])
        end2[0] = int(end2[0])
        end2[1] = int(end2[1])
        
        fg = False
        if(start2[0]<start1[0] and end2[0]>end1[0]):
            fg = True
        
        if((start2[0]>=start1[0] and start2[0]<=end1[0]) or (end2[0]>=start1[0] and end2[0]<=end1[0])):
            fg = True
            if(start2[0]==end1[0]):
                #check Minitues
                if(start2[1]>end1[1]):
                    fg = False
                else:
                    fg = True
                
            
        
        
        
        return fg