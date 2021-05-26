x = int(input())
y = int(input())
z = int(input())
n = int(input())
x1 = [i for i in range(0,x+1)]
y1 = [i for i in range(0,y+1)]
z1 = [i for i in range(0,z+1)]
co_ord = [[a,b,c]for a in x1 for b in y1 for c in z1 if (a+b+c)!=n]
co_ord.sort()
print(co_ord)