# from flask_uploads import IMAGES, configure_uploads, UploadSet
from app.config.env import Config
import os


def init_uploads(app):
    app.config['UPLOADED_PHOTO_DEST'] = os.path.dirname(os.path.abspath(__file__))
    # app.config['UPLOADED_PHOTO_ALLOW'] = IMAGES

    # 上传   文件配置 Linux
    # app.config['UPLOAD_FOLDER'] = Config.UPLOAD_FOLDER  # 上传目录
    app.config['MAX_CONTENT_LENGTH'] = Config.MAX_CONTENT_LENGTH  # 上传大小

    # patch_request_class(app, 32 * 1024 * 1024)

    # 实例化 UploadSet 对象
    # photos = UploadSet('PHOTO')
    #
    # configure_uploads(app, photos)

