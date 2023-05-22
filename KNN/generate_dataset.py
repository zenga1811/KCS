import numpy as np
import os, sys, glob, pickle, time

os.system("clear")
os.chdir("/home/ive/repoDB")

files = (os.walk("slova"))
	
size = len(os.listdir("slova"))
i = 0
x_train = []
y_train = []
	
start = time.perf_counter()
for root, dirs, file in files:
	average = []
	if len(root.split("/")) > 1:
		slovo = root.split("/")[1]
		slova = glob.glob("slova/" + slovo + "/*.txt")
		for slovo_ in slova:
			coef = (np.genfromtxt(slovo_))
			x_train.append(coef)
			y_train.append(slovo)

	stop = time.perf_counter()
	timeDiff = round((stop-start) * (size/(i+1) - 1))
	sys.stdout.write('\r')
	sys.stdout.write("Obradjeno:\t" + str(round((i/size)*100, 2)) + "%\t" + tr(datetime.timedelta(seconds = timeDiff))
	sys.stdout.flush()
	i = i + 1
	
np.savetxt("knn/x_train.txt", x_train)
np.savetxt("knn/y_train.txt", y_train, fmt = "%s")