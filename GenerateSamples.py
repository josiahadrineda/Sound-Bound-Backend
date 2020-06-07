#Generate samples for testing purposes

from pydub import AudioSegment
from pydub.utils import make_chunks
from random import randint

sample = AudioSegment.from_file('./ImperialMarch60.wav', 'wav')
chunks = sample[::10000]
sample_reconstructed = AudioSegment.empty()
for chunk in chunks:
    rand = randint(-40,40)
    chunk += rand
    print(rand)
    sample_reconstructed += chunk

sample_reconstructed.export('./Samples/sample_reconstructed.wav', 'wav')