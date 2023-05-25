import os, sys, pickle
from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import GridSearchCV
from ocjena import ocjena
import numpy as np

os.system("clear")
os.chdir("/home/ive/repoDB")

try:
	clf = pickle.load(open("dataset/clf", 'rb'))

except:

	try:
		with open("dataset/x_train", "rb") as fp:
			x_train = np.nan_to_num(pickle.load(fp))

		with open("dataset/y_train", "rb") as fp:
			y_train = np.nan_to_num(pickle.load(fp))

	except:
		print("Nije generiran dataset")
		exit()

	"""
	grid_params = { 'n_neighbors' : [5,7,9,11,13,15],
	               'weights' : ['uniform','distance'],
	               'metric' : ['minkowski','euclidean','manhattan']}

	gs = GridSearchCV(KNeighborsClassifier(), grid_params, verbose = 4, cv=3, n_jobs = -1)
	g_res = gs.fit(x_train, y_train)
	print(g_res.best_params_)
	"""

	model = KNeighborsClassifier(metric = 'minkowski',
								n_neighbors = 15,
								weights = 'distance',
								algorithm = 'brute')

	clf = model.fit(x_train, y_train)
	pickle.dump(clf, open("dataset/clf", 'wb'))


x_test = np.genfromtxt("test_files/wav_file.txt")
ocjena("test_files/transkript.lab", clf.predict(x_test))