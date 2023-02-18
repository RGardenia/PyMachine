'''
@Author: Gardenia
'''
from flask import Flask
import app as env
from app.common.Result import Result
from app.config.extensions import config_extensions

# 读取启动环境
environment = env.read()

# 修改 序列化方式
# Flask.json_encoder = AlchemyJsonEncoder

# 创建 Flask app
app = Flask(__name__)


def init(config_name=None):
    # 初始化 扩展工具
    config_extensions(app)

    app.response_class = Result

    return app
