import numpy as np
import os, sys, glob, pickle
from sklearn.neighbors import KNeighborsClassifier
from Levenshtein import distance as distancel
from Levenshtein import editops


os.system("clear")
os.chdir("/home/ive/repoDB")

ignoriraj = ['buka', 'uzdah', 'greska', 'sil']

x_test = np.genfromtxt("test_files/wav_file.txt")

try:
	clf = pickle.load(open("knn/clf", 'rb'))
except:
	print("Model nije istreniran")
	exit()

predict = clf.predict(x_test)
prepoznato = []

for x in predict:
	if(x == 'a:'):
		x = 'a'
	elif(x == 'e:'):
		x = 'e'
	elif(x == 'i:'):
		x = 'i'
	elif(x == 'o:'):
		x = 'o'
	elif(x == 'u:'):
		x = 'u'
	elif(x == 'r:'):
		x = 'r'
	if x not in ['buka', 'uzdah', 'greska', 'sil']:
		prepoznato.append(x)

transkript = []

for line in open("test_files/transkript.lab"):
	x = line.split("\n")
	x = x[0].split(" ")
	x = x[2]
	if(x == 'a:'):
		x = 'a'
	elif(x == 'e:'):
		x = 'e'
	elif(x == 'i:'):
		x = 'i'
	elif(x == 'o:'):
		x = 'o'
	elif(x == 'u:'):
		x = 'u'
	elif(x == 'r:'):
		x = 'r'
	if x not in ['buka', 'uzdah', 'greska', 'sil']:
		transkript.append(x)

transkript = "".join(transkript)
prepoznato = "".join(prepoznato)

zadnje = ''
results = []

for slovo in prepoznato:
	if slovo == zadnje:
		results[-1] = (slovo, results[-1][1] + 1)
	else:
		results.append((slovo, 1))
		zadnje = slovo


praviGlasovi = []
for (glas, i) in results:
	if(i>=2):
		praviGlasovi.append(glas)

prepoznato = "".join(praviGlasovi)

print("\nPravi transkript\n" + transkript)
print("\nPrepoznati transkript\n" + prepoznato)

insert = delete = replace = 0
for i,j,k in editops(prepoznato, transkript):
	if(i=='delete'):
		delete+=1
	elif(i=='insert'):
		insert+=1
	elif(i=='replace'):
		replace+=1

print("\nDeleted: " + str(delete))
print("Inserted: " + str(insert))
print("Replaced: " + str(replace))
print("Levenshtein distance: " + str(distancel(prepoznato, transkript)))