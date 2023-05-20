import os, sys, glob, pickle, datetime
import numpy as np
from scipy.spatial import distance
from Levenshtein import distance as distancel
from Levenshtein import editops

os.system("clear")
os.chdir("/home/ive/repoDB")

ignoriraj = ['buka', 'uzdah', 'greska', 'sil']
indeksi = []
novaDat = []

try:
	with open("dataset/melKoeficijenti", "rb") as fp:
		sveSrednjeVrijednosti = np.nan_to_num(pickle.load(fp))

	with open("dataset/glasovi", "rb") as fp:
		sviGlasovi = np.nan_to_num(pickle.load(fp))

	print("Loaded")

except:
	print("Dataset nije generiran\nPokreni skriptu all_files/generiranje_dataseta.py")
	exit()

try:
	indeksi = []
	for line in open('dataset/recenica.txt'):
		x = line.split("\n")
		indeksi.append(x[0])

except:
	startTime = datetime.datetime.now()

	novaDat = np.nan_to_num(np.genfromtxt(open("test_files/wav_file.txt")))
	c = 0

	size = novaDat.shape[0]*len(sviGlasovi)
	for i in range(len(novaDat)):
		distanceList = []
		for j in range(len(sviGlasovi)):
			timeDiff = datetime.datetime.now() - startTime
			string = "Obradjeno:\t" + str(round((c/size)*100, 2)) + "%\t" + str(timeDiff)
			sys.stdout.write('\r')
			sys.stdout.write(string)
			sys.stdout.flush()
			c = c + 1

			dst = distance.euclidean(novaDat[i][1:], sveSrednjeVrijednosti[j][1:])
			#dst = abs(np.correlate(novaDat[i][1:], sveSrednjeVrijednosti[j][1:]))
			distanceList.append(dst)
		minValue = min(distanceList)
		minIndex = distanceList.index(min(distanceList))
		if(sviGlasovi[minIndex] == 'a:'):
			glas = 'a'
		elif(sviGlasovi[minIndex] == 'e:'):
			glas = 'e'
		elif(sviGlasovi[minIndex] == 'i:'):
			glas = 'i'
		elif(sviGlasovi[minIndex] == 'o:'):
			glas = 'o'
		elif(sviGlasovi[minIndex] == 'u:'):
			glas = 'u'
		elif(sviGlasovi[minIndex] == 'r:'):
			glas = 'r'
		else:
			glas = sviGlasovi[minIndex]
		try:
			if(glas not in ignoriraj):
				indeksi.append(glas)
				open("dataset/distance.txt", "a").write(str(minValue) + "\n")
				open("dataset/recenica.txt", "a").write(str(indeksi[-1]) + "\n")
		except:
			continue

transkript = []

for line in open("test_files/transkript.lab"):
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
prepoznato = "".join(indeksi)

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