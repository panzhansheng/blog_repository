from flask import Blueprint,Flask,request,abort,jsonify

# template_folder is the templates files folder
bp_login = Blueprint('login_post', __name__, template_folder='../views/auth')
print(f'bp_login init')
