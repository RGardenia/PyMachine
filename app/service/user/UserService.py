from app.model.MySQL import MySQL
from flask import jsonify


class UserService():
    def __init__(self):
        self.control = MySQL()

    # 查询数据
    def select(self):
        sql = 'select * from student;'
        result = self.control.select_data(sql)
        return jsonify(result)

    # 插入数据
    def Insert(self, value):
        sql = f'Insert into user(name,age,create_time) values ("{value["name"]}","{value["age"]}","{value["create_time"]}");'
        result = self.control.control_data(sql)
        if result == 1:
            message = {
                'code': 200,
                'success': True
            }
            return jsonify(message)
