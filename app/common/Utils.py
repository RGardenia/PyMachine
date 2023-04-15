'''
    工具类，封装通用方法
'''
from app.common.GardeniaEncoder import GardeniaEncoder
import time, json, datetime, array
from app.config.env import Config
from app.common.Code import Code
from sqlalchemy import DateTime
import os


class Utils:

    @staticmethod
    def withModel(pic_path):
        import torch.nn.functional as F
        import numpy as np
        import torch

        model = 'resnet101-0.914.pth'
        device = torch.device('cuda:0' if torch.cuda.is_available() else 'cpu')
        idx_to_labels = np.load(os.path.join(Config.BASE_DIR, 'dataset') + '\\idx_to_labels.npy',
                                allow_pickle=True).item()

        # 载入最佳模型作为当前模型
        model = torch.load(os.path.join(Config.BASE_DIR, 'checkpoints') + '\\' + model)
        model = model.eval().to(device)
        from torchvision import transforms

        # 测试集图像预处理-RCTN：缩放、裁剪、转 Tensor、归一化
        test_transform = transforms.Compose([transforms.Resize(256),
                                             transforms.CenterCrop(224),
                                             transforms.ToTensor(),
                                             transforms.Normalize(
                                                 mean=[0.485, 0.456, 0.406],
                                                 std=[0.229, 0.224, 0.225])
                                             ])
        from PIL import Image
        img_path = pic_path
        img_pil = Image.open(img_path)

        input_img = test_transform(img_pil)  # 预处理
        input_img = input_img.unsqueeze(0).to(device)
        labelList = list(idx_to_labels.values())  # 获取 类别列表

        # 执行前向预测，得到所有类别的 logit 预测分数
        pred_logits = model(input_img)
        pred_softmax = F.softmax(pred_logits, dim=1)  # 对 logit 分数做 softmax 运算
        top_n = pred_softmax.cpu().detach().numpy()[0] * 100

        result = np.array(top_n, dtype='int')

        res = np.argmax(result)
        label = labelList[res]
        print(label)

        return label

    @staticmethod
    def dict_to_json(dict_obj):
        return json.dumps(dict_obj, cls=GardeniaEncoder, indent=4)

    ''' 
    * 用于sql结果列表对象类型转字典
    * @param list data
    * @return dict
    '''

    @staticmethod
    def db_l_to_d(data):
        data_list = []
        for val in data:
            val_dict = val.to_dict()
            data_list.append(val_dict)
        data = {}
        data = data_list
        return data

    ''' 
    * 用于sql结果对象类型转字典
    * @param object obj
    * @return dict
    '''

    @staticmethod
    def class_to_dict(obj):
        '''把对象(支持单个对象、list、set)转换成字典'''
        is_list = obj.__class__ == [].__class__
        is_set = obj.__class__ == set().__class__
        if is_list or is_set:
            obj_arr = []
            for o in obj:
                # 把Object对象转换成Dict对象
                dict = {}
                dict.update(o.__dict__)
                obj_arr.append(dict)
                return obj_arr
        else:
            dict = {}
            dict.update(obj.__dict__)
            return dict

    """ 验证文件类型
        @param string filename
        return string path
    """

    @staticmethod
    def allowed_file(filename):
        return '.' in filename and \
               filename.rsplit('.', 1)[1] in Config.ALLOWED_EXTENSIONS

    """ uuid,唯一id 
        return string id
    """

    @staticmethod
    def unique_id(prefix=''):
        return prefix + hex(int(time.time()))[2:10] + hex(int(time.time() * 1000000) % 0x100000)[2:7]

    """ 确保 文件夹存在
        return bool
    """

    @staticmethod
    def makeSurePath(strPath):
        import os
        path = strPath.strip().rstrip("\\")
        # 判断路径是否存在
        isExists = os.path.exists(path)
        if isExists:
            return True
        try:
            os.makedirs(path)
        except IOError:
            print("Path is not accessible.")
            return False
        return True
