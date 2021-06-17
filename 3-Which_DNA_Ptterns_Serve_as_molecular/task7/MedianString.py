import sys

def hammingdist(pat1, pat2):
	d = sum(1 for a, b in zip(pat1, pat2) if a != b)
	return d


def DisBetPatAndString(pat, dnas):
	k = len(pat)
	dis = 0
	for dna in dnas:
		hamdist = float('inf')
		for i in range(len(dna)-k):
			kmer = dna[i:i+k]
			ham = hammingdist(pat, kmer)
			if ham < hamdist:
				hamdist = ham
		dis += hamdist
	return dis

infile = sys.argv[1]

with open(infile) as of:
	pat, dnas = of.read().strip().split('\n')
	dnas = dnas.split()
	print(DisBetPatAndString(pat, dnas))
