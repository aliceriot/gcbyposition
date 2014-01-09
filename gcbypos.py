import gzip fin = gzip.open('test_data/heli.R1s.fq.gz', 'rb')

def gcbypos(seqfile):
	gc = {}
	for line in enumerate(seqfile):
		count, txt = line
		if count % 4 == 1:
			if count == 1:
				for i in range(len(txt)):
					gc[i] = 0
				for j in range(len(txt)):
					if txt[j] == 'G' or txt[j] == 'C' or txt[j] == 'g' or txt[j] == 'c':
						gc[j] += 1
			else:
				for j in range(len(txt)):
					if txt[j] == 'G' or txt[j] == 'C' or txt[j] == 'g' or txt[j] == 'c':
						gc[j] += 1
	return gc
