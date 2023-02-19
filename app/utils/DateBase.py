from app.config.env import Config
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm import scoped_session
from sqlalchemy import create_engine

# 创建数据库及连接
engine = create_engine(Config.SQLALCHEMY_DATABASE_URI)

# 创建DBSession类型:
DBSession = sessionmaker(bind=engine)
# dBSession = DBSession()

dBSession = scoped_session(DBSession)


def init_datebase(app):
    # 配置 sqlalchemy  数据库驱动://数据库用户名:密码@主机地址:端口/数据库?编码
    app.config['SQLALCHEMY_DATABASE_URI'] = Config.SQLALCHEMY_DATABASE_URI
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = Config.SQLALCHEMY_TRACK_MODIFICATIONS

    @app.teardown_appcontext
    def shutdown_session(exception=None):
        dBSession.close()
