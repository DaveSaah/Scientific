from math import atan, degrees, modf

coord = input("Enter the coordinates(E.g 3,4): ")

nums = [float(x) for x in coord.split(",")]

dist = ((nums[0])**2 + (nums[1])**2)**0.5

bear = degrees(atan(nums[0]/nums[1]))

if nums[0] == abs(nums[0]) and nums[1] == abs(nums[1]):
	degs = bear
elif nums[0] == abs(nums[0]) and nums[1] != abs(nums[1]):
	degs = 180 + bear
elif nums[0] != abs(nums[0]) and nums[1] != abs(nums[1]):
	degs = 180 + bear
elif nums[0] != abs(nums[0]) and nums[1] == abs(nums[1]):
	degs = 360 - bear
	
sd = modf(degs)

deg = int(sd[1])

sf1 = sd[0]*60
sf = modf(sf1)

mins = int(sf[1])

sa1 = sf[0]*60
secs = round(sa1, 2)

print('The bearing is: {0}°{1}\'{2}\" and the distance is {3}'.format(deg, mins, secs, round(dist,4)))