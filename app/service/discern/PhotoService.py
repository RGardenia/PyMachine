from app.model.Models import MlPic
from app.model.Vo.Schema import MlPicSchema
from app.config.extensions import db
import json, datetime


class PhotoService():
    def __init__(self):
        pass

    # 查询数据
    def selectAll(self):
        model = MlPic.query.filter_by(del_flag=0).all()
        data = []
        for mlpic in model:
            data.append(mlpic.toJson())
        return data

    # 插入数据
    def Insert(self, pic_data):
        # TODO 调用 模型 预测
        label = 'TODO'

        picture = MlPic(
            name=pic_data["name"],
            pic_url=pic_data["pic_url"],
            pic_byte=pic_data["pic_byte"],
            del_flag=0,
            label=label
        )

        # 保存数据至 数据库
        db.session.add(picture)
        # 返回 插入数据
        db.session.flush()
        db.session.commit()

        return picture.toJson()

    def delete(self, pic_byte):
        mlPic = MlPic.query.filter(MlPic.pic_byte == pic_byte).first()

        # is_delete为True表示删除
        mlPic.del_flag = 1

        db.session.commit()

        return True
