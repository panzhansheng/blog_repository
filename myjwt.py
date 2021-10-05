from werkzeug.security import generate_password_hash, check_password_hash
import jwt
from flask import Flask, request, Response, jsonify, make_response, render_template, session, redirect, url_for, Blueprint
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash
import sys
from functools import wraps
from blog_repository import app
from models import Users
import db
import datetime
import inject
from repositories.user_repository import UserRepository

def token_required(f):  
   @wraps(f)  
   def decorator(*args, **kwargs):
#      token = None
      # havent login 
      user_repo = inject.instance(UserRepository)
      try:
         token = session["token"]
      except:
         return render_template('login.html')
      if 'x-access-tokens' in request.headers:  
         token = request.headers['x-access-tokens'] 

      if not token:
         #return jsonify({'message': 'a valid token is missing'})   
         return render_template('login.html')

      try:
         data = jwt.decode(token, app.config['SECRET_KEY'])
#         current_user = Users.query.filter_by(public_id=data['public_id']).first()  
         current_user = user_repo.find(public_id=data['public_id'])[0]
      except Exception as e:
         print(f'exception message={str(e)}', file=sys.stdout)
         return render_template('login.html')
#         return jsonify({'exception message': str(e)})  

      return f(current_user, *args,  **kwargs)  
   return decorator    

