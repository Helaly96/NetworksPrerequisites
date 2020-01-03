x=input()
y=x[::-1]
z=y[0:8]
z=z[::-1]
print(z)

y=bin(int(z,16))[2:].zfill(32)

first=y[0:8]
first_str = ''.join([str(i) for i in first])
secound=y[8:16]
secound_str = ''.join([str(i) for i in secound])
third=y[16:24]
third_str = ''.join([str(i) for i in third])
last=y[24:]
last_str = ''.join([str(i) for i in last])

print(int(first_str,2),end=".")
print(int(secound_str,2),end=".")
print(int(third_str,2),end=".")
print(int(last_str,2),end="")


#https://www.browserling.com/tools/hex-to-ip?fbclid=IwAR1IK8lsrSUyWFw7_uU_zPh3GW0YxMlv4Opju3Qb7Snb974NQf-sgc7ztO0