from flask import Flask, render_template, request, redirect
from main import Palette
from werkzeug.utils import secure_filename
from forms import UploadForm
import os



app = Flask(__name__)

SECRET_KEY = os.urandom(32)
app.config['SECRET_KEY'] = SECRET_KEY


@app.route("/")
def home():
    form = UploadForm()
    return render_template('home.html', form=form);

@app.route("/features")
def features():
    return render_template('features.html')

#@app.route('/upload', methods=['POST'])
#def upload_file():
 #   if request.method == 'POST':
        #f = request.files[]

if __name__ == '__main__':
    app.run(debug=True, port=5000);