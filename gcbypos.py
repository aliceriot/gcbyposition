import gzip
fin = gzip.open('test_data/heli.R1s.fq.gz', 'rb')

def gcbypos(seqfile):
	gc = {}
	for count, txt in enumerate(seqfile):
		if count % 4 == 1:
			for i in len(txt):
				gc[i].append(txt[i])
	return gc

