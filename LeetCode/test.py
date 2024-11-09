s="IX"
roman=0
i = len(str(s))-1
while i>-1:
    print(f"i:{i} s[{i}]={s[i]}")
    if s[i]=="X":
        if s[i-1]=="I":
            roman+=9
            i=i-1
            print("111111111")
        else:
            roman+=10        
    elif s[i]=="I":
        roman+=1  
    i=i-1
print(roman)