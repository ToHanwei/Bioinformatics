import sys

infile = sys.argv[1]

with open(infile) as ofile:
	pat, text, dist = ofile.readlines()
	pat = pat.strip()
	text = text.strip()
	dist = int(dist.strip())

text_len = len(text)
pat_len = len(pat)
starts = []
for i in range(text_len - pat_len + 1):
	substr = text[i:i+pat_len]
	count = sum(1 for x, y in zip(substr, pat) if x != y)
	if count <= dist:
		starts.append(i)

print(*starts)	
print(len(starts))
