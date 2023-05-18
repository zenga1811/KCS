#!/bin/bash
cd ~/repoDB/test_files

sox wav_file.wav wav_file_short.raw
x2x +sd < wav_file_short.raw > wav_file.raw

frame -l 320 -p 160 -n 1 wav_file.raw | \
window -l 320 -L 512 | \
mgcep -a 0.42 -m 12 -l 512 -o 0| \
x2x +da -c 13 -f %.4e > wav_file.txt

rm wav_file_short.raw wav_file.raw