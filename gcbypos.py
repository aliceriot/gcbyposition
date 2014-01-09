import gzip
fin = gzip.open('test_data/heli.R1s.fq.gz', 'rb')

def gcbypos(seqfile):
	#initialize empty dictionary
	gc = {}
	for line in enumerate(seqfile):
		count, txt = line
		#check to look only at seq lines
		if count % 4 == 1:
			#check for case of first line
			if count == 1:
				#fill dictionary w/ zeros
				for i in range(len(txt)-1):
					gc[i] = 0
				#check for g/c and update counts
				for j in range(len(txt)-1):
					if txt[j] == 'G' or txt[j] == 'C' or txt[j] == 'g' or txt[j] == 'c':
						gc[j] += 1
			else:
				#if not first line, check for g/c and update counts
				for j in range(len(txt)-1):
					if txt[j] == 'G' or txt[j] == 'C' or txt[j] == 'g' or txt[j] == 'c':
						gc[j] += 1
	for key in gc:
		#divide by count to get proportion
		gc[key] = gc[key] / float(count)
	return gc
