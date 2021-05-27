import sys

infile = sys.argv[1]

with open(infile) as text:
	string = text.readlines()[0]
	string = string.strip()

skew = 0
print(skew, end=' ')
for s in string:
	if s == 'G':
		skew += 1
	elif s == 'C':
		skew -= 1

	print(skew, end=' ')

print('')
