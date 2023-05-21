import os, pickle
from sklearn.neighbors import KNeighborsClassifier
from ocjena import ocjena
import numpy as np

os.system("clear")

try:
	clf = pickle.load(open("/home/ive/repoDB/knn/clf", 'rb'))
except:
	print("Model nije istreniran")
	exit()

x_test = np.genfromtxt("/home/ive/repoDB/test_files/wav_file.txt")

ocjena("/home/ive/repoDB/test_files/transkript.lab", clf.predict(x_test))