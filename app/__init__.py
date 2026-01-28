from flask import Flask
import os

def create_app():
    """Application factory for Flask app"""
    # Get the parent directory of the app folder
    basedir = os.path.abspath(os.path.dirname(os.path.dirname(__file__)))
    app = Flask(__name__, 
                template_folder=os.path.join(basedir, 'templates'),
                static_folder=os.path.join(basedir, 'static'))
    
    from .routes import main_bp
    app.register_blueprint(main_bp)
    
    return app
