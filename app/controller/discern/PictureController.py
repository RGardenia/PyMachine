from app.common.Result import Result
from app.controller.base.BaseController import BaseController
from app.common.Utils import Utils
from app.filter.JsonFilter import AlchemyJsonEncoder
from app.model.Models import SysUser, MlPic
from app.model.Vo.Schema import SysUserSchema, MlPicSchema
from manager import app
from flask import json, Blueprint, request
import os, base64
from app.config.extensions import jsonrpc

schmea = MlPicSchema()

pic = Blueprint("mlPicture", __name__)


# , endpoint='pic_list'
@pic.route("/list", methods=["GET"])
def Select():
    res = MlPic.query.all()

    return res


@pic.route("/add", methods=["POST"], endpoint='pic')
def add():
    # res = MlPic.query.all()

    mysqlresult = SysUser.query.all()

    return mysqlresult
