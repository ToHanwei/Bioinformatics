import sys
import random
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


def randommotifs(dnas, k):
	motifs = []
	nlens = len(dnas[0])
	for dna in dnas:
		i = random.randint(0, nlens-k)
		motif = dna[i:i+k]
		motifs.append(motif)
	return motifs



infile = sys.argv[1]

with open(infile) as valuef:
	lines = valuef.read().strip().split('\n')
	k, t = lines[0].strip().split()
	k, t = int(k), int(t)
	dnas = lines[1:]


def randomizedmotifsearch(dnas, k):
	bmotif = randommotifs(dnas, k)
	while True:
		bscore = entropyScore(bmotif)
		profile = generateProfile(bmotif)
		# generate motifs
		motifs = []
		for i, dna in enumerate(dnas):
			mostm = mostmotif(dna, profile, k)
			motifs.append(mostm)
		score = entropyScore(motifs)
		if bscore > score:
			bmotif = motifs
		else:
			return bmotif, bscore



step = 0
bestscore = float('inf')
bestmotif = []
while step < 1000:
	bmotif, bscore = randomizedmotifsearch(dnas, k)
	if bestscore > bscore:
		bestscore = bscore
		bestmotif = bmotif
		print(bestmotif)
		print(bestscore)
	step += 1

print('#'*20)

for motif in bestmotif:
	print(motif)


