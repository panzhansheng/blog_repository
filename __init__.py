import inject
from blog_repository import db
from flask import Flask,Blueprint
#from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import create_engine,MetaData,Table,Column
from sqlalchemy.types import String
from sqlalchemy.orm import sessionmaker
#from config import Config
from repositories.blog_repository import BlogRepository

from services.blog_service import BlogService

db.init_db()


def config_ioc(binder):
    blog_repository = BlogRepository()

    blog_serivce = BlogService()

    blog_bind = db.BlogSQL
    # edutype_bind = db.EduTypeSQL
    # recruitplan_bind = db.RecruitPlanSQL
    # major_bind = db.MajorSQL
    # prerecstudent_bind = db.PreRecStudentSQL

    binder.bind(BlogRepository,blog_repository)
    # binder.bind(EduTypeRepository,edutype_repository) 
    # binder.bind(RecruitPlanRepository, recruitplan_repository)
    # binder.bind(MajorRepository, major_repository)
    # binder.bind(PreRecStudentRepository, prerecstudent_repository)

    binder.bind(BlogService,blog_serivce)
    # binder.bind(EduTypeService,edutype_service)
    # binder.bind(RecruitPlanService,recruitplan_service)
    # binder.bind(MajorService,major_service)
    # binder.bind(PreRecStudentService, prerecstudent_service)

    binder.bind(db.BlogSQL,blog_bind)
    # binder.bind(db.EduTypeSQL,edutype_bind)
    # binder.bind(db.RecruitPlanSQL,recruitplan_bind)
    # binder.bind(db.MajorSQL,major_bind)
    # binder.bind(db.PreRecStudentSQL,prerecstudent_bind)

inject.configure(config_ioc)


class CustomFlask(Flask):
    jinja_options = Flask.jinja_options.copy()
    jinja_options.update(dict(
      block_start_string='{%',
      block_end_string='%}',
      variable_start_string='((',
      variable_end_string='))',
      comment_start_string='{#',
      comment_end_string='#}',
    ))


app = CustomFlask(__name__)
#app = Flask(__name__)
#app.config.from_object(Config)


#cors = CORS(app, resources={r"/api/*": {"origins": "*"}})

# static_module = Blueprint('static_file', __name__,url_prefix='',static_folder='../static/dist', static_url_path='' )

# static_module = Blueprint('static_file', __name__,url_prefix='',static_folder='../static/dist', static_url_path='/')

# app.register_blueprint(static_module,  url_prefix='/')

import template as bp
bp.init(app)

print(f'blog_repository directory init called')