# module imports 
from flask import Flask, render_template, request
import os 
# local imports 
from formPref import PreferenceForm

app = Flask(__name__)
app.config['SECRET_KEY'] = os.urandom(16)

@app.route('/')
def home():
    """ Render information on the project """
    return render_template('home.html')

@app.route('/preferences', methods=["GET","POST"])
def preferences():
    """ Take in user preferences and return matches """
    pForm = PreferenceForm()
    if request.method == "POST":
        # populate from pForm
        minAge = request.form.get('minAge')
        maxAge = request.form.get('maxAge')
        state = request.form.get('state')
        city = request.form.get('city')
        pName = request.form.get('pName')
        pField = request.form.get('pField')
        eLevel = request.form.get('eLevel')
        eMajor = request.form.get('eMajor')
        return render_template(
                'matches.html',
                minAge = minAge,
                maxAge = maxAge,
                state = state,
                city = city,
                pName = pName,
                pField = pField,
                eLevel = eLevel,
                eMajor = eMajor,
                )
    return render_template(
            'preferences.html',
            form=pForm,
            )

# @app.route('/matches')
# def matches():
#     return render_template('matches.html', prefs=False)

if __name__ == "__main__":
    app.run(debug=True)
