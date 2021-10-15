import sys

from werkzeug.utils import redirect
from werkzeug.security import generate_password_hash

sys.path.append('../')
from repositories.user_repository import UserRepository
#from typing_extensions import Required

import inject
from flask import  jsonify,json, render_template,request
from models.blog import Blog
from models.Users import Users
from repositories.blog_repository import BlogRepository
from services.blog_service import BlogService
from api import bp
from auth.myjwt import token_required_outer, token_required


blog_service = inject.instance(BlogService)
userRepo = inject.instance(UserRepository)

print(f'blog_api called')
# api home at URL /api, the html page is at Views/ directory
@bp.route('/', methods=['GET'])
def home():
     return render_template('auth/login.html', user='')


@bp.route('/blog', methods=['GET'])
def blog_home():
     return render_template('home/home.html')


@bp.route('/blog/get', methods=['GET'])
#@token_required_outer(url='/api/blog/get')
@token_required
def get_blog(current_user):
    return render_template('index.html', user=current_user.name)

@bp.route('/blog/user', methods=['GET', 'POST'])
#@token_required_outer(url='/api/blog/get')
@token_required
def get_user(current_user):
     if request.method == 'GET':
          return render_template('auth/user.html', user=current_user.name)
     else:
          user_name = request.form['username']
          password = request.form['new_password']
          print(f'new_pass={password}')
          user = userRepo.find(name=f'{user_name}')
          if len(user) > 0:
               hashed_password = generate_password_hash(password, method='sha256')
               userRepo.update_pass(user[0], hashed_password)
               return render_template('auth/user_ok.html', user=user[0].name)

          return render_template('auth/user.html', user=current_user.name)

@bp.route('/blog/register', methods=['GET','POST'])
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
               db_user = Users(name=user_name, password=hashed_password)
               userRepo.create(db_user)
               return render_template('auth/register_ok.html', user=db_user.name)
          # user already exists
          else:
               return redirect('/api/blog/register')

@bp.route('/blog/getbloglist', methods=['GET'])
#@token_required_outer(url='/api/blog/getbloglist')
@token_required
def get_blog_list(current_user):

    list = blog_service.getall()

    result = {
         
         'blogs' : [ item.to_json() for item in list ]

    }


    return jsonify(result)