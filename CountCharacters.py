"""Method 1
a=input()
b=len(a)
count=0
for i in a:
    if(i=="i" or i=="I"):
        count+=1
print("number of i is",count)
print("length of input is",b) """
#Method 2
a=input()
count=0
b=0
for i in a:
    count+=1
    if(i=="i" or i=="I"):
        b+=1
print("number of i is",b)
print("length of input is",count)

    
    