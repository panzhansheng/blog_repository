import inject
import db
from flask import Flask,Blueprint
#from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import create_engine,MetaData,Table,Column
from sqlalchemy.types import String
from sqlalchemy.orm import sessionmaker
#from config import Config
from repositories.blog_repository import BlogRepository
from api import bp as api_module
from services.blog_service import BlogService
#from api.blog_api import blog_service

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
app.config['SECRET_KEY']='Gdou@2021'
#app = Flask(__name__)
#app.config.from_object(Config)

app.register_blueprint(api_module,  url_prefix='/api')
blog_service = BlogService()
blog_list = blog_service.getall()
print(f'blog_list={blog_list}')

import template as bp
bp.init(app)

from auth import login as bp_login
bp_login.init(app)

app.run("0.0.0.0", port="8080")


# for control-c capture
# def handler(signal, frame):
#   print('CTRL-C pressed!', file=sys.stdout)
#   sys.exit(0)

# signal.signal(signal.SIGINT, handler)

# # check to see if this is the main thread of execution
# if __name__ == '__main__':

#     # Create the Flask object for the application
# #    app = Flask(__name__)
#     # start the Flask Web Application
#     # While it can be run on any feasible IP, IP = 0.0.0.0 renders the web app on
#     # the host machine's localhost and is discoverable by other machines on the same network 
#     blog_service = BlogService()
#     blog_list = blog_service.getall()
#     print(f'blog_list={blog_list}')
#     app.run("0.0.0.0", port="8000")

