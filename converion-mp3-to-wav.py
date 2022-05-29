from scipy.io import wavfile
import wave
import numpy as np
import matplotlib.pyplot as plt
from pydub import AudioSegment
 # Definir función de formato de conversión
def trans_mp3_to_wav("C:\\Users\\killo\\Desktop\\Phyton\\audio\\1.1-concepto-basico-de-scrum.mp3"):
    print(filepath)
    song = AudioSegment.from_mp3(filepath)
    song.export("now.wav", format="wav")
trans_mp3_to_wav(source_file_path)


import subprocess
subprocess.call(['ffmpeg', '-i', 'audio.mp3',
                   'audio.wav'])