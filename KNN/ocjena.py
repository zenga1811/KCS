from Levenshtein import distance as distancel
from Levenshtein import editops

def ocjena(file, prepoznato):
	temp = []
	for x in prepoznato:
		if(x == 'a:'):
			x = 'a'
		elif(x == 'e:'):
			x = 'e'
		elif(x == 'i:'):
			x = 'i'
		elif(x == 'o:'):
			x = 'o'
		elif(x == 'u:'):
			x = 'u'
		elif(x == 'r:'):
			x = 'r'
		if x not in ['buka', 'uzdah', 'greska', 'sil']:
			temp.append(x)
	prepoznato = temp

	transkript = []
	for line in open(file):
		x = line.split("\n")
		x = x[0].split(" ")
		x = x[2]
		if(x == 'a:'):
			x = 'a'
		elif(x == 'e:'):
			x = 'e'
		elif(x == 'i:'):
			x = 'i'
		elif(x == 'o:'):
			x = 'o'
		elif(x == 'u:'):
			x = 'u'
		elif(x == 'r:'):
			x = 'r'
		if x not in ['buka', 'uzdah', 'greska', 'sil']:
			transkript.append(x)

	transkript = "".join(transkript)

	zadnje = ''
	temp = []
	for slovo in prepoznato:
		if slovo == zadnje:
			temp[-1] = (slovo, temp[-1][1] + 1)
		else:
			temp.append((slovo, 1))
			zadnje = slovo

	praviGlasovi = []
	for (glas, i) in temp:
		if(i>=2):
			praviGlasovi.append(glas)
	prepoznato = "".join(praviGlasovi)

	

	insert = delete = replace = 0
	for op, _, _ in editops(prepoznato, transkript):
		if(op == 'delete'):
			delete+=1
		elif(op == 'insert'):
			insert+=1
		elif(op == 'replace'):
			replace+=1
			
	print("\nPravi transkript\n" + transkript)
	print("\nPrepoznati transkript\n" + prepoznato)
	print("\nObrisano:\t\t" + str(delete))
	print("Umetnuto:\t\t" + str(insert))
	print("Zamijenjeno:\t\t" + str(replace))
	print("Levenshtein distance:\t" + str(distancel(prepoznato, transkript)))