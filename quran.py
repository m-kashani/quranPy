import codecs

def ReadQuran(file='quran-simple-clean.txt'):
	f = codecs.open(file, encoding='utf-8', mode='r')
	quran = []
	for line in f:
		line = line.strip()
		if line:
			parts = line.split('|')
			if len(parts) >= 3:
				chapter = parts[0]
				verse = parts[1]
				text = parts[2]
				vid = chapter + ':' + verse
				quran.append({'vid': vid, 'v': text})
	f.close()
	return quran