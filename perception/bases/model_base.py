class ModelBase(object):
    """
    Model base class
    """

    def __init__(self, config):
        self.config = config  # Configuration
        self.model = None  # model

    def save(self):
        """
        Store checkpoint, the path is defined in the configuration file
        """
        if self.model is None:
            raise Exception("[Exception] You have to build the model first.")

        print("[INFO] Saving model...")
        json_string = self.model.to_json()
        open(self.config.hdf5_path + self.config.exp_name + '_architecture.json', 'w').write(json_string)
        print("[INFO] Model saved")

    def load(self, checkpoint_path):
        """
        Load checkpoint, the path is defined in the configuration file
        """
        if self.model is None:
            raise Exception("[Exception] You have to build the model first.")

        print("[INFO] Loading model checkpoint ...\n")
        self.model.load_weights(self.config.hdf5_path + self.config.exp_name + '_best_weights.h5')
        print("[INFO] Model loaded")

    def build_model(self):
        """
        Building a model
        """
        raise NotImplementedError
