def appendString(str1,str2):
    newStr=""
    len1=len(str1)
    for i in range (len1+1):
        if i < len1//2:
            newStr+=str1[i]
        elif i==len1//2:
            newStr+=str2
        else:
            newStr+=str1[i-1]
    return newStr

s1=input("Please input your first string ! ")
s2=input ("Please input your second string ! ")
if type(s1)!=type("a") or type(s2)!=type("a"):
    raise ValueError("Please input Strings.")

print(appendString(s1,s2))