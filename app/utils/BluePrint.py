from app.controller.user import UserController
from app.controller.base.BluePrintController import admin


def init_blueprint(app):
    # 注册后端蓝图
    app.register_blueprint(admin, url_prefix='/admin')