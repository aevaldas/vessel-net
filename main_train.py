from configs.utils.config_utils import process_config
from experiments.data_loaders.standard_loader import DataLoader
# from infers.simple_mnist_infer import SimpleMnistInfer
from perception.models.dense_unet import SegmentionModel
from perception.trainers.segmention_trainer import SegmentionTrainer


def main_train():
    """
    Training model

    :return:
    """
    print('[INFO] Reading Configs...')

    config = None

    try:
        config = process_config('configs/segmention_config.json')
    except Exception as e:
        print('[Exception] Config Error, %s' % e)
        exit(0)
    # np.random.seed(47)  # 固定随机数

    print('[INFO] Preparing Data...')
    dataloader = DataLoader(config=config)
    dataloader.prepare_dataset()

    train_imgs, train_gt = dataloader.get_train_data()
    val_imgs, val_gt = dataloader.get_val_data()

    print('[INFO] Building Model...')
    model = SegmentionModel(config=config)
    #
    print('[INFO] Training...')
    trainer = SegmentionTrainer(
        model=model.model,
        data=[train_imgs, train_gt, val_imgs, val_gt],
        config=config)
    trainer.train()
    print('[INFO] Finishing...')


if __name__ == '__main__':
    main_train()
    # test_main()
