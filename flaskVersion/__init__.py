from flask import Flask, render_template

"""
function must be named 'create_app' so flask knows what to run
"""
def create_app():
    app = Flask(__name__)

    @app.route('/')
    def s_login():
        return render_template('login.html')

    @app.route('/profile')
    def s_profile():
        return render_template('profile.html')
    
    @app.route('/matches')
    def s_matches():
        return render_template('matches.html')

    return app
