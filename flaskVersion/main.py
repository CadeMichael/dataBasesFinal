from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def s_home():
    return render_template('home.html')

@app.route('/preferences')
def s_preferences():
    return render_template('preferences.html')

@app.route('/matches')
def s_matches():
    return render_template('matches.html')

if __name__ == "__main__":
    app.run(debug=True)
