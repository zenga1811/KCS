import os, sys, glob, pickle, time
import numpy as np

os.system("clear")
os.chdir("/home/ive/repoDB")

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
with open("melKoeficijenti", "wb") as f:
	pickle.dump(melKoeficijenti, f)
with open("glasovi", "wb") as f:
	pickle.dump(glasovi, f)
