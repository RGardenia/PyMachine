from flask_marshmallow import Marshmallow
from flask_sqlalchemy import SQLAlchemy
# from flask_redis import FlaskRedis
# from flask_session import Session
# from flask_script import Manager
from flask_jsonrpc import JSONRPC
from flask_migrate import Migrate
from flask_cors import CORS


# 权限模块 https://github.com/raddevon/flask-permissions
# from flask_permissions.core import Permissions
# from flask_jwt_extended import JWTManager
# import pymysql

# pymysql.install_as_MySQLdb()
# 使用mysql数据库时，要么使用pymysql，然后这么配置
# 要么直接使用 mysqlclient

# 日志对象
# log = Log()

# 创建db对象，方便后期模型类的创建
db = SQLAlchemy()

# Session存储对象
# session_store = Session()

# jsonrpc模块实例对象
jsonrpc = JSONRPC()

# 数据转换器的对象创建
ma = Marshmallow()

# 创建迁移对象
# migrate = Migrate()

# 开启 CORS
cors = CORS()

# 创建终端脚本管理对象
# manager = Manager()

# redis链接对象
# redis = FlaskRedis()

# JWT
# jwt = JWTManager()


def config_extensions(app):
    from app.utils.DateBase import init_datebase
    from app.utils.BluePrint import init_blueprint
    from app.utils.upload import init_uploads
    from app.config.env import Config
    """ app 初始化时，传入 app 参数，挂载到 app """
    # 项目根目录
    app.BASE_DIR = Config.BASE_DIR

    # 加载配置文件
    app.config.from_object(Config)

    # 数据库初始化
    db.init_app(app)
    init_datebase(app)

    # 数据迁移初始化
    # migrate.init_app(app, db=db)
    Migrate(app, db)
    # 添加数据迁移的命令到终端脚本工具中
    # manager.add_command('db', MigrateCommand)

    cors.init_app(app)
    # jwt.init_app(app)

    # 数据转换器的初始化
    ma.init_app(app)

    # 注册 上传实例
    init_uploads(app)

    # 日志初始化
    # app.log = log.init_app(app)

    # 蓝图注册
    init_blueprint(app)

    # jsonrpc初始化
    jsonrpc.service_url = "/api"
    jsonrpc.init_app(app)

    # 初始化终端脚本工具
    # manager.app = app

    # 注册自定义命令
    # load_command(manager)