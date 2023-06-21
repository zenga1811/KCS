import os, pickle, sys, time, datetime
from sklearn.neighbors import KNeighborsClassifier
from ocjena import ocjena
from statistics import mean
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

	print("Generating new model\n\n")

	model = KNeighborsClassifier(metric = "minkowski",
								n_neighbors = 100,
								weights = "distance")

	clf = model.fit(np.asarray(x_train), y_train)
	pickle.dump(clf, open("dataset/clf", 'wb'))

wav_folder = "wav_sm04/"
lab_folder = "lab_sm04/"
test_dir = "test_files/test/"

srednje_vrijednosti = []
size = 0.2*2329

start = time.perf_counter()
i = 0
for file in os.listdir(wav_folder):
	id = os.fsdecode(file).split(".")[0]
	wav_filename = (os.path.join(wav_folder, id + ".wav"))
	lab_filename = (os.path.join(lab_folder, id + ".lab"))

	if(os.path.exists(wav_filename) and os.path.exists(lab_filename)):

		os.system("cp " + wav_filename + " " + test_dir + "/wav_file.wav")
		os.system("cp " + lab_filename + " " + test_dir + "/transkript.lab")
			
		os.chdir("test_files/test")
		os.system("./script.sh")
		os.chdir("../..")
			
		temp = np.genfromtxt(test_dir + "wav_file.txt")
		x_test = []
		for line in temp:
			x_test.append(line[1:])

		delete, replace, insert, pouzdanost = ocjena(test_dir + "transkript.lab", clf.predict(np.asarray(x_test)))
		srednje_vrijednosti.append([delete, replace, insert, pouzdanost])

		os.system("rm test_files/test/transkript.lab test_files/test/wav_file.txt")
			
		stop = time.perf_counter()
		timeDiff = round((stop-start) * (size/(i+1) - 1))

		string = "Obradjeno:\t" + str(round((i/size)*100, 2)) + "%\t" + str(datetime.timedelta(seconds = timeDiff))
		sys.stdout.write('\r')
		sys.stdout.write(string)
		sys.stdout.flush()

		i = i + 1
			
		if(i > size):
			break
	
srednje_vrijednosti = np.asarray(srednje_vrijednosti).mean(0)

print("\n\nSrednje vrijednosti")
print("Izbrisano:\t" + str(srednje_vrijednosti[0]))
print("Zamijenjeno:\t" + str(srednje_vrijednosti[1]))
print("Umetnuto:\t" + str(srednje_vrijednosti[2]))
print("Pouzdanost:\t" + str(srednje_vrijednosti[3]))