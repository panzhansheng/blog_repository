import sys

from werkzeug.utils import redirect

sys.path.append('../')
from repositories.user_repository import UserRepository
#from typing_extensions import Required

import inject
from flask import  jsonify,json, render_template,request
from models.Blog import Blog
from models.User import User
from repositories.blog_repository import BlogRepository
from services.blog_service import BlogService
from api import bp
from auth.myjwt import token_required_outer, token_required


blog_service = inject.instance(BlogService)
#userRepo = inject.instance(UserRepository)

print(f'blog_api called')
@bp.route('/blog/getbloglist', methods=['GET'])
#@token_required_outer(url='/api/blog/getbloglist')
@token_required
def get_blog_list(current_user):

    list = blog_service.getall()

    result = {
         
         'blogs' : [ item.to_json() for item in list ]

    }


    return jsonify(result)