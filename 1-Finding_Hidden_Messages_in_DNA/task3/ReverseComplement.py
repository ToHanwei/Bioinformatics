import sys

infile = sys.argv[1]

with open(infile) as seqf:
	seq = seqf.readlines()[0]
	seq = seq.strip()

hask_table = {'A': 'T', 'T': 'A', 'C': 'G', 'G': 'C'}

rc_str = ''

seqlen = len(seq)
for i in range(seqlen-1, -1, -1):
	aad = seq[i]
	rcaad = hask_table[aad]
	rc_str += rcaad

print(rc_str)
