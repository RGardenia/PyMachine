from app.controller.base.BaseController import BaseController
from app.filter.JsonFilter import AlchemyJsonEncoder
from app.model.Vo.Schema import SysUserSchema
from app.config.extensions import jsonrpc
from app.common.Result import success_api
from app.model.Models import SysUser
from app.common.Utils import Utils
from flask import request, Blueprint, json
from manager import app

schmea = SysUserSchema()

user = Blueprint("sysUser", __name__)


@jsonrpc.method(name="Home.index")
def index():
    return "hello world!"


@user.route("/insertteacher", methods=["POST", "GET"])
def Insert():
    from app.service.user.UserService import UserService
    mysqltools = UserService()
    values = {
        'name': '测试老师数据222',
        'age': 19,
        'create_time': '2020-07-31'
    }
    mysqlresult = mysqltools.Insert(values)
    return mysqlresult


@user.route("/list", methods=["GET"])
def Select():
    # from app.service.user.UserService import UserService
    # mysqltools = UserService()
    # mysqlresult = mysqltools.select()
    mysqlresult = SysUser.query.all()

    res = schmea.dump(mysqlresult, many=True)
    return success_api(data=res)
