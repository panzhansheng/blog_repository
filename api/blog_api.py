import sys
sys.path.append('../')

import inject
from flask import  jsonify,json, render_template
from models.blog import Blog
from repositories.blog_repository import BlogRepository
from services.blog_service import BlogService
from api import bp
blog_service = inject.instance(BlogService)

print(f'blog_api called')
# api home at URL /api, the html page is at Views/ directory
@bp.route('/', methods=['GET'])
def home():
     return render_template('./index.html')

@bp.route('/blog/getbloglist', methods=['GET'])
def get_blog_list():

    list = blog_service.getall()

    result = {
         
         'blogs' : [ item.to_json() for item in list ]

    }


    return jsonify(result)