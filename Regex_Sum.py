import re

fname = raw_input('Enter file:')
hand = open(fname)
nums = list()
sum = 0
i = 0 
for line in hand:
    line = line.rstrip()
    x = re.findall('[0-9]+', line)
    for i in range(len(x)):
    	val = int(x[i])
    	sum = sum + val
	nums.append(val)
print len(nums)
print sum

