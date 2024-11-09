class Solution:
    def romanToInt(self, s: str) -> int:
        s=str(s)
        roman=0
        i = len(str(s))-1
        while i>-1:
            print(s[i])
            if s[i]=="M":
                if i>0 and s[i-1]=="C":
                    roman+=900
                    i=i-1
                else:
                    roman+=1000
            elif s[i]=="D":
                if i>0 and s[i-1]=="C":
                    roman+=400
                    i=i-1
                else:
                    roman+=500                
            elif s[i]=="C":
                if i>0 and  s[i-1]=="X":
                    roman+=90
                    i=i-1
                else:
                    roman+=100                 
            elif s[i]=="L":
                if i>0 and s[i-1]=="X":
                    roman+=40
                    i=i-1
                else:
                    roman+=50  
            elif s[i]=="X":
                if i>0 and s[i-1]=="I":
                    roman+=9
                    i=i-1
                else:
                    roman+=10      
            elif s[i]=="V":
                if i>0 and s[i-1]=="I":
                    roman+=4
                    i=i-1
                else:
                    roman+=5                 
            elif s[i]=="I":
                roman+=1  
            i=i-1
        print(roman)
        return roman
a=Solution()
a.romanToInt("MCMXCIV")