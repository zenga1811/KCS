from pydub import AudioSegment
import os, sys, time
os.system("clear")

os.chdir("/home/ive/repoDB")
files = os.listdir("wav_sm04")
size = len(files)
obradjeno = 0

start = time.perf_counter()
for file in files:
	brojac = 0
	id = file[2:-4]

	fullAudio = AudioSegment.from_wav("wav_sm04/sm"+id+".wav")
	labFile = "lab_sm04/sm" + id + ".lab"
	os.system("mkdir obradjeno/" + id)
	
	stop = time.perf_counter()
	timeDiff = round((stop-start) * (size/(obradjeno+1) - 1))

	sys.stdout.write('\r')
	sys.stdout.write("Obradjeno:\t" + str(round((obradjeno/size)*100, 2)) + "%\t" + str(datetime.timedelta(seconds = timeDiff)))
	sys.stdout.flush()

	try:
		with open(labFile) as f:
			lines = f.readlines()
			for line in lines:

				name = str(brojac)+"_"+line.split()[2]

				if brojac < 10:
					name = "000" + name
				elif brojac >= 10 and brojac < 100:
					name = "00" + name
				elif brojac >= 100 and brojac < 1000:
					name = "0" + name
				else:
					pass
					
				t1 = float(line.split()[0])/10000
				t2 = float(line.split()[1])/10000

				newAudio = fullAudio[t1:t2]
				newAudio.export(name+'.wav', format = "wav")

				os.system("sox "+name+".wav "+name+"_short.raw")
				os.system("/home/ive/repos/SPTK/build/x2x +sd "+name+"_short.raw > " + name + ".raw")
				#os.system("rm "+name+".wav")
				os.system("rm "+name+"_short.raw")
				os.system("mv "+name+".raw obradjeno/"+id+"/")
				os.system("mv "+name+".wav obradjeno/"+id+"/")
				brojac = brojac + 1

		obradjeno = obradjeno +1
	except FileNotFoundError:
		continue