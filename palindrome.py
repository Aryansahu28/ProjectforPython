# def reverse(x):
#     y = str(x)
#     print(y)
#     if(y[0]=='+' or y[0] == '-'):
#         n1 = y[1:]
#         print(n1)
#         n = int(y)
#         print(n)
#         s = 0
#         while(n>0):
#             r = n%10
#             s = s*10 + r
#             print(s)
#             n = n/10
#         print(f"{y[0]}{s}")

#     else:
#         y = int(x)
#         s = 0
#         while(y>0):
#             r = y%10
#             s = s*10 + r
#             y = y/10
#         print(s)

# reverse(+2345)

x = +2345
y = str(x)
print(y)
print(y[0])
print(y[1:])
n = str(y[1:])
print(n)