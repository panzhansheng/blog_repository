import inject
from flask import  jsonify,json, render_template,request, make_response, session
from models.Blog import Blog
from models.User import User
from repositories.blog_repository import BlogRepository
from services.blog_service import BlogService
from user import bp_user
from auth.myjwt import token_required_outer, token_required
from repositories.user_repository import UserRepository
from werkzeug.security import generate_password_hash
from werkzeug.utils import redirect
from werkzeug.security import generate_password_hash, check_password_hash
import db
import datetime
import jwt
from flask import current_app as app

userRepo = inject.instance(UserRepository)

print(f'bp_user called')
# api home at URL /api, the html page is at Views/ directory
@bp_user.route('/', methods=['GET'])
# /views/user/auth/login.html
def home():
     return render_template('login.html', user='')


@bp_user.route('/user', methods=['GET'])
def blog_home():
     return render_template('index.html')


@bp_user.route('/get', methods=['GET'])
#@token_required_outer(url='/api/blog/get')
@token_required
def get_blog(current_user):
    return render_template('index.html', user=current_user.name)

@bp_user.route('/user/user', methods=['GET', 'POST'])
#@token_required_outer(url='/api/blog/get')
@token_required
def get_user(current_user):
     if request.method == 'GET':
          return render_template('user.html', user=current_user.name)
     else:
          user_name = request.form['username']
          password = request.form['new_password']
          print(f'new_pass={password}')
          user = userRepo.find(name=f'{user_name}')
          if len(user) > 0:
               hashed_password = generate_password_hash(password, method='sha256')
               userRepo.update_pass(user[0], hashed_password)
               return render_template('user_ok.html', user=user[0].name)

          return render_template('user.html', user=current_user.name)

@bp_user.route('/user/register', methods=['GET','POST'])
@token_required
def register(current_user):
     if request.method == 'GET':
          return render_template('auth/register.html', user=current_user.name)
     else:
          user_name = request.form['username']
          password = request.form['password']
          # return a list
          user = userRepo.find(name=f'{user_name}')
          print(f'user_name={user_name}, password={password}, user={user}')
          # no user exists
          if len(user) == 0:
               hashed_password = generate_password_hash(password, method='sha256')
               db_user = User(name=user_name, password=hashed_password)
               userRepo.create(db_user)
               return render_template('auth/register_ok.html', user=db_user.name)
          # user already exists
          else:
               return redirect('/user/user/register')
