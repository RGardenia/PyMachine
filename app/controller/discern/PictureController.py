import os, base64, uuid, random, string, secrets, datetime
from app.common.Result import Result, success_api, fail_api
from app.model.Vo.Schema import SysUserSchema, MlPicSchema
from app.service.discern.PhotoService import PhotoService
from flask import json, Blueprint, request
from werkzeug.utils import secure_filename
from app.config.env import Config
from app.common.Utils import Utils
from manager import app

schmea = MlPicSchema()

pic = Blueprint("mlPicture", __name__)


# , endpoint='pic_list'
@pic.route("/list", methods=["GET"])
def Select():
    return success_api(data=PhotoService().selectAll())


@pic.route('/upload', methods=['POST'])
def upload_pic():
    # 获取请求体中的数据
    picture = request.files['the_file']

    # 保存 图片 数据
    save_path = Config.UPLOAD_FOLDER + '\\' + secure_filename(picture.filename)
    picture.save(save_path)

    # TODO 模型 预测 类别
    label = Utils.withModel(save_path)

    # TODO 生成随机 唯一字符串
    # byte = uuid.uuid1()
    num = 19
    byte = ''.join(secrets.choice(string.ascii_letters + string.digits) for x in range(num))

    pic_data = {"name": secure_filename(picture.filename),
                "pic_url": save_path,
                "pic_byte": str(byte),
                "create_time": datetime.date.today(),
                "label": label}
    data = PhotoService().Insert(pic_data=pic_data)
    return success_api(data=data)


@pic.route("/delete", methods=["post"])
def Delete():
    pic_byte = request.args.get('pic_byte')
    if PhotoService().delete(pic_byte):
        return success_api()
    else:
        return fail_api()

