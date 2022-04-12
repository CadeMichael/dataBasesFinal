from flask_wtf import FlaskForm
from wtforms import  IntegerField, StringField, SubmitField

class PreferenceForm(FlaskForm):
    """Preference Form"""
    
    # minimum age 
    minAge = IntegerField(
            'Minimum Age',
            )

    # maximum age 
    maxAge = IntegerField(
            'Maximum Age',
            )

    # location State
    state = StringField(
            'State',
            )

    # location City
    city = StringField(
            'City',
            )

    # profession Name 
    pName = StringField(
            'Profession',
            )

    # profession Field 
    pField = StringField(
            'Profession Field'
            )

    # education Level 
    eLevel = StringField(
            'Highest Level of Education',
            )

    # education Major 
    eMajor = StringField(
            'Degree Major',
            )

    # submit 
    submit = SubmitField('Submit')
