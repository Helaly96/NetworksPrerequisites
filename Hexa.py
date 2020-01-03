def IP(x,u): 

    y=x[::-1]
    y1=u[::-1]

    z=y[0:8]
    z1=y1[0:8]

    z=z[::-1]
    z1=z1[::-1]

    
    y=bin(int(z,16))[2:].zfill(32)
    y1=bin(int(z1,16))[2:].zfill(32)



    first=y1[0:8]
    first_str = ''.join([str(i) for i in first])
    secound=y1[8:16]
    secound_str = ''.join([str(i) for i in secound])
    third=y1[16:24]
    third_str = ''.join([str(i) for i in third])
    last=y1[24:]
    last_str = ''.join([str(i) for i in last])

    print("Last Address to be used is")
    print(int(first_str,2),end=".")
    print(int(secound_str,2),end=".")
    print(int(third_str,2),end=".")
    print(int(last_str,2))


    first=y[0:8]
    first_str = ''.join([str(i) for i in first])
    secound=y[8:16]
    secound_str = ''.join([str(i) for i in secound])
    third=y[16:24]
    third_str = ''.join([str(i) for i in third])
    last=y[24:]
    last_str = ''.join([str(i) for i in last])

    print("Next Address to be used is")
    print(int(first_str,2),end=".")
    print(int(secound_str,2),end=".")
    print(int(third_str,2),end=".")
    print(int(last_str,2),end="")



h=input()
y=h.split(".")
x=[]

for i in range(4):
    x.append(hex(int(y[i]))[2:].zfill(2).upper())

hexed = ''.join([str(i) for i in x])

y=input()
y= int(y)
y2= int(y) -1

w_last=int(hexed,16)+int(y2)
w=int(hexed,16)+int(y)

w_last=hex(int(w_last))[2:].zfill(8).upper()
w=hex(int(w))[2:].zfill(8).upper()

print("Starting address is")
print(h)


z=IP(w,w_last)

