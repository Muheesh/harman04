a=[]
for i in range(1,11):
    b=(i)
    a.append(b)
print(a)
b=[]
for i in a:
    if i%2 == 0 :
        b.append(i)
print(b)