from flask_wtf import FlaskForm
from wtforms import *
from wtforms.validators import DataRequired
from wtforms.validators import ValidationError
from string import punctuation

class WordJumblerForm(FlaskForm):
    jWord = StringField('Jumbled Word', validators=[DataRequired()])
    submit = SubmitField('Commence Jumbling')
    
    def validate_jWord(FlaskForm, field):
        word = list(field.data)
        for character in word:
            if character.isdigit():
                raise ValidationError("Do not enter numbers")
            if character in punctuation:
                raise ValidationError("Do not enter special characters")

class CaesarCipherForm(FlaskForm):
    originalMessage = StringField("Orignal Message", validators = [])
    encodedMessage = StringField("Encoded Message", validators = [])
    cipherKey = SelectField("Cipher Key",choices = [(1,"one"),(2,"two"),(3,"three"),(4,"four"),(5,"five"),(6,"six")],coerce = int,description = "This is how far the letters will be shifted over. For instance, if the Cipher Key is 2, the letter a will be shifted to c")
    submit = SubmitField("Encode & Decode")
    def validate_originalMessage(FlaskForm, field):
        word = list(field.data)
        for character in word:
            if character.isdigit():
                raise ValidationError("Do not enter numbers")
            if character in punctuation:
                raise ValidationError("Do not enter special characters")
                
class SoundReverserForm(FlaskForm):
    recordTime = SelectField("Recording Time",choices = [(1,"one"),(2,"two"),(3,"three"),(4,"four"),(5,"five"),(6,"six")],coerce = int)
    submit = SubmitField("Reverse Sound")
    