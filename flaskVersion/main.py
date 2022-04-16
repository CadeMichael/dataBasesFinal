# module imports 
from flask import Flask, render_template, request
import os 
import sqlite3
# local imports 
from formPref import PreferenceForm
from query import queryPrefs

app = Flask(__name__)
# for flask-wtf need secret key
app.config['SECRET_KEY'] = os.urandom(16)

# generate a list of all people (for testing purposes)
def allPeople():
    con = sqlite3.connect('notebook.db')
    cur = con.cursor()
    people = cur.execute("select * from people").fetchall()
    con.commit()
    con.close()
    return people
# home
@app.route('/')
def home():
    """ Render information on the project """
    return render_template('home.html')

# preferences
@app.route('/preferences', methods=["GET","POST"])
def preferences():
    """ Take in user preferences and return matches """
    pForm = PreferenceForm()
    if request.method == "POST":
        # populate from pForm
        minAge = request.form.get('minAge')
        maxAge = request.form.get('maxAge')
        pName = request.form.get('pName')
        pCompany = request.form.get('pCompany')
        pField = request.form.get('pField')
        hName = request.form.get('hName')
        hKind = request.form.get('hKind')
        hSetting = request.form.get('hSetting')
        eName = request.form.get('eName')
        eType = request.form.get('eType')
        eMajor = request.form.get('eMajor')
        eDegree = request.form.get('eDegree')
        people = queryPrefs(minAge,
                maxAge,
                pName,
                pCompany,
                pField,
                hName,
                hKind,
                hSetting,
                eName,
                eType,
                eMajor,
                eDegree)
        return render_template(
                'matches.html',
                people = people
                )
    return render_template(
            'preferences.html',
            form=pForm,
            )

if __name__ == "__main__":
    app.run(debug=True)
