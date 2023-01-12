from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileRequired, FileAllowed
from wtforms import IntegerField, SubmitField
from wtforms.validators import DataRequired

class UploadForm(FlaskForm):
    file = FileField('Upload Image: ', validators=[FileRequired(),
                                          FileAllowed(['jpg', 'png'], 'Images only!')
                                          ])
    color_count = IntegerField('Number of colors: ', validators=[DataRequired()])
    submit = SubmitField()
    
    
    
