#Determine tempo
"""
from __future__ import print_function
import librosa

filename = librosa.util.example_audio_file()

y, sr = librosa.load(filename)

tempo, beat_frames = librosa.beat.beat_track(y=y, sr=sr)

print("Estimated tempo : {:.2f} beats per minute.".format(tempo))

beat_times = librosa.frames_to_time(beat_frames, sr=sr)
"""

#POSSIBLY USE THIS FOR AUDIO TO 8-BIT CONVERSION

#Separate harmonics from percussives & display chromagram
"""
import numpy as np
import librosa

filename = librosa.util.example_audio_file()

y, sr = librosa.load(filename)

hop_length = 512

y_harmonic, y_percussive = librosa.effects.hpss(y)

tempo, beat_frames = librosa.beat.beat_track(y=y_percussive, sr=sr)

mfcc = librosa.feature.mfcc(y=y, sr=sr, hop_length=hop_length, n_mfcc=13)

mfcc_delta = librosa.feature.delta(mfcc)

beat_mfcc_delta = librosa.util.sync(np.vstack([mfcc, mfcc_delta]), beat_frames)

chromagram = librosa.feature.chroma_cqt(y=y_harmonic, sr=sr)

beat_chroma = librosa.util.sync(chromagram, beat_frames, aggregate=np.median)

beat_features = np.vstack([beat_chroma, beat_mfcc_delta])

import matplotlib.pyplot as plt
import librosa.display

plt.subplot(111)
librosa.display.specshow(chromagram, y_axis='chroma')
plt.colorbar()
plt.title("Chromagram")
plt.show()
"""

#POSSIBLE SOUND BOUND STUFF

#Audio file to db spectrogram
"""
import matplotlib.pyplot as plt
import numpy as np
import librosa.display
import librosa

filename = librosa.util.example_audio_file()
y, sr = librosa.load(filename)
plt.figure(figsize=(12, 8))

stft = librosa.stft(y)
D = librosa.amplitude_to_db(np.abs(stft), ref=np.max)
librosa.display.specshow(D, y_axis='linear')
plt.colorbar(format='%+2.0f dB')
plt.title('Linear-frequency power spectrogram')

plt.show()
"""

#Audio file to mono and stereo waveforms
"""
import matplotlib.pyplot as plt
import librosa.display
import librosa

filename = librosa.util.example_audio_file()

plt.figure(figsize=(14, 10))

y, sr = librosa.load(filename)
plt.subplot(211)
librosa.display.waveplot(y, sr=sr)
plt.title('Linear-frequency monophonic waveform')

y, sr = librosa.load(filename, mono=False)
plt.subplot(212)
librosa.display.waveplot(y, sr=sr)
plt.title('Linear-frequency stereophonic waveform')

plt.show()
"""

#Convert waveforms to dB (THIS IS WHAT WE NEED)
#(https://dsp.stackexchange.com/questions/35841/matlab-code-to-evaluate-audio-loundness-over-time)
from scipy.signal import butter, lfilter
from math import sqrt, log
from numpy import squeeze, vectorize
import matplotlib.pyplot as plt
import librosa

wav, fs_Hz = librosa.load('ImperialMarch60.wav')
calibration_factor = 1.0    #Adjust this accordingly
wav_Pa = wav * calibration_factor

smooth_sec = 0.125
smooth_Hz = 1 / smooth_sec
[b,a] = butter(1, smooth_Hz / (fs_Hz / 2), 'low')
#This is where I'm having problems...
#ValueError: selected axis is out of range
wav_env_Pa = sqrt(lfilter(b, a, squeeze(vectorize(wav_Pa**2))))

Pa_ref = 20 * 10**-6
SPL_dB = 10 * log(wav_env_Pa / Pa_ref)

plt.figure()

plt.subplot(211)
t_sec = wav_Pa[1:] / fs_Hz
plt.plot(t_sec, wav_Pa)
plt.xlabel("Time (s)")
plt.ylabel("Pressure (Pa)")

plt.subplot(212)
plt.plot(t_sec, SPL_dB)
plt.xlabel("Time (s)")
plt.ylabel("SPL (dB)")

plot.show()