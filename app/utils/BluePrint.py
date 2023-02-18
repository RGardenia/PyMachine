from app.controller.user.UserController import user
from app.controller.discern.PictureController import pic


def init_blueprint(app):
    # 注册后端蓝图
    app.register_blueprint(user, url_prefix='/sys/user')
    app.register_blueprint(pic, url_prefix='/ml/pic')
