count=0
a,b,c=map(int,input().split())
for k in range(a,b+1):
    if c%k==0:
        count+=1
print(count)
