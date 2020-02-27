str=raw_input("Enter your string : ")
res=""
n=len(str)
for x in range(0,n):
    res=res+str[n-x-1]
print(res)
