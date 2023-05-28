#!/bin/bash
cd ~/repoDB

i=0
y=$(find obradjeno -name "*.raw" | wc -l)
percentage=0

for FILE in obradjeno/*/*.raw
do
	frame -l 320 -p 160 $FILE | \
	window -l 320 -L 512 | \
	#mfcc -l 512 -s 16 -q 4 -o 0| \
	mgcep -a 0.42 -l 512 -q 4 -o 0|\
	vstat -l 26 -o 1 | \
	x2x +da -f %.4e -c 26 > ${FILE}.txt

	((percentage=100*i/y))
	echo -en "\r$percentage%\c\b"
	((i=i+1))
done