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

def generKmer(k):
	# Recursively generate all peptides
	if k == 1:
		return ['A', 'G', 'C', 'T']
	ps = generKmer(k-1)
	news = []
	for p in ps:
		news.append(p + 'A')
		news.append(p + 'G')
		news.append(p + 'C')
		news.append(p + 'T')
	return news
	

def MedianString(dnas, k):
	distance = float('inf')
	median = ''
	pats = generKmer(k)
	for pat in pats:
		dis = DisBetPatAndString(pat, dnas)
		if distance > dis:
			distance = dis
			median = pat
	return median

infile = sys.argv[1]

with open(infile) as of:
	lines = of.read().strip().split('\n')
	k = int(lines[0])
	dnas = lines[1:]
	print(MedianString(dnas, k))
