from flask import Flask

def create_app():
    #configure app
    app = Flask(__name__)

    #index route
    @app.route('/')
    def index():
        return "Hello this is Petfax"
    
    return app