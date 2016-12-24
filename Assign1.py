import urllib
from BeautifulSoup import *

url = raw_input('Enter - ')
html = urllib.urlopen(url).read()

soup = BeautifulSoup(html)

# Retrieve sum of all numbers
tags = soup('span')
sum=0
count=0
for tag in tags:
    # Look at the parts of a tag
    sum = sum + int(tag.contents[0])
    count = count + 1

print sum
print count