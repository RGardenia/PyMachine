import datetime
import os


class Config(object):
    # Server
    Server_Port = 9999
    # mysql
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:151613@39.98.107.99:3306/cnn_model?charset=utf8'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    DATABASE_HOST = '39.98.107.99'
    DATABASE_PORT = 3306
    DATABASE_USER = 'root'
    DATABASE_PASSWORD = '151613'
    DATABASE_NAME = 'cnn_model'
    DATABASE_TABLE_USER = 'user'

    # 构建项目所在的 绝对路径，也就是 day08 的绝对路径
    BASE_DIR = os.path.abspath(os.path.dirname(os.path.dirname(__file__)))

    # debug
    # DEBUG = True  # 调试模式
    DEBUG_LOG = True

    # log save 1 为文件形式，2为数据库形式，默认数据库
    SAVE_LOG = 1
    # upload
    UPLOAD_FOLDER = '/opt/uploads/'  # 允许目录
    MAX_CONTENT_LENGTH = 16 * 1024 * 1024  # 允许大小16MB
    ALLOWED_EXTENSIONS = set(['txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'])  # 允许文件
    # 自定义的 图片上传路径
    MEDIA_ROOT = os.path.join(BASE_DIR, UPLOAD_FOLDER, 'media/')
    # 静态资源存放路径
    STATIC_ROOT = os.path.join(BASE_DIR, UPLOAD_FOLDER, 'static/')

    # jwt
    SECRET_KEY = '7PXsHcHGfa4e3kEs8Rvcv8ymjI0UeauX'
    JWT_LEEWAY = 604800
    JWT_ACCESS_TOKEN_EXPIRES = datetime.timedelta(days=1)  # 指明token的过期时间
    # JWT_HEADER_TYPE = 'JWT'  # 可以修改 请求头中 ，token字符串的 前缀
