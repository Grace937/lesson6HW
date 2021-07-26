s=[86,'a',98,'b',69,'c',84,'d',93,'e']
a=0
b=0
for i in range(0,10,2):
    if a<=(s[i]):
        a=(s[i])
        b=(s[i+1])
print(b,a)