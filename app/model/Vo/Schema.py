from marshmallow import Schema, fields


class SysUserSchema(Schema):
    id = fields.String()
    username = fields.String()
    password = fields.String()
    realname = fields.String()
    create_time = fields.Date()
    user_identity = fields.Integer()
    del_flag = fields.Integer()


class SysLogSchema(Schema):
    __tablename__ = 'sys_log'

    id = fields.String()
    log_type = fields.Integer()
    log_content = fields.String()
    operate_type = fields.Integer()
    userid = fields.String()
    username = fields.String()
    create_time = fields.Date()


class MlPicSchema(Schema):
    __tablename__ = 'ml_pic'

    id = fields.Integer()
    name = fields.String()
    pic_url = fields.String()
    label = fields.String()
    rel_path = fields.String()
    del_flag = fields.Integer()
    pic_byte = fields.String()
    create_time = fields.Date()
    create_by = fields.String()