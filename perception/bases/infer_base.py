class InferBase(object):
    """
    Inferred base class
    """

    def __init__(self, config):
        self.config = config  # 配置

    def load_model(self, name):
        """
        Loading model
        """
        raise NotImplementedError

    def predict(self, data):
        """
        forecast result
        """
        raise NotImplementedError
