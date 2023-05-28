import os, sys, pickle
from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import GridSearchCV
from sklearn.metrics import accuracy_score
from ocjena import ocjena
import numpy as np

os.system("clear")
os.chdir("repoDB")

try:
	clf = pickle.load(open("dataset/clf", 'rb'))

except:
	try:
		with open("dataset/x_train", "rb") as fp:
			temp = np.nan_to_num(pickle.load(fp))
		x_train = []
		for line in temp:
			x_train.append(line[1:])

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
	print("Generating new model\n\n")

	model = KNeighborsClassifier(metric = "euclidean",
								n_neighbors = 100,
								weights = "distance",
								algorithm = "brute")

	clf = model.fit(np.asarray(x_train), y_train)
	#pickle.dump(clf, open("dataset/clf", 'wb'))

test_dir = "test_files/test1/"
temp = np.genfromtxt(test_dir + "wav_file.txt")
x_test = []
for line in temp:
	x_test.append(line[1:])

ocjena(test_dir + "transkript.lab", clf.predict(np.asarray(x_test)))