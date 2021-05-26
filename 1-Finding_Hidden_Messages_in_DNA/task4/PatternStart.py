import sys

infile = sys.argv[1]

with open(infile) as ofile:
	pattern, genome = ofile.readlines()
	pattern = pattern.strip()
	genome = genome.strip()

glen = len(genome)
plen = len(pattern)

starts = []
for i in range(glen-plen):
	pat = genome[i:i+plen]
	if pat == pattern:
		starts.append(i)

for s in starts:
	print(s, end=" ")
print('')
