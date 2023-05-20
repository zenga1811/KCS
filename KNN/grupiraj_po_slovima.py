import numpy as np
import os, sys, glob

os.system("clear")
os.chdir("/home/ive/repoDB")

files=glob.glob("obradjeno/*/*.txt")
brojac = len(files)

i = 0
size = len(files)

for file in files:
	slovo = file.split("/")[2].split(".")[0].split("_")[1]
	name = file.split("/")[-1]

	#print("\nKopiraj " + file + " u slova/" + slovo + "/" + name)
	#print("Preimenuj slova/" + slovo + "/" + name + " u slova/" + str(i) + "_" + slovo + ".txt")
	

	try:
		os.makedirs("slova/" + slovo)
	except:
		pass
	os.system("cp " + file + " slova/" + slovo)
	os.system("mv slova/" + slovo + "/" + name + " slova/" + slovo + "/" + str(i) + "_" + slovo + ".txt")

	sys.stdout.write('\r')
	sys.stdout.write("Obradjeno:\t(" + str(round((i/size)*100, 2)) + "%)")
	sys.stdout.flush()
	i = i + 1