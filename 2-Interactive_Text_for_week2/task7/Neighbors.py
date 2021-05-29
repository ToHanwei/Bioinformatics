import sys 

infile = sys.argv[1]

with open(infile) as ofile:
	pat, dis = ofile.readlines()
	pat = pat.strip()
	dis = int(dis.strip())

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
			

print(*neighbors(pat, dis))
