T=int(input())
for i in range(T):
    X=int(input())
    Sum=0
    while X!=0:
             N=int(X%10)
             Sum+=N
             X=int(X/10)
    print(Sum)
