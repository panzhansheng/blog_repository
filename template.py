import inject
import os
from flask import Blueprint
from flask import current_app as app

from api import bp as api_module
from user import bp_user as user_module
from auth import bp_login as login_module

def init(app):
    # url_prefix is the interface prefix of the specified blueprint
    app.register_blueprint(api_module, name="api", url_prefix='/api')
    app.register_blueprint(user_module, name="user", url_prefix='/user')
    app.register_blueprint(login_module, name="login", url_prefix='/')

#    static_module = Blueprint('static_file', __name__,  static_folder="public", static_url_path="/")
#    app.register_blueprint(static_module,   url_prefix='/')

# import all registered blueprint module here:
from user import blueprint_user
from api import blog_api
from auth import login
