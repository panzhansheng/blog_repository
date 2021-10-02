from flask import Blueprint,Flask,request,abort,jsonify


bp = Blueprint('api', __name__,)
print(f'api.init')

import sys
sys.path.append('../')

# import inject
# from flask import  jsonify,json
# from models.blog import Blog
# from repositories.blog_repository import BlogRepository
# from services.blog_service import BlogService
# from api import bp
# blog_service = inject.instance(BlogService)

# @bp.route('/blog/getbloglist', methods=['GET'])
# def get_blog_list():

#     list = blog_service.getall()
#     print(f'list={list}')
#     result = {
         
#          'blogs' : [ item.to_json() for item in list ]
# #         jsonify(list)
# #       json.dumps([dict(r) for r in list]) 
#     }


#     return jsonify(result)