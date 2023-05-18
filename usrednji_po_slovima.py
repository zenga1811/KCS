import numpy as np
import os, sys, glob

os.system("clear")
os.chdir("/home/nick/repoDB")


files = (os.walk("slova"))

size = len(os.listdir("slova"))
i = 0

for root, dirs, file in files:
	average = []
	if len(root.split("/")) > 1:
		slovo = root.split("/")[1]
		slova = glob.glob("slova/" + slovo + "/*.txt")
		for slovo_ in slova:
			coef = (np.genfromtxt(slovo_))
			average.append(coef)
		average = np.asarray(average)
		np.savetxt("average_slova/" + slovo, average.mean(0), newline = " ")
	sys.stdout.write('\r')
	sys.stdout.write("Obradjeno:\t(" + str(round((i/size)*100, 2)) + "%)")
	sys.stdout.flush()
	i = i + 1