import sys
from collections import defaultdict


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

def window_count(patterns, window):
	pat_table = defaultdict(int)
	for i in range(windowSize-kmer):
		pat = window[i:i+kmer]
		pat_table[pat] += 1
	for pat, count in pat_table.items():
		if count >= thre:
			patterns.append(pat)
	return patterns, pat_table


window = genome[:windowSize]
patterns, table = window_count(patterns, window) 
for i in range(windowSize, geolen):
	first_pat = window[:kmer]
	table[first_pat] -= 1
	aad = genome[i]
	window = window[1:] + aad
	last_pat = window[-kmer:]
	table[last_pat] += 1
	
	if table[last_pat] >= thre:
		patterns.append(last_pat)
	

print(len(set(patterns)))
	
	
