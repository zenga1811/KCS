import os, sys, glob, pickle, time, datetime
import numpy as np
from scipy.spatial import distance
from ocjena import ocjena

os.system("clear")
os.chdir("repoDB")

try:
	with open("dataset/x_train", "rb") as fp:
		melKoeficijenti = np.nan_to_num(pickle.load(fp))

	with open("dataset/y_train", "rb") as fp:
		glasovi = np.nan_to_num(pickle.load(fp))

	print("Loaded")

except:
	print("Dataset nije generiran\nPokreni skriptu 4_generate_dataset.py")
	exit()

try:
	indeksi = []
	for line in open('dataset/recenica.txt'):
		x = line.split("\n")
		indeksi.append(x[0])

except:
	
	indeksi = []
	novaDat = np.nan_to_num(np.genfromtxt(open("test_files/wav_file.txt")))
	size = novaDat.shape[0]*len(glasovi)
	c = 0

	start = time.perf_counter()
	for i in range(len(novaDat)):
		distanceList = []
		for j in range(len(glasovi)):
			stop = time.perf_counter()
			timeDiff = round((stop-start) * (size/(c+1) - 1))

			string = "Obradjeno:\t" + str(round((c/size)*100, 2)) + "%\t" + str(datetime.timedelta(seconds = timeDiff))
			sys.stdout.write('\r')
			sys.stdout.write(string)
			sys.stdout.flush()
			c = c + 1

			dst = distance.euclidean(novaDat[i], melKoeficijenti[j])
			distanceList.append(dst)
		minValue = min(distanceList)
		minIndex = distanceList.index(min(distanceList))

		if(glasovi[minIndex] == 'a:'):
			glas = 'a'
		elif(glasovi[minIndex] == 'e:'):
			glas = 'e'
		elif(glasovi[minIndex] == 'i:'):
			glas = 'i'
		elif(glasovi[minIndex] == 'o:'):
			glas = 'o'
		elif(glasovi[minIndex] == 'u:'):
			glas = 'u'
		elif(glasovi[minIndex] == 'r:'):
			glas = 'r'
		else:
			glas = glasovi[minIndex]
		try:
			indeksi.append(glas)
			open("dataset/recenica.txt", "a").write(str(indeksi[-1]) + "\n")
		except:
			continue

ocjena("test_files/transkript.lab", indeksi)