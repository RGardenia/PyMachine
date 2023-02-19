from app.model.Models import MlPic
from app.config.extensions import db


class PhotoService():
    def __init__(self):
        pass

    # 查询数据
    def selectAll(self):
        # User.query.filter_by(username='huan').first()
        return MlPic.query.all()

    # 插入数据
    def Insert(self, pic_data):
        picture = MlPic(
            name=pic_data["name"],
            pic_url=pic_data["pic_url"],
            pic_byte=pic_data["pic_byte"]
        )

        # 保存数据至 数据库
        db.session.add(picture)
        # 返回 插入数据
        db.session.flush()
        db.session.commit()

        return picture.toJson()
