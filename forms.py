from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileRequired, FileAllowed
from wtforms import IntegerField
from wtforms.validators import DataRequired

class UploadForm(FlaskForm):
    file = FileField('image', validators=[FileRequired(),
                                          FileAllowed(['jpg', 'png'], 'Images only!')
                                          ])
    color_count = IntegerField('number', validators=[DataRequired()])
    
    
    
