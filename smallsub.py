#here all possibilities r present
n=input()
x=[]
for i in n:
    if i not in x:
        x.append(i)
print(len(x))
