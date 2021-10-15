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

# define a wraps with parameter
def token_required_outer(url):
   def token_required_1(f):
      # Python装饰器
      @wraps(f)  
      def decorator(*args, **kwargs):
   #      token = None
         # havent login 
         print(f'reques.referer={request.referrer}')
         user_repo = inject.instance(UserRepository)
         try:
            token = session["token"]
         except:
            return render_template('login.html', url=url)
         if 'x-access-tokens' in request.headers:  
            token = request.headers['x-access-tokens'] 

         if not token:
            #return jsonify({'message': 'a valid token is missing'})   
   #         return render_template('login.html')
            redirect(url_for(request.referrer))

         try:
            data = jwt.decode(token, app.config['SECRET_KEY'])
   #         current_user = Users.query.filter_by(public_id=data['public_id']).first()  
            current_user = user_repo.find(public_id=data['public_id'])[0]
         except Exception as e:
            print(f'exception message={str(e)}', file=sys.stdout)
            return render_template('login.html', url=url)
   #         return jsonify({'exception message': str(e)})  

         return f(current_user, *args,  **kwargs)  
      return decorator
   return token_required_1

# wraps without parameter
def token_required(f):
   # Python装饰器
   @wraps(f)  
   def decorator(*args, **kwargs):
#      token = None
      # havent login 
      print(f'reques.referer={request.referrer}')
      user_repo = inject.instance(UserRepository)
      try:
         token = session["token"]
      except:
         return render_template('auth/login.html', url=request.referrer)
      if 'x-access-tokens' in request.headers:  
         token = request.headers['x-access-tokens'] 

      if not token:
         #return jsonify({'message': 'a valid token is missing'})   
#         return render_template('login.html')
         redirect(url_for(request.referrer))

      try:
         data = jwt.decode(token, app.config['SECRET_KEY'])
#         current_user = Users.query.filter_by(public_id=data['public_id']).first()  
         current_user = user_repo.find(public_id=data['public_id'])[0]
      except Exception as e:
         print(f'exception message={str(e)}', file=sys.stdout)
         # url parameter will be ignored
         return render_template('auth/login.html', url=request.url)
#         return jsonify({'exception message': str(e)})  

      return f(current_user, *args,  **kwargs)  
   return decorator

