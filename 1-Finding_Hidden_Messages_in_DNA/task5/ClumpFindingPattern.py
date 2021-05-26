import sys

infile = sys.argv[1]

with open(infile) as ofile:
	genome, args = ofile.readlines()
	genome = genome.strip()
	kmer, windowSize, thre = args.strip().split(' ')
	kmer = int(kmer)
	windowSize = int(windowSize)
	thre = int(thre)

geolen = len(genome)
patterns = []
for i in range(geolen-windowSize):
	window = genome[i:i+windowSize]
	windowPat = {}
	for j in range(windowSize-kmer):
		pat = window[j:j+kmer]
		if pat in windowPat:
			windowPat[pat] += 1
		else:
			windowPat[pat] = 1
	for pat, count in windowPat.items():
		if (count >= thre) and (pat not in patterns):
			patterns.append(pat)

for pat in patterns:
	print(pat, end=' ')
print('')
