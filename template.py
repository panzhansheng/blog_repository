import inject
import os
from flask import Blueprint
from flask import current_app as app

from api import blog_api
from api import bp as api_module

def init(app):
    app.register_blueprint(api_module,  url_prefix='/api')
#    static_module = Blueprint('static_file', __name__,  static_folder="public", static_url_path="/")
#    app.register_blueprint(static_module,   url_prefix='/')

