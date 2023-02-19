import json

from flask import Response, jsonify
from app.common.Code import Code
from app.common.Utils import DataEncoder


class Result(Response):
    charset = 'utf-8'
    default_status = 200
    # default_mimetype = 'text/html'
    default_mimetype = 'application/xml'

    # def __init__(self, response=None, status=None, headers=None,
    #              mimetype=None, content_type=None, direct_passthrough=False):
    #     super.__init__()

    @classmethod
    def force_type(cls, rv, environ=None):
        if isinstance(rv, dict):
            rv = jsonify(rv)
        return super(Result, cls).force_type(rv, environ)


def success_api(data=None, code: int = Code.SUCCESS, msg: str = "成功！"):
    """ 成功响应 默认值“成功” """
    return {"code": code, "success": True, "msg": msg, "data": data}


def fail_api(data=None, code: int = Code.ERROR, msg: str = "失败！"):
    """ 失败响应 默认值“失败” """
    return {"code": code, "success": False, "msg": msg, "data": data}


def table_api(msg: str = "", count=0, data=None, limit=10):
    """ 动态表格渲染响应 """
    res = {
        'msg': msg,
        'code': 0,
        'data': jsonify(data),
        'count': count,
        'limit': limit
    }
    return res