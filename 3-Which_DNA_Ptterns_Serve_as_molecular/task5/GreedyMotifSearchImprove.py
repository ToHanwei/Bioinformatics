import sys
from collections import Counter


def generateProfile(motifs):
	profile = []
	ns = len(motifs) + 4
	for col in zip(*motifs):
		cd = {'A': 1, 'C': 1, 'G': 1, 'T': 1}
		for c in col:
			cd[c] += 1
		profile.append([cd[c]/ns for c in 'ACGT'])
	return profile


def mostmotif(dna, profile, k):
	trans = {'A': 0, 'C': 1, 'G': 2, 'T': 3}
	mosts = float('-inf')
	motif = ''
	for i in range(len(dna)-k):
		kmer = dna[i:i+k]
		score = 1
		for j, m in enumerate(kmer):
			m = trans[m]
			score *= profile[j][m]
		if mosts < score:
			mosts = score
			motif = kmer
	return motif


def entropyScore(motifs):
	score = 0
	length = len(motifs)
	for col in zip(*motifs):
		c = Counter(col)
		c = sorted(c.items(), key=lambda x: x[1], reverse=True)
		score += (length - c[0][1])
	return score


infile = sys.argv[1]

with open(infile) as valuef:
	lines = valuef.read().strip().split('\n')
	k, t = lines[0].strip().split()
	k, t = int(k), int(t)
	dnas = lines[1:]

bestmotif = [seq[:k] for seq in dnas]
bestscore = entropyScore(bestmotif)
for i in range(len(dnas[0])-k):
	motif = dnas[0][i:i+k]
	motifs = [motif]
	profile = generateProfile(motifs)
	for j in range(1, len(dnas)):
		dna = dnas[j]
		mostm = mostmotif(dna, profile, k)
		motifs.append(mostm)
		profile = generateProfile(motifs)
	score = entropyScore(motifs)
	if bestscore > score:
		bestscore = score
		bestmotif = motifs

for motif in bestmotif:
	print(motif)
