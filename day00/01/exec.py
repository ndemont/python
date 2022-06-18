import sys
list = []
str = []
for i in range(1, len(sys.argv)):
	list.append(sys.argv[i])
for elem in list[::-1]:
	elem = elem.swapcase()
	str.append(elem[::-1])
if str:
	print(*str, sep=" ", end="\n")