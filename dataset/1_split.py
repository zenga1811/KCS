from pydub import AudioSegment
import os, sys
os.system("clear")

files = os.listdir("/home/nick/repoDB/wav_sm04")
size = len(files)
obradjeno = 0

for file in files:
	brojac = 0
	id = file[2:-4]

	fullAudio = AudioSegment.from_wav("/home/nick/repoDB/wav_sm04/sm"+id+".wav")
	labFile = "/home/nick/repoDB/lab_sm04/sm" + id + ".lab"
	os.system("mkdir /home/nick/repoDB/obradjeno/" + id)

	sys.stdout.write('\r')
	sys.stdout.write("Obradjeno: " + str(obradjeno)+ " od "+ str(size)+ "\t(" + str(round((obradjeno/size)*100, 2)) + "%)")
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
				os.system("x2x +sd "+name+"_short.raw > " + name + ".raw")
				os.system("rm "+name+".wav")
				os.system("rm "+name+"_short.raw")
				os.system("mv "+name+".raw /home/nick/repoDB/obradjeno/"+id+"/")
				brojac = brojac + 1

		obradjeno = obradjeno +1
	except FileNotFoundError:
		continue