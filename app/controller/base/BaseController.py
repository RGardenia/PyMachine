from app.config.env import Config
from app.service.log.LogService import LogService
from app.common.Code import Code
from app.common.Utils import Utils
from flask import request, jsonify
# import cerberus
import time, json


class BaseController:
    """
    * 验证输入信息
    * @param  dict rules
    * @param  string error_msg
    * @return response
    """

    def validateInput(self, rules, error_msg=None):
        # 这边修改成json格式接收参数
        try:
            requests = request.values()
        except TypeError:
            requests = request.get_json()
        error = {}
        # error['msg'] = v.errors
        error['error_code'] = Code.BAD_REQUEST
        error['error'] = True
        return self.json(error)

    ''' 
    * 验证输入信息根据字段名
    * @param  dict rules
    * @param  string error_msg
    * @return response
    '''

    def validateInputByName(self, name, rules, error_msg=None):
        # 这边修改成json格式接收参数
        try:
            requests = request.values()
        except TypeError:
            requests = request.get_json()
        error = {}
        # error['msg'] = v.errors
        error['error_code'] = Code.BAD_REQUEST
        error['error'] = True
        return self.json(error)

    '''
    * 返回Json数据
    * @param  dict body
    * @return json
    '''

    def json(self, body={}):
        if Config.DEBUG_LOG:
            debug_id = Utils.unique_id()
            data = {
                'LOG_ID': debug_id,
                'IP_ADDRESS': request.remote_addr,
                'REQUEST_URL': request.url,
                'REQUEST_METHOD': request.method,
                'PARAMETERS': request.args,
                'RESPONSES': body
            }
            # if Config.SAVE_LOG == 1:
            #     log().debug(data)
            # elif Config.SAVE_LOG == 2:
            #     LogService().add(json.dumps(data), 1, 2)
            body['debug_id'] = debug_id
        return jsonify(body)

    '''
    * 返回错误信息
    * @param  msg string
    * @return json
    '''

    def error(self, msg='', show=True):
        return self.json({'error_code': Code.BAD_REQUEST, 'error': True, 'msg': msg, 'show': show})

    '''
    * 返回成功信息
    * @param  msg string
    * @return json
    '''

    def successData(self, data='', msg='', show=True):
        return self.json({'error_code': Code.SUCCESS, 'data': data, 'msg': msg, 'show': show})
