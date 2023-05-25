#!/bin/bash
cd ~/repoDB/test_files

sox wav_file.wav wav_file_short.raw
x2x +sd < wav_file_short.raw > wav_file.raw

frame -l 320 -p 160 wav_file.raw | \
window -l 320 -L 512 | \
mfcc -l 512 -s 16 -q 4| \
x2x +da -c 12 -f %.4e > wav_file.txt

rm wav_file_short.raw wav_file.raw