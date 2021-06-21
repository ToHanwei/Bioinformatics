import sys
import random

from collections import Counter


def generateorign(dnas, k):
	motifs = []
	length = len(dnas[0]) - k
	for dna in dnas:
		i = random.randint(0, length)
		motif = dna[i:i+k]
		motifs.append(motif)
	return motifs 

def denerateprofile(motifs, drop):
	# delete one motif with random
	temp = motifs[drop]
	del motifs[drop]
	div = len(motifs) + 4
	profile = []
	for col in zip(*motifs):
		count = {'A': 1/div, 'G': 1/div, 'C': 1/div, 'T': 1/div}
		for c in col:
			count[c] += (1 / div)
		profile.append(count)
	motifs.insert(drop, temp)
	return profile


def probabilitydis(profile, dna, k):
	probdis = []
	kmers = []
	for i in range(len(dna) - k):
		kmer = dna[i:i+k]
		kmers.append(kmer)
		prob = 1
		for j, c in enumerate(kmer):
			prob *= profile[j][c]
		probdis.append(prob)
	s = sum(probdis)
	probdis = [prob / s for prob in probdis]
	sample = random.choices(kmers, weights=probdis)
	return sample[0]


def motifscore(motifs):
	nseqs = len(motifs)
	score = 0
	for col in zip(*motifs):
		count = Counter(col)
		count = sorted(count.items(),
						key=lambda x: x[1],
						reverse=True
					  )
		score += (nseqs - count[0][1])
	return score


def GibbsSampler(dnas, k, t, N):
	motifs = generateorign(dnas, k)
	bestmotifs = motifs[:]
	bestscore = motifscore(bestmotifs)
	for i in range(N):
		drop = random.randint(0, t-1)
		profile = denerateprofile(motifs, drop)
		sample = probabilitydis(profile, dnas[drop], k)
		motifs[drop] = sample
		score = motifscore(motifs)
		if score < bestscore:
			bestmotifs = motifs[:]
			bestscore = score
	return bestmotifs, bestscore
		


infile = sys.argv[1]
with open(infile) as argf:
	lines = argf.readlines()
	args = lines[0].strip().split()
	dnas = [line.strip() for line in lines[1:]]
	k = int(args[0])
	t = int(args[1])
	N = int(args[2])

step = 0
best = float('inf')
bestm = []
while step < 1000:
	motifs, score = GibbsSampler(dnas, k, t, N)
	if best > score:
		bestm = motifs[:]
		best = score
	step += 1

for motif in bestm:
	print(motif)
print(best)
