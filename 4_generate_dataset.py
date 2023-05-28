import os, sys, glob, pickle, time, datetime
import numpy as np

os.system("clear")
os.chdir("repoDB")

files=glob.glob("obradjeno/*/*.txt")
brojac = len(files)

glasovi = []
melKoeficijenti = []
redak = 0

start = time.perf_counter()
for file in files:
	glasovi.append(os.path.basename(file).split('.')[0].split("_")[1])
	melKoeficijenti.append(np.genfromtxt(file))

	stop = time.perf_counter()
	timeDiff = round((stop-start) * (brojac/(redak+1) - 1))

	sys.stdout.write('\r')
	sys.stdout.write("Obradjeno:\t" + str(round((redak/brojac)*100, 2)) + "%\t" + str(datetime.timedelta(seconds = timeDiff)))
	sys.stdout.flush()

	redak = redak + 1

with open("dataset/x_train", "wb") as f:
	pickle.dump(melKoeficijenti, f)
with open("dataset/y_train", "wb") as f:
	pickle.dump(glasovi, f)