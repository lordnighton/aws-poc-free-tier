from wtforms import (Form, TextField, FileField, validators, SubmitField, DecimalField, IntegerField)

class FileUploadForm(Form):
    """Form used on a main page to load the files into a back-end storage"""
    fileUploadField = FileField("Choose a file from you local disk:", validators=[
                        validators.InputRequired()])
    
    submit = SubmitField("Upload")