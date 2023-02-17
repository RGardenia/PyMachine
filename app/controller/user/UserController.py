from app.controller.base.BaseController import BaseController
from app.common.Utils import Utils
from app.filter.JsonFilter import AlchemyJsonEncoder
from app.model.Models import SysUser
from app.model.Vo.Schema import SysUserSchema
from manager import app
from flask import json
from flask import request
import os, base64

schmea = SysUserSchema()

@app.route("/insertteacher", methods=["POST", "GET"])
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


@app.route("/sys/user/list", methods=["GET"])
def Select():
    # from app.service.user.UserService import UserService
    # mysqltools = UserService()
    # mysqlresult = mysqltools.select()
    mysqlresult = SysUser.query.all()

    res = schmea.dump(mysqlresult, many=True)
    return res
