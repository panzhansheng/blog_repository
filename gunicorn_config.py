# /path-to-your-project/gunicorn_conf.py
bind = '0.0.0.0:8080'
worker_class = 'sync'
loglevel = 'debug'
accesslog = '/var/log/gunicorn/access_log_blog_repository'
acceslogformat ="%(h)s %(l)s %(u)s %(t)s %(r)s %(s)s %(b)s %(f)s %(a)s"
errorlog =  '/var/log/gunicorn/error_log_blog_repository'