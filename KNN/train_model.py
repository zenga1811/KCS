import numpy as np
import os, sys, glob, pickle
from sklearn.neighbors import KNeighborsClassifier
from sklearn.svm import SVC
from sklearn.model_selection import GridSearchCV

os.system("clear")
os.chdir("/home/ive/repoDB")

try:
	x_train = np.nan_to_num(np.genfromtxt("knn/x_train.txt"))
	y_train = np.genfromtxt("knn/y_train.txt", dtype = 'str')
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
pickle.dump(clf, open("knn/clf", 'wb'))