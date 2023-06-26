import Levenshtein

def solve(s):
	seen = s[0]
	ans = s[0]
	for i in s[1:]:
		if i != seen:
			ans += i
			seen = i
	return ans

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
	prepoznato = solve("".join(praviGlasovi))

	insert = delete = replace = 0
	for op, _, _ in Levenshtein.editops(prepoznato, transkript):
		if(op == 'delete'):
			delete+=1
		elif(op == 'insert'):
			insert+=1
		elif(op == 'replace'):
			replace+=1

	"""
	print("\nPravi transkript\n" + transkript)
	print("\nPrepoznati transkript\n" + prepoznato)
	print("\nObrisano:\t\t" + str(delete))
	print("Umetnuto:\t\t" + str(insert))
	print("Zamijenjeno:\t\t" + str(replace))
	print("Levenshtein distance:\t" + str(Levenshtein.distance(prepoznato, transkript)))
	print("Pouzdanost:\t\t" + str(((len(transkript)-Levenshtein.distance(prepoznato, transkript))/len(transkript))))
	"""

	return delete, insert, replace, (len(transkript)-Levenshtein.distance(prepoznato, transkript))/len(transkript), transkript, prepoznato