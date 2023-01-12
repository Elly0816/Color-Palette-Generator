from flask import Flask, render_template, request, redirect
from main import Palette
from werkzeug.utils import secure_filename
from forms import UploadForm
import os



app = Flask(__name__)

SECRET_KEY = os.urandom(32)
app.config['SECRET_KEY'] = SECRET_KEY


@app.route("/", methods=["GET", "POST"])
def home():
    form = UploadForm()
    if request.method == "GET":
        return render_template('home.html', form=form);
    elif request.method == "POST":
        if form.validate_on_submit():
            folder = 'images/'
            number = int(request.form['color_count'])
            if request.files['file']:
                f = request.files['file']
                filename = secure_filename(f.filename)
                print (number)
                new_path = os.path.join(folder, filename)
                print(new_path)
                f.save(new_path)
                palette = Palette(filename, 1200, folder, number)
                palette.getImage()
                colors = palette.getColors()
                print(colors)
                return render_template('home.html', form=form, colors=colors)    
        


@app.route("/features")
def features():
    return render_template('features.html')

if __name__ == '__main__':
    app.run(debug=True, port=5000);