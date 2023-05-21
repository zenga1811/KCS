import numpy as np
import os, sys, glob, time

os.system("clear")
os.chdir("/home/ive/repoDB")

files=glob.glob("obradjeno/*/*.txt")
brojac = len(files)

i = 0
size = len(files)

start = time.perf_counter()
for file in files:
	slovo = file.split("/")[2].split(".")[0].split("_")[1]
	name = file.split("/")[-1]
	
	try:
		os.makedirs("slova/" + slovo)
	except:
		pass
	os.system("cp " + file + " slova/" + slovo)
	os.system("mv slova/" + slovo + "/" + name + " slova/" + slovo + "/" + str(i) + "_" + slovo + ".txt")

	stop = time.perf_counter()
	timeDiff = round((stop-start) * (size/(i+1) - 1))

	sys.stdout.write('\r')
	sys.stdout.write("Obradjeno:\t" + str(round((i/size)*100, 2)) + "%\t" + str(datetime.timedelta(seconds = timeDiff)))
	sys.stdout.flush()
	i = i + 1