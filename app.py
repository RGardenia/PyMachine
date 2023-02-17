# import os
# from flask import Flask
#
#
# def create_app(config=None):
#     app = Flask(__name__)
#     # 先创建一个核心对象 然后加载配置文件
#     # load default configuration
#     # 使用模块导入的方式配置文件
#     app.config.from_object("config.settings")
#
#     # 根据系统环境的不同去加载不同的配置文件
#     if "FLASK_CONF" in os.environ:
#         app.config.from_envvar("FLASK_CONF")
#
#     # 传递参数来加载配置文件
#     if config is not None:
#         if isinstance(config, dict):
#             app.config.update(config)
#         elif config.endswith(".py"):  # 如果是文件，加载文件的
#             app.config.from_pyfile(config)
#     # 注册蓝图
#     import route
#     route.init_app(app)
#
#     # 注册数据类型
#     import model
#     model.init_db_app(app)
#
#     # 绑定序列化模型
#     import serializer
#     serializer.init_app(app)
#
#     return app