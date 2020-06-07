# Sound-Bound-Backend
<h1>AudioNormalizer.py is the only file you need to pay attention to</h1>
<br>
<h2><i>specifically the last function named normalize_audio(audio, mode="")</i></h2>
<br>
audio: directory of the audio file to be checked in .wav
<br>
mode: accommodates for hearing impairment<br>
  - if nothing is specified, normalization occurs in regular mode<br>
  - if 'mild' is specified, normalization occurs in hearing impairment mode, mild<br>
  - same thing for 'moderate'<br>
  - same thing for 'severe'<br>
<h2>Return type is an integer representing the percentage increase/decrease from current volume</h2>
