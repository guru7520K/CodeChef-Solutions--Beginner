y=[]
n= int(input())
for i in range(n):
       y.append(input())
for u in y:
    count=0
    for c in u:
        if c == "4":
             count+=1
    print(count)
