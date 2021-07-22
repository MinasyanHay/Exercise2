def func(str1):
    if(len(str1)<7):
        raise ValueError ("Please input longer string than 7")
    elif(len(str1)%2==0):
        raise ValueError("Your length of string must be even!!!")
    elif type(str1)!=str:
        raise ValueError("Please input string")
    else:
        newStr=""
        for i in range((len(str1)//2)-1,(len(str1)//2)+2):
            newStr += str1[i]
        
    return newStr
    

str1="aaaBBBaaa"
print(func(str1))