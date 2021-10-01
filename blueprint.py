import inject
import os
from flask import Blueprint
from app_backend import app


from app_backend.wxweb import bp as wx_module
from app_backend.api import bp as api_module

def init(app):
#    app.register_blueprint(wx_module,  url_prefix='/wx')
    app.register_blueprint(api_module,  url_prefix='/api')
#    static_module = Blueprint('static_file', __name__,  static_folder="public", static_url_path="/")
#    app.register_blueprint(static_module,   url_prefix='/')

