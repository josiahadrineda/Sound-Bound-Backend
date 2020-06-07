# Sound-Bound-Backend
<h2>AudioNormalizer.py is basically the backbone</h2>
<br>
<h3><i>specifically the last function named normalize_audio(audio, mode="")</i></h3>
<br>
audio: directory of the audio file to be checked in .wav
<br>
mode: accommodates for hearing impairment<br>
  - if nothing is specified, normalization occurs in regular mode<br>
  - if 'mild' is specified, normalization occurs in hearing impairment mode, mild<br>
  - same thing for 'moderate'<br>
  - same thing for 'severe'<br>
<h2>Return type is an integer representing the percentage increase/decrease from current volume</h2>
<hr>
<h2>AdjustVolumeAPI.py is exactly what it sounds like</h2>
<br>
index.html inside the templates folder is just a test website to check the responsiveness of the API
