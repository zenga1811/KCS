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
	results = []

	for slovo in prepoznato:
		if slovo == zadnje:
			results[-1] = (slovo, results[-1][1] + 1)
		else:
			results.append((slovo, 1))
			zadnje = slovo


	praviGlasovi = []
	for (glas, i) in results:
		if(i>=2):
			praviGlasovi.append(glas)

	prepoznato = "".join(praviGlasovi)

	print("\nPravi transkript\n" + transkript)
	print("\nPrepoznati transkript\n" + prepoznato)

	insert = delete = replace = 0
	for i,j,k in editops(prepoznato, transkript):
		if(i=='delete'):
			delete+=1
		elif(i=='insert'):
			insert+=1
		elif(i=='replace'):
			replace+=1

	print("\nDeleted: " + str(delete))
	print("Inserted: " + str(insert))
	print("Replaced: " + str(replace))
	print("Levenshtein distance: " + str(distancel(prepoznato, transkript)))