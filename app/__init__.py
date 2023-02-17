'''
@Author: Gardenia
'''
from flask import Flask
# 权限模块 https://github.com/raddevon/flask-permissions
# from flask_permissions.core import Permissions
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm import scoped_session
from app.common.Code import Code
import manager as e
from app.config.env import Config
from app.config.extensions import config_extensions

# 模型类
# from goods.models import *
# 视图配置路由
# from goods.urls import *
import os, json

# 读取启动环境
environment = e.read()

# 修改 序列化方式
# Flask.json_encoder = AlchemyJsonEncoder

# 创建 Flask app
app = Flask(__name__)

# 配置 sqlalchemy  数据库驱动://数据库用户名:密码@主机地址:端口/数据库?编码
app.config['SQLALCHEMY_DATABASE_URI'] = Config.SQLALCHEMY_DATABASE_URI
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = Config.SQLALCHEMY_TRACK_MODIFICATIONS
# 上传文件配置
app.config['UPLOAD_FOLDER'] = Config.UPLOAD_FOLDER  # 上传目录
app.config['MAX_CONTENT_LENGTH'] = Config.MAX_CONTENT_LENGTH  # 上传大小

# 创建数据库及连接
engine = create_engine(Config.SQLALCHEMY_DATABASE_URI)

# 创建DBSession类型:
DBSession = sessionmaker(bind=engine)
# dBSession = DBSession()

dBSession = scoped_session(DBSession)


@app.teardown_appcontext
def shutdown_session(exception=None):
    dBSession.close()


# 引入使用的控制器
# if environment == 'run' or environment == 'restful':
#     from app.controller import UsersController, AdminController
# 蓝图，新增的后台部分代码
# from app.controller.AdminController import admin
#
# app.register_blueprint(admin, url_prefix='/admin')

def Create(config_name=None):
    # 导入配置文件
    app.config.from_object(Config)
    # 初始化工具(sqlalchemy,migrate)
    config_extensions(app)

    from app.controller.user import UserController
    # 注册后端蓝图
    from app.controller.BluePrintController import admin
    app.register_blueprint(admin, url_prefix='/admin')

    return app
