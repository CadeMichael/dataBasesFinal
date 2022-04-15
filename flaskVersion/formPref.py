from flask_wtf import FlaskForm
from wtforms import  IntegerField, StringField, SubmitField

class PreferenceForm(FlaskForm):
    """Preference Form"""
    
    # minimum age 
    minAge = IntegerField(
            'Minimum Age:',
            default=-1
            )

    # maximum age 
    maxAge = IntegerField(
            'Maximum Age:',
            default=-1
            )

    # profession Name 
    pName = StringField(
            'Profession:',
            )

    # profession Company 
    pCompany = StringField(
            'Works For:',
            )

    # profession Field 
    pField = StringField(
            'Profession Field:',
            )

    # hobby name
    hName = StringField(
            'Hobby name',
            )

    # hobby kind
    hKind = StringField(
            'Type of hobby',
            )

    # hobby setting
    hSetting = StringField(
            'Hobby Setting',
            )

    # education name 
    eName = StringField(
            'Name of Institution:',
            )

    # education type 
    eType = StringField(
            'Type of Institution',
            )

    # education Major 
    eMajor = StringField(
            'Degree Major:',
            )

    # education degree 
    eDegree = StringField(
            'Degree Major:',
            )

    # submit 
    submit = SubmitField('Submit')
