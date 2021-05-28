import sys

infile = sys.argv[1]

with open(infile) as ofile:
	s1, s2 = ofile.readlines()
	s1, s2 = s1.strip(), s2.strip()

hamdis = sum(1 for x, y in zip(s1, s2) if x != y)

print(hamdis)
