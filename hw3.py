n=int(input())
k=int(1)
for i in range(n):
    t=int((2*n-1-k)/2)
    print(t*" ",k*"*")
    k+=2
