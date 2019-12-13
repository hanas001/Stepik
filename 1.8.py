X = int(input())
H = int(input())
M = int(input())

HM = H*60 + M
X = X + HM
tm = (X%60)
th = (X//60)

print (th)
print (tm)