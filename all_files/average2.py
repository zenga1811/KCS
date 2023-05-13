import numpy as np
import glob, os, sys
from statistics import mean
os.system("clear")

rootdir = "average/"
i = 0
temp = np.zeros(13)

for subdir, dirs, files in os.walk(rootdir):
    temp = np.zeros(13)
    for file in files:
        try:
            name = os.path.join(subdir, file)
            a = np.genfromtxt(name)
            #print("\n\n" + str(a) + "\n + \n" + str(temp))
            temp = np.vstack([temp, a])
            #print("=\n" + str(temp) + "\n")
        except Exception as e:
            print(str(e))
            pass

    average = np.average(temp[1:], 0)
    print("\nAverage of " + str(subdir.split("/")[1]) + ":\n" + str(average))
    
    try:
        np.savetxt("average/average_slova/" + str(subdir.split("/")[1]) + ".txt", average, newline = " ")
        print("Saved to: " + str(subdir.split("/")[1]) + ".txt")
    except Exception as error:
        print("failed: " + str(error))
        pass
