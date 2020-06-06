#(https://stackoverflow.com/questions/33720395/can-pydub-set-the-maximum-minimum-volume)
from pydub import AudioSegment
from pydub.utils import make_chunks
from functools import reduce

#dBFS = Decibels relative to Full Scale
def match_target_amplitude(sample, target_dBFS):
    diff = target_dBFS - sample.dBFS
    return sample.apply_gain(diff)

#Split into chunks to prevent samples with extended silence from lowering overall volume
def chunk_normalize(sample, sample_rate, target_dBFS):
    def min_max_volume(min, max):
        for chunk in make_chunks(sample, sample_rate):
            if chunk.dBFS < min:
                yield match_target_amplitude(chunk, min)
            elif chunk.dBFS > max:
                yield match_target_amplitude(chunk, max)
            else:
                yield chunk
    
    return reduce(lambda x,y: x+y, min_max_volume(target_dBFS[0], target_dBFS[1]))

sample = AudioSegment.from_file('sample_quiet.wav', 'wav')
normalized_dB = [-32, -18]  #[min_normalized_dB, max_normalized_dB]
sample_rate = 41000
normalized_sample = chunk_normalize(sample, sample_rate, normalized_dB)

normalized_sample.export('/home/osboxes/Desktop/Programming/Python/Projects/Sound Bound/normalized_sample_quiet.wav', 'wav')

#Generate samples for testing purposes
"""
from pydub import AudioSegment
sample = AudioSegment.from_file('ImperialMarch60.wav', 'wav')
sample -= 36
sample.export('sample_quiet.wav', 'wav')
"""