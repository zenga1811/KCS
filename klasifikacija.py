import os, sys, glob, pickle
import numpy as np
from scipy.spatial import distance
from Levenshtein import distance as distancel
from Levenshtein import editops

os.system("clear")

files=glob.glob("all_files/average/average_slova/*.txt")
brojac = len(files)

ignoriraj = ['buka', 'uzdah', 'greska']
indeksi = []
novaDat = []

try:
	with open("sveSrednjeVrijednosti", "rb") as fp:
		sveSrednjeVrijednosti = pickle.load(fp)

	with open("sviGlasovi", "rb") as fp:
		sviGlasovi = pickle.load(fp)

	print("Loaded")

except:
	sviGlasovi = []
	sveSrednjeVrijednosti = []
	redak = 0
	for file in files:
		sviGlasovi.append(os.path.basename(file).split('.')[0])
		sveSrednjeVrijednosti.append(np.genfromtxt(file))
		sys.stdout.write('\r')
		sys.stdout.write("Obradjeno: " + str(redak)+ " od "+ str(brojac)+ "\t(" + str(round((redak/brojac)*100, 2)) + "%)")
		sys.stdout.flush()

		redak = redak + 1

	with open("sveSrednjeVrijednosti", "wb") as fp:
		pickle.dump(sveSrednjeVrijednosti, fp)

	with open("sviGlasovi", "wb") as fp:
		pickle.dump(sviGlasovi, fp)
	print("Saved")

f1 = open("test_files/wav_file.txt")
novaDat = np.genfromtxt(f1)
print("\n\n")

sveSrednjeVrijednosti = np.nan_to_num(sveSrednjeVrijednosti)
novaDat = np.nan_to_num(novaDat)

c = 0
dst = 0
dst_ = 0
size = novaDat.shape[0]*len(sviGlasovi)
for i in range (0, novaDat.shape[0]-1):
	minValue = 1e5
	for j in range(len(sviGlasovi)):
		c = c+1
		"""sys.stdout.write('\r')
		sys.stdout.write("Obradjeno: " + str(c)+ " od "+ str(size)+ "\t(" + str(round((c/size)*100, 2)) + "%)")
		sys.stdout.write("\t" + str(i) + ":" + str(j))
		sys.stdout.flush()"""
		dst = distance.euclidean(novaDat[i][1:], sveSrednjeVrijednosti[j][1:])
		if(dst < dst_):
			print("Nova min dst: " + str(dst))
		dst_ = dst
		if(dst <= minValue):
			minValue = dst
			minIndex = j
		else:
			continue

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
	except:
		continue
print()
print(indeksi)