class TrainerBase(object):
    """
    Trainer base class
    """

    def __init__(self, model, data, config):
        self.model = model  # 模型
        self.data = data  # 数据
        self.config = config  # 配置

    def train(self):
        """
        Training logic
        """
        raise NotImplementedError
