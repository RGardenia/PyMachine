from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS

# from flask_jwt_extended import JWTManager

import pymysql

pymysql.install_as_MySQLdb()
# 使用mysql数据库时，要么使用pymysql，然后这么配置
# 要么直接使用 mysqlclient

db = SQLAlchemy()  # 创建db对象，方便后期模型类的创建
migrate = Migrate()  # 创建迁移对象
cors = CORS()


# jwt = JWTManager()


def config_extensions(app):
    """ app 初始化时，传入 app 参数，挂载到 app 上"""
    db.init_app(app)
    migrate.init_app(app, db=db)
    cors.init_app(app)
    # jwt.init_app(app)
