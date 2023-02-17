from marshmallow import Schema, fields


class SysUserSchema(Schema):
    id = fields.String()
    username = fields.String()
    password = fields.String()
    realname = fields.String()
    create_time = fields.Date()
    user_identity = fields.Integer()
    del_flag = fields.Integer()
