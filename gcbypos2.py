import gzip
fin = gzip.open('test_data/heli.R1s.fq.gz', 'rb')

def gcinit(dictionary,positions):
	for key in range(positions):
		dictionary[key] = 0
	return dictionary

def gccheck(diction,text):
	for i in range(len(text):
		if text[i] == 'G' or text[i] == 'g' or text[i] == 'c' or text[i] == 'C':
			diction[i] += 1
	return diction
	


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
				gcinit(gc,len(txt))
				#check for g/c and update counts
				gccheck(gc,txt)
			else:
				#if not first line, check for g/c and update counts
				gccheck(gc,txt)
	for key in gc:
		#divide by count to get proportion
		gc[key] = gc[key] / float(count)
	return gc
