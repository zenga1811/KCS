#!/bin/bash
clear

i=0
y=132127
percentage=0

for FILE in ~/repoDB/obradjeno/*/*.raw
do
	frame -l 320 -p 160 $FILE | \
	window -l 320 -L 512 | \
	mgcep -a 0.42 -m 12 -l 512 | \
	vstat -l 13 -o 1 | \
	x2x +da -f %.4e -c 13 > ${FILE}.txt

	((percentage=100*i/y))
	echo -en "\r$percentage%\c\b"
	((i=i+1))
done