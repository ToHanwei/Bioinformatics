import sys
from collections import defaultdict

infile = sys.argv[1]

with open(infile) as ofile:
	text, args = ofile.readlines()
	text = text.strip()
	args = args.strip().split(' ')
	kmer = int(args[0])
	dis = int(args[1])


def suffix(pat):
	"""
	return suffix of pattern
	first symbol was droped
	"""
	return pat[1:]

def prefix(pat):
	"""
	return prefix of pattern
	"""
	return pat[0]

def hammingdist(s1, s2):
	"""
	return hamming distance
	"""
	return sum(1 for x, y in zip(s1, s2) if x != y)


def neighbors(pat, dis):
	"""
	get neighbors of pattern within a given
	hamming distance
	params:
		pat: pattern
		dis: distance
	return:
		neighbors of pattern
	"""
	if dis == 0:
		return {pat} 
	if len(pat) == 1:
		return {'A', 'T', 'C', 'G'}
	# recursive call
	# brack the problem into smaller, identical problems
	suffixNeighs = neighbors(suffix(pat), dis)
	neighs = set()
	prex = prefix(pat)
	for text in suffixNeighs:
		# two kinds of treatment
		# hamming distance < given value
		# hamming distance > given value
		if hammingdist(suffix(pat), text) < dis:
			for nuic in ['A', 'C', 'G', 'T']:
				neighs.add(nuic + text)
		else:
			neighs.add(prex + text)
	return neighs


def reverse(pat):
	"""
	get reverse complements
	"""
	mapd = {'A': 'T', 'T': 'A', 'C': 'G', 'G': 'C'}
	length = len(pat)
	reves = ''
	for i in range(length-1, -1, -1):
		nul = pat[i]
		rev = mapd[nul]
		reves += rev
	return reves


def FrequentWordsWithMismatches(text, k, d):
	"""
	count frequent word mismatches
	"""
	length = len(text)
	frepmap = defaultdict(int)
	for i in range(length-k+1):
		pat = text[i:i+k]
		neighs = neighbors(pat, d)
		for neigh in neighs:
			rev = reverse(neigh)
			frepmap[rev] += 1
			frepmap[neigh] += 1
	maxvalue = 0
	patterns = []
	for pat, count in frepmap.items():
		if count > maxvalue:
			maxvalue = count
			patterns = [pat]
		elif count == maxvalue:
			patterns.append(pat)
	return patterns

pats = FrequentWordsWithMismatches(text, kmer, dis)
print(*pats)


