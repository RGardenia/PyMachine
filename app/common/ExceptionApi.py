from flask import jsonify, make_response
from app.config.env import Config
from app.common.Log import log
from app.common.Utils import Utils
from app.service.LogService import LogService
import traceback, sys
from app import dBSession


def ExceptionApi(code, e):
    """ 接口异常处理 """
    exc_type, exc_value, exc_traceback = sys.exc_info()
    if Config.DEBUG_LOG:
        if Config.SAVE_LOG == 1:
            log().exception(e)
        elif Config.SAVE_LOG == 2:
            LogService().add(e, 1, 3)  # 导致文件互相引用
    body = {}
    body['error_code'] = code
    body['error'] = True
    body['show'] = False
    body['debug_id'] = Utils.unique_id()
    dBSession.close()
    # 这里exc_type 和exc_value信息重复，所以不打印
    body['traceback'] = traceback.format_exception(exc_type, exc_value, exc_traceback)
    return make_response(jsonify(body))
