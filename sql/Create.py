import datetime
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm import scoped_session
from sqlalchemy import (
    create_engine,
    Column,
    Integer,
    String,
    Enum,
    DECIMAL,
    DateTime,
    Boolean,
    UniqueConstraint,
    Index
)
from sqlalchemy.ext.declarative import declarative_base

SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:151613@39.98.107.99:3306/cnn_model?charset=utf8'

# 基础类
Base = declarative_base()
# 创建引擎
engine = create_engine(
    SQLALCHEMY_DATABASE_URI,
    # 超过链接池大小外最多创建的链接
    max_overflow=0,
    # 链接池大小
    pool_size=5,
    # 链接池中没有可用链接则最多等待的秒数，超过该秒数后报错
    pool_timeout=10,
    # 多久之后对链接池中的链接进行一次回收
    pool_recycle=1,
    # 查看原生语句（未格式化）
    echo=True
)
# 绑定引擎
Session = sessionmaker(bind=engine)
# 创建数据库链接池，直接使用session即可为当前线程拿出一个链接对象conn
# 内部会采用threading.local进行隔离
session = scoped_session(Session)


class UserInfo(Base):
    """ 必须继承Base """
    # 数据库中存储的表名
    __tablename__ = "user"
    # 对于必须插入的字段，采用nullable=False进行约束，它相当于NOT NULL
    id = Column(Integer, primary_key=True, autoincrement=True, comment="主键")
    name = Column(String(32), index=True, nullable=True, comment="姓名")
    age = Column(Integer, nullable=True, comment="年龄")
    phone = Column(DECIMAL(6), nullable=True, unique=True, comment="手机号")
    address = Column(String(64), nullable=True, comment="地址")
    # 对于非必须插入的字段，不用采取nullable=False进行约束
    gender = Column(Enum("male", "female"), default="male", comment="性别")
    create_time = Column(
        DateTime, default=datetime.datetime.now, comment="创建时间")
    last_update_time = Column(
        DateTime, onupdate=datetime.datetime.now, comment="最后更新时间")
    delete_status = Column(Boolean(), default=False,
                           comment="是否删除")


__table__args__ = (
    UniqueConstraint("name", "age", "phone"),  # 联合唯一约束
    Index("name", "addr", unique=True),  # 联合唯一索引
)


def __str__(self):
    return f"object : <id:{self.id} name:{self.name}>"


if __name__ == "__main__":
    # 创建表
    Base.metadata.create_all(engine)
    # 删除表
    # Base.metadata.drop_all(engine)

    # 创建数据表
    # db.create.all()

    # 模型类.属性.startswith()    #以什么开头的数据
    # 模型类.属性.endswith()    #以什么结尾的数据
    # 模型类.属性.contains()    #数据包含什么什么
    # User.query.filter(User.phone.endswith('3000')).first()  # 获取手机尾号为3000的数据
    # User.query.filter(User.name != 'huan').all()  # 获取用户名不是huan的所有数据
    #
    # 字段为整型或日期类型时，还可以使用以下代码：
    # 模型类.属性.__lt__(18)  # 小于18
    # 模型类.属性.__gt__(18)  # 大于18
    # 模型类.属性.__ge__(18)  # 大于等于18
    # 模型类.属性.__le__(18)  # 小于等于18
    # 模型类.属性.between(18，30)  # 18到30之间

    # User.query.limit(2).all()  # 获取所有数据中前两条数据
    # User.query.offset(2).limit(2).all()  # 跳过所有数据中前两条数据再获取跳过后的前两条数据

    # # 导入and方法，实现逻辑与查询
    # from sqlalchemy import and_
    #
    # User.query.filter(and_(User.name != 'huan', User.phone.endswith('3000'))).all()  # 获取用户名不是huan以及手机尾号为3000
    #
    # # 导入or方法，实现逻辑或查询
    # from sqlalchemy import or_
    #
    # User.query.filter(or_(User.name != 'huan', User.email.endswith('3000'))).all()  # 获取用户名不是huan或手机尾号为3000
    #
    # # 导入not，实现取反查询
    # from sqlalchemy import not_
    #
    # User.query.filter(not_(User.name == 'huan')).all()  # 获取用户名不是huan的所有数据

    # 模型类.query.order_by(参数)
    # User.query.order_by(User.id).all  # 对所有的id进行排序

    # 修改数据
    # user = User.query.first()  # 选定要修改的数据
    # user.username = 'xiu'  # 要修改的参数值
    # db.session.commit()  # 提交事务

    # 删除数据
    # user = User.query.first()
    # db.session.delete(user)
    # db.session.commit()

    # db.drop_all()
