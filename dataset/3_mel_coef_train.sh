#!/bin/bash
clear

x=0
y=132127

for FILE in ./obradjeno/*/*.raw
do
	frame -l 320 -p 160 $FILE | \
	window -l 320 -L 512 | \
	mgcep -a 0.42 -m 12 -l 512 | \
	vstat -l 13 -o 1 | \
	x2x +fa -f %.4e -c 13 > ${FILE}.txt

	echo "scale=10 ; ($x / $y) * 100" | bc
	((x=x+1))
done