#printing prime numbers from 0 to 100
b=[];
for i in range(0,100):
    if i > 1: 
        for x in range(2,i):
            if (i % x) == 0: 
                break
        else: 
            b.append(i)
print(b)
  