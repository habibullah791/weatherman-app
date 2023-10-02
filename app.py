# app.py (or main.py)
from flask import Flask
from routes.Routes import weatherManApp

app = Flask(__name__)

# Register the blueprint with the app
app.register_blueprint(weatherManApp, url_prefix='/api')

if __name__ == '__main__':
    app.run(debug=True)
