class Solution():
    def lengthOfLongestSubstring(self, s):

        print(s)
        max=0
        
        for i, char in enumerate(s):
            #print(f'char at position {i} is : {char}')
            all=[]
            all.append(char)
            for y in range(i+1,len(s)):
                if(s[y] not in all):
                    all.append(s[y])
                else:
                    break
            if len(all)>max:
                max=len(all)
            print(all)
        return max
                
                
                

            
s="  "
solution=Solution()
result = solution.lengthOfLongestSubstring(s)
print(result)