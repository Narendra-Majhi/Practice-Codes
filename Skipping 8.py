T = int(input())
c = 0
c1 = 1
for i in range(1,T):
    if("8" not in str(i)):
        print(i,end=" ")
        c = c+1
    if(c==8):
        print()
        c = 0
    if(i>=(10**c1)-1):
        print()
        c1 = c1+1
    
