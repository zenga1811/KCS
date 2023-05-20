import os, sys, glob, pickle, time
import numpy as np

os.system("clear")
os.chdir("/home/ive/repoDB")

files=glob.glob("obradjeno/*/*.txt")
brojac = len(files)

sviGlasovi = []
sveSrednjeVrijednosti = []
redak = 0

start = time.perf_counter()
for file in files:
	sviGlasovi.append(os.path.basename(file).split('.')[0].split("_")[1])
	sveSrednjeVrijednosti.append(np.genfromtxt(file))

	stop = time.perf_counter()
	timeDiff = round((stop-start) * (brojac/(redak+1) - 1))

	sys.stdout.write('\r')
	sys.stdout.write("Obradjeno:\t" + str(round((redak/brojac)*100, 2)) + "%\t" + str(datetime.timedelta(seconds = timeDiff)))
	sys.stdout.flush()

	redak = redak + 1
with open("melKoeficijenti", "wb") as f:
	pickle.dump(sveSrednjeVrijednosti, f)
with open("glasovi", "wb") as f:
	pickle.dump(sviGlasovi, f)
