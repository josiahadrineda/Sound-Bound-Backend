#Here's my take on a Flask API
#My first try so it might not be very pristine
#Yeetus

from flask import Flask, request, render_template
from AudioNormalizer import normalize_audio
from werkzeug.utils import secure_filename
import os

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def adjust_volume():
    if request.method == 'POST':
        file = request.files['file']
        filename = secure_filename(file.filename)

        text = request.form['text']
        if text == 'mild' or text == 'moderate' or text == 'severe':
            dBFS_adjustment = normalize_audio(filename, text)
        else:
            dBFS_adjustment = normalize_audio(filename)

        return render_template('index.html', message=dBFS_adjustment)
    return render_template('index.html', message="upload")

if __name__ == '__main__':
    app.run(debug=True)