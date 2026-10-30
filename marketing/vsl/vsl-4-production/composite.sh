#!/bin/bash
# out/gfx.mp4 + out/presenter.mp4 + mask.png + out/captions.ass -> out/vsl-4.mp4
set -e
ffmpeg -v error -y -i out/gfx.mp4 -i out/presenter.mp4 -loop 1 -i mask.png -filter_complex \
 "[1:v]scale=540:960:flags=lanczos,format=rgba[p];[2:v]format=gray,scale=540:960[m];[p][m]alphamerge[pm];[0:v][pm]overlay=1290:60:shortest=1[v1];[v1]ass=out/captions.ass:fontsdir=fonts,format=yuv420p[v]" \
 -map "[v]" -map 1:a -af "loudnorm=I=-16:TP=-1.5:LRA=11,aresample=48000" \
 -c:v libx264 -preset veryfast -crf 22 -r 24 -c:a aac -b:a 160k -movflags +faststart out/vsl-4.mp4
ffprobe -v error -show_entries format=duration,size -of csv=p=0 out/vsl-4.mp4
