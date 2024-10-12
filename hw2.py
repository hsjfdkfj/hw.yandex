n=int(input())
pi=float(3.141592653589793)
sum=float(0)
for i in range(1,n+1):
 sum+=1/pow(i,2)
print(pow(pi,2)/sum)