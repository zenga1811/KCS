#!/bin/bash

sox wav_file.wav wav_file_short.raw
~/Downloads/SPTK/build/x2x +sf < wav_file_short.raw > wav_file.raw

~/Downloads/SPTK/build/frame -l 320 -p 160 -n 1 wav_file.raw | \
~/Downloads/SPTK/build/window -l 320 -L 512 | \
~/Downloads/SPTK/build/mgcep -a 0.42 -m 12 -l 512 -o 0| \
~/Downloads/SPTK/build/x2x +fa -c 13 -f %.4e > wav_file.txt

rm -r wav_file_short.raw wav_file.raw
