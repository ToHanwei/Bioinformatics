import sys

infile = sys.argv[1]

with open(infile) as inputf:
	lines = inputf.readlines()
	dna = lines[0].strip()
	k = int(lines[1].strip())
	matrix = []
	for line in lines[2:]:
		values = line.strip().split()
		linevals = []
		for val in values:
			linevals.append(float(val))
		matrix.append(linevals)

trans = {'A': 0, 'C': 1, 'G': 2, 'T': 3}

mostPr = float('-inf')
mostKmer = ''
for i in range(len(dna)-k):
	kmer = dna[i:i+k]
	Pr = 1
	for jj, w in enumerate(kmer):
		ii = trans[w]
		Pr *= matrix[ii][jj]
	if Pr > mostPr:
		mostPr = Pr
		mostKmer = kmer

print(mostKmer)

