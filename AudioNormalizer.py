"""
TO DO:
- Try testing for sudden loud to soft and sudden soft to loud (DONE)
    - Will NOT accommodate for sudden shifts in volume
- Also implement hearing loss modes (DONE)
    - Mild: Loss of 20-40 dB
    - Moderate: Loss of 41-60 dB
    - Severe: Loss of 61-80 dB
"""

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

def hearing_impairment(target_dBFS, mode):
    modes = ['mild', 'moderate', 'severe']
    adjustment_factor = 0
    if mode in modes:
        if mode == "mild":
            adjustment_factor = 16
        elif mode == "moderate":
            adjustment_factor = 20
        elif mode == "severe":
            adjustment_factor = 25
        
        mode = mode[0].upper() + mode[1:]
        #print("Hearing Impairment Mode:", mode)

        for i in range(len(target_dBFS)):
            target_dBFS[i] += adjustment_factor
    else:
        #print("Hearing Impairment Mode Disabled.")
        pass
    return target_dBFS
    

#CALL THIS!!!!!!!!!!!!!!!!!!!!!!!!!!
def normalize_audio(audio, mode=""):
    sample = AudioSegment.from_file(audio, 'wav')
    normalized_dB = hearing_impairment([-32, -18], mode)  #[min_normalized_dB, max_normalized_dB]
    sample_rate = 41000
    normalized_sample = chunk_normalize(sample, sample_rate, normalized_dB)

    dBFS_adjustment = sample.dBFS / normalized_sample.dBFS
    """
    if dBFS_adjustment > 0:
        return "dBFS Adjustment: +{}".format(dBFS_adjustment)
    return "dBFS Adjustment: {}".format(dBFS_adjustment)
    """
    dBFS_adjustment = (dBFS_adjustment - 1) * 100

    #Rtype => Int expressed as a percentage (+ = increase volume, - = decrease volume)
    return int(dBFS_adjustment)