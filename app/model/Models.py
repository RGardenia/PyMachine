# coding: utf-8
from sqlalchemy import Column, Integer, String, Text, DateTime
from sqlalchemy.schema import FetchedValue
from sqlalchemy.ext.declarative import declarative_base
from app.config.extensions import db

Base = declarative_base()
metadata = Base.metadata


class SysUser(db.Model):
    __tablename__ = 'sys_user'

    id = Column(String, primary_key=True)
    username = Column(String(99), nullable=False, server_default=FetchedValue(), autoincrement=True)
    realname = Column(String(100))
    password = Column(String(199), nullable=False)
    salt = Column(String(45))
    avatar = Column(String(199))
    birthday = Column(DateTime)
    sex = Column(Integer)
    del_flag = Column(Integer)
    create_time = Column(DateTime)
    user_identity = Column(Integer)

    def toJson(self):
        return {
            "id": self.id,
            "username": self.username,
            "password": self.password,
            "realname": self.realname,
            "create_time": self.create_time,
            "user_identity": self.user_identity,
            "del_flag": self.del_flag
        }


class SysLog(db.Model):
    __tablename__ = 'sys_log'

    id = Column(String, primary_key=True)
    log_type = Column(Integer)
    log_content = Column(String(1000))
    operate_type = Column(Integer)
    userid = Column(String(199))
    username = Column(String(199))
    create_time = Column(DateTime)

    def toJson(self):
        return {
            "id": self.id,
            "log_type": self.log_type,
            "log_content": self.log_content,
            "operate_type": self.operate_type,
            "userid": self.userid,
            "username": self.username,
            "create_time": self.create_time,
        }


class MlPic(db.Model):
    __tablename__ = 'ml_pic'

    id = Column(Integer, primary_key=True)
    name = Column(String(110))
    pic_url = Column(String(200))
    label = Column(String(50))
    rel_path = Column(String(100))
    nginx_port = Column(Integer)
    pic_byte = Column(String(199))
    create_time = Column(DateTime)
    create_by = Column(String(60))

    def toJson(self):
        return {
            "id": self.id,
            "name": self.name,
            "pic_url": self.pic_url,
            "label": self.label,
            "rel_path": self.rel_path,
            "nginx_port": self.nginx_port,
            "pic_byte": self.pic_byte,
            "create_time": self.create_time,
            "create_by": self.create_by,
        }


class HtLog(Base):
    __tablename__ = 'ht_logs'

    id = Column(Integer, primary_key=True)
    type = Column(Integer, nullable=False, server_default=FetchedValue())
    level = Column(Integer, nullable=False, server_default=FetchedValue())
    data = Column(Text, nullable=False)
    create_time = Column(Integer, nullable=False)

    @property  # 把方法变成属性，生成setter
    def password(self):
        return self._password

    @password.setter  # 设置数据
    def password(self, value):
        # self._password = generate_password_hash(value)
        pass

    @classmethod
    def create_user(cls, username, userpass, useremail, usermobile):
        user = cls()
        user.username = username
        user.password = userpass
        user.useremail = useremail
        user.usermobile = usermobile
        # db.session.add(user)
        # db.session.commit()


class HtSuggest(Base):
    __tablename__ = 'ht_suggest'

    add_time = Column(Integer, nullable=False)
    id = Column(Integer, primary_key=True)
    users_id = Column(Integer, nullable=False)
    message = Column(String(255, 'utf8_unicode_ci'), nullable=False)


class User(Base):
    __tablename__ = 'ht_users'

    id = Column(Integer, primary_key=True)
    name = Column(String(255, 'utf8_unicode_ci'), unique=True)
    email = Column(String(255, 'utf8_unicode_ci'), nullable=False, unique=True)
    tel = Column(String(20, 'utf8_unicode_ci'), unique=True)
    password = Column(String(255, 'utf8_unicode_ci'), nullable=False)
    status = Column(Integer, nullable=False)
    remember_token = Column(String(100, 'utf8_unicode_ci'))
    created_at = Column(Integer)
    updated_at = Column(Integer)
    url_path = Column(String(300, 'utf8_unicode_ci'))
    real_path = Column(String(300, 'utf8_unicode_ci'))
