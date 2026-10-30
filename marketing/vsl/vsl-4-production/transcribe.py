"""python3 transcribe.py MODEL file1.mp4 file2.mp4 ...  -> prints text, writes file.words.json"""
import sys, json, subprocess, numpy as np
from faster_whisper import WhisperModel
m = WhisperModel(sys.argv[1], device="cpu", compute_type="int8")
for f in sys.argv[2:]:
    raw = subprocess.run(["ffmpeg", "-v", "error", "-i", f, "-ac", "1", "-ar", "16000", "-f", "f32le", "-"], capture_output=True).stdout
    audio = np.frombuffer(raw, np.float32)
    segs, info = m.transcribe(audio, language="es", word_timestamps=True, beam_size=5)
    words = [(w.word.strip(), round(w.start, 2), round(w.end, 2)) for s in segs for w in s.words]
    json.dump(words, open(f + ".words.json", "w"), ensure_ascii=False)
    print(f, "|", " ".join(w for w, _, _ in words), flush=True)
