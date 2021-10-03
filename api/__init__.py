from flask import Blueprint,Flask,request,abort,jsonify

# api blueprint's template folder is at /views
bp = Blueprint('api', __name__, template_folder='../views')
print(f'api.init')
