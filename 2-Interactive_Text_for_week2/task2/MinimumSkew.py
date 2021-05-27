import sys

infile = sys.argv[1]

with open(infile) as genof:
	genome = genof.readlines()[0]
	genome = genome.strip()

skew = 0
_min = 0
index = []

for i, s in enumerate(genome):
	if s == 'G':
		skew += 1
	elif s == 'C':
		skew -= 1
	if skew < _min:
		_min = skew
		index = [i+1]
	elif skew == _min:
			index.append(i+1)


for i in index:
	print(i, end=' ')

print('')
	
