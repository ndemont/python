import sys

sys.tracebacklimit = 0

assert (len(sys.argv) > 1), "less than one argument is provided"
assert (len(sys.argv) < 3), "more than one argument is provided"
assert (sys.argv[1].isnumeric()), "argument is not integer"

number = int(sys.argv[1])
if not number:
	print("I'm Zero")
elif not number % 2:
	print("I'm Even")
else:
	print("I'm Odd")