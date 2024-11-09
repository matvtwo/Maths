from typing import List
import array as arr
class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        count = len(digits)-1
        number=0
        digits[count]=int(digits[count])+1
        i=count
        while i >= 0:
            print(f"{i}a)element is = {digits[i]}")
            if(int(digits[i])>=10 and i!=0):
                digits[i]=int(digits[i])-10#
                digits[i-1]=int(digits[i-1])+1#перенос дестяка
            elif (int(digits[i])>=10 and i==0):
                digits[i]=int(digits[i])-10#
                digits=[1]+digits
            print(f"{i}b)element is = {digits[i]}")
            i=i-1
        return digits

a=Solution()
print(a.plusOne([8,9,9,9,9,9,9,9,9,9]))