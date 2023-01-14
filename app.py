from flask import Flask, render_template, request, redirect
from main import Palette
from werkzeug.utils import secure_filename
from forms import UploadForm
import os



app = Flask(__name__)

SECRET_KEY = os.urandom(32)
app.config['SECRET_KEY'] = SECRET_KEY
PEOPLE_FOLDER = os.path.join('static', 'photo')
app.config['UPLOAD_FOLDER'] = PEOPLE_FOLDER


@app.route("/", methods=["GET", "POST"])
def home():
    form = UploadForm()
    if request.method == "GET":
        image = None
        for file in os.listdir(os.path.join(PEOPLE_FOLDER)):
            if os.path.isfile(os.path.join(PEOPLE_FOLDER, file)):
                image = os.path.join(PEOPLE_FOLDER, file)
                break
        return render_template('home.html', form=form, image=image);
    elif request.method == "POST":
        for file in os.listdir(PEOPLE_FOLDER):
            os.remove(os.path.join(PEOPLE_FOLDER, file))
            # if os.path.isfile(file):
            #     os.remove(file)
        if form.validate_on_submit():
            folder = 'images/'
            if not os.path.exists(folder):
                os.mkdir(folder)
            number = int(request.form['color_count'])
            if request.files['file']:
                f = request.files['file']
                filename = secure_filename(f.filename)
                print (number)
                new_path = os.path.join(folder, filename)
                print(new_path)
                f.save(new_path)
                palette = Palette(filename, 1200, folder, number)
                palette.get_image()
                colors = palette.get_colors()
                palette.save_to_static(folder, PEOPLE_FOLDER, 1080, filename)
                file_to_send = os.path.join(PEOPLE_FOLDER, filename)
                palette.delete_from_images()
                print(colors)
                return render_template('home.html', form=form, colors=enumerate(colors), image=file_to_send)    
        


@app.route("/features")
def features():
    return render_template('features.html')

if __name__ == '__main__':
    app.run(debug=True, port=5000);