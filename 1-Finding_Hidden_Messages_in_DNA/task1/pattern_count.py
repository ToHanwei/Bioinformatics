infile = "dataset_2_6.txt"

with open(infile) as inputf:
	text, pattern = inputf.readlines()
	text = text.strip()
	pattern = pattern.strip()

leng_text = len(text)
leng_patt = len(pattern)
count = 0
for i in range(leng_text):
	if text[i:i+leng_patt] == pattern:
		count += 1
print(count)
