#!/bin/bash

sox wav_file.wav wav_file_short.raw
x2x +sd < wav_file_short.raw > wav_file.raw

frame -l 320 -p 160 wav_file.raw | \
window -l 320 -L 512 | \
#mfcc -l 512 -s 16 -q 4 -o 0| \
mgcep -a 0.42 -l 512 -q 4 -o 2|\
x2x +da -f %.4e -c 26 > wav_file.txt

rm wav_file_short.raw wav_file.raw wav_file.wav