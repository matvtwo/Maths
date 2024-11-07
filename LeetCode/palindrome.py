class Solution:
    def isPalindrome(self, x: int) -> bool:
        y=x
        x2=""
        for i in range (len(str(x))):
            x2+=str(y%10)
            y=int(y/10)
        return x==x2
a=Solution()
a.isPalindrome(1221)
print(1221)