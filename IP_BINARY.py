x=input()
y=x.split(".")
prefix=int(input())
arr=[]

for i in range(4):
    z = bin(int(y[i]))[2:].zfill(8)
    arr.append(z)

bin = ''.join([str(i) for i in arr])
arr=list(bin)

for j in range(prefix,32):
    arr[j]=0

bin2 = ''.join([str(i) for i in arr])

q=0
for j in range(8):
    print(bin2[q],end="")
    print(bin2[q+1],end="")
    print(bin2[q+2],end="")
    print(bin2[q+3],end=" ")
    q+=4
