from flask import Blueprint,Flask,request,abort

bp = Blueprint('api', __name__,)
print(f'api.init')