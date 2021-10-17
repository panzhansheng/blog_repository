from flask import Blueprint,Flask,request,abort,jsonify

# api blueprint's template folder is at /views
bp_user = Blueprint('user', __name__, template_folder='../views/user')
print(f'user.init')
