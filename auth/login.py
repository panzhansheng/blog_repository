from werkzeug.security import generate_password_hash, check_password_hash
import jwt
from flask import Flask, request, Response, jsonify, make_response, render_template, session, redirect, url_for, Blueprint
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash
import sys
from functools import wraps
#from blog_repository import app
from flask import current_app as app
from models import User
import db
import datetime
import inject
from auth import bp_login

from repositories.user_repository import UserRepository

@bp_login.route('/', methods=['GET','POST'])
def login_user(): 

  if request.method == 'GET':
    return render_template('login.html')

#  auth = request.authorization   
  user_name = request.form['username']
  password = request.form['password']
  url = request.form['url']
#  print(f'user={user_name}')

  user_repo = inject.instance(UserRepository)
  user = user_repo.find(name=user_name)
  # user not found
  if len(user) == 0:
    return render_template('login.html')
  else:
    user = user[0]
  print(f'user={user}')
  hashed_password = generate_password_hash(password, method='sha256')
  print(f'user={user.name},{user.password}, hashed={hashed_password}, url={url}, refer={request.referrer}')

#   if not auth or not auth.username or not auth.password:  
#      return make_response('could not verify', 401, {'WWW.Authentication': 'Basic realm: "login required"'})    
#  user = Users.query.filter_by(name=name).first()   
  if user is None:
    return render_template('login.html')

  if check_password_hash(user.password, password): 
     # will expire 2 days
     print(f"password OK, key={app.config['SECRET_KEY']}")
     token_str = {'public_id': user.public_id, 'exp' : datetime.datetime.utcnow() + datetime.timedelta(minutes=60*24*2)}
     token = jwt.encode(token_str, app.config['SECRET_KEY']) 
     user.token = token
     db.session.commit()   
     session['token'] = token
     print(f'token={token}')
     print(f'request.url={request.url}, request.referer={request.referrer}, request.ip={request.host}')
#     return jsonify({'token' : token.decode('UTF-8'),'token_str': token_str}) 
     # if access /login directly, will be directed to login.html page, after successful login, goto /api/blog
     if request.referrer == f'http://{request.host}/' or request.referrer == None:
       return redirect('/user/get')
     else:
      return redirect(request.referrer)
  return make_response('could not verify',  401, {'WWW.Authentication': 'Basic realm: "login required"'})

@bp_login.route('/logout', methods=['GET'])
def logout_user(): 
    session['token'] = ''
    return render_template('index.html')

# def init(app):
#     app.register_blueprint(bp_login, name='login', url_prefix='/')

