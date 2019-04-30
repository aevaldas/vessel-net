class DataLoaderBase(object):
    """
    Base class for data loading
    """

    def __init__(self, config):
        self.config = config  # 设置配置信息

    def prepare_dataset(self):
        """
        Convert raw data to hdf5 format
        """
        raise NotImplementedError

    def get_train_data(self):
        """
        Get training data
        """
        raise NotImplementedError

    def get_val_data(self):
        """
        Get verification data
        """
        raise NotImplementedError
