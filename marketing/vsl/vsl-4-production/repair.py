"""Cut a repeated phrase out of a clip: python3 repair.py IN OUT CUT_FROM CUT_TO  (seconds; joins with an 80 ms crossfade)"""
import subprocess, sys
src, dst, a, b = sys.argv[1], sys.argv[2], float(sys.argv[3]), float(sys.argv[4])
x = 0.08
fc = (f"[0:v]trim=0:{a + x/2:.3f},setpts=PTS-STARTPTS[v1];[0:v]trim={b - x/2:.3f},setpts=PTS-STARTPTS[v2];"
      f"[v1][v2]xfade=transition=fade:duration={x}:offset={a - x/2:.3f},format=yuv420p[v];"
      f"[0:a]atrim=0:{a + x/2:.3f},asetpts=PTS-STARTPTS[a1];[0:a]atrim={b - x/2:.3f},asetpts=PTS-STARTPTS[a2];"
      f"[a1][a2]acrossfade=d={x}[a]")
subprocess.run(['ffmpeg', '-v', 'error', '-y', '-i', src, '-filter_complex', fc, '-map', '[v]', '-map', '[a]',
                '-c:v', 'libx264', '-preset', 'veryfast', '-crf', '16', '-r', '24', '-c:a', 'aac', '-b:a', '192k', dst], check=True)
