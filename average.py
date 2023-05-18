import numpy as np
import glob, os, sys
os.system("clear")

files=glob.glob("../obradjeno/*/*.txt")

current = 0
whole = len(files)

for file in files:

    name = file.split("/")[-1][0:-8]

    arr = np.nan_to_num(np.genfromtxt(file))
    average = []
    average = arr.mean(0)
    path = "../average/" + name[5] + "/" + str(current) + "_" + name[5:] + ".txt"
    try:
        np.savetxt(path, average, newline = " ")
    except:
        os.makedirs("../average/"+name[5])
        np.savetxt(path, average, newline = " ")

    sys.stdout.write('\r')
    sys.stdout.write("Obradjeno: " + str(current)+ " od "+ str(whole)+ "\t(" + str(round((current/whole)*100, 2)) + "%)")
    sys.stdout.flush()

    current = current + 1