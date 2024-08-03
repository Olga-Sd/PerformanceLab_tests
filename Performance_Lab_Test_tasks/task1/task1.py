import sys

n = int(sys.argv[1])
m = int(sys.argv[2])
#n,m  = map(int, input().split())

step = m-1

if m > n:
    i = m%n
else:
    i = m
ans = '1' 

while  i != 1:
    ans = ans + str(i)
    i = i +step
    #print(ans,i)
    if i>n:
       i = i % n
       if i == 0:
           i = n
       #print(ans,i)
print(ans)  
