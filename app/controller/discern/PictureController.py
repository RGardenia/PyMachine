import os, base64, uuid, random, string, secrets
from app.controller.base.BaseController import BaseController
from app.common.Result import Result, success_api, fail_api
from app.model.Vo.Schema import SysUserSchema, MlPicSchema
from app.filter.JsonFilter import AlchemyJsonEncoder
from app.service.discern.PhotoService import PhotoService
from flask import json, Blueprint, request
from werkzeug.utils import secure_filename
from app.config.extensions import jsonrpc
from app.common.Utils import Utils
from app.config.env import Config
from manager import app

schmea = MlPicSchema()

pic = Blueprint("mlPicture", __name__)


# , endpoint='pic_list'
@pic.route("/list", methods=["GET"])
def Select():
    return success_api(data=PhotoService().selectAll())


@pic.route('/upload', methods=['POST', 'GET'])
def upload_pic():
    if request.method == 'POST':
        # 获取请求体中的数据
        pic = request.files['the_file']

        # 保存 图片 数据
        save_path = Config.UPLOAD_FOLDER + '\\' + secure_filename(pic.filename)
        # pic.save(save_path)

        # TODO 生成随机 唯一字符串
        # byte = uuid.uuid1()
        num = 19
        byte = ''.join(secrets.choice(string.ascii_letters + string.digits) for x in range(num))

        pic_data = {"name": secure_filename(pic.filename),
                    "pic_url": save_path,
                    "pic_byte": str(byte)}
        data = PhotoService().Insert(pic_data=pic_data)
        return success_api(data=data)
    return fail_api(msg="请求方式不正确！")
