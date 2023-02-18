"""
* 蓝图-后台
"""
from flask import Blueprint
from app.controller.base.BaseController import BaseController

admin = Blueprint('admin', __name__)


@admin.route('/register')
def register():
    return BaseController().successData(msg='注册成功')
