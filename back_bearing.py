import math

try:
    f_bearing = input("Enter the forward bearing(E.g 2 34 45): ")
    deg1 = [float(x) for x in f_bearing.split()]
except:
    print("Invalid input, try again!")
    f_bearing = input("Enter the forward bearing(E.g 2 34 45): ")
    deg1 = [float(x) for x in f_bearing.split()]

deg1[0] = round(deg1[0], 0)
deg1[1] = round(deg1[1]/60, 1)
deg1[2] = round(deg1[2]/60, 1)

deg = 0

for x in deg1:
    deg += x

bbs = 0

if deg > 180.0:
    bbs = deg - 180
elif deg < 180:
    bbs = deg + 180

sd = math.modf(bbs)

degs = int(sd[1])

sf1 = sd[0]*60
sf = math.modf(sf1)

mins = int(sf[1])

sa1 = sf[0]*60
secs = round(sa1, 2)

print('Back bearing is: {0}°{1}\'{2}\"'.format(degs, mins, secs))
