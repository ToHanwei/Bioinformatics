import sys

infile = sys.argv[1]
wordsize = int(sys.argv[2])

with open(infile) as inputf:
	text = inputf.readlines()[0]
	text = text.strip()

leng_text = len(text)
count = {}
for i in range(leng_text-wordsize):
	subtext = text[i:i+wordsize]
	if subtext in count:
		count[subtext] += 1
	else:
		count[subtext] = 1

count = sorted(count.items(), key=lambda x: x[1], reverse=True)

print(count)
		
