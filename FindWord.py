print("Guess the word")
a="mush"
c=[]
for i in range(0,len(a)):
    print("_",end=" ")
for j in range(0,len(a)):
    b=input("\nenter a character ")
    c.append(b)
if(c==list(a)):
    print("\nGot it")
else:
    print("\nIncorrect!! try again")
        