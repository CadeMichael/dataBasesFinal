from flask import Flask, render_template

"""
function must be named 'create_app' so flask knows what to run
"""
def create_app():
    app = Flask(__name__)

    @app.route('/')
    def login():
        return render_template('login.html')

    return app
