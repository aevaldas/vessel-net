# -- coding: utf-8 --
import argparse
import json

import os
from bunch import Bunch

from configs.utils.utils import mkdir_if_not_exist


def get_config_from_json(json_file):
    """
    Convert a configuration file to a configuration class
    change json file to dictionary
    """
    with open(json_file, 'r') as config_file:
        config_dict = json.load(config_file)  # 配置字典

    config = Bunch(config_dict)  # 将配置字典转换为类

    return config, config_dict


def process_config(json_file):
    """
    Parsing Json files
    solve json file
    :param json_file: Configuration file
    :return: Configuration class
    """
    config, _ = get_config_from_json(json_file)
    config.val_groundtruth_path = os.path.join("./experiments", config.exp_name, "dataset/validate/groundtruth/")
    config.val_img_path=os.path.join("./experiments", config.exp_name, "dataset/validate/origin/")
    config.train_groundtruth_path = os.path.join("./experiments", config.exp_name, "dataset/train/groundtruth/")
    config.train_img_path = os.path.join("./experiments", config.exp_name, "dataset/train/origin/")
    config.hdf5_path = os.path.join("./experiments", config.exp_name, "hdf5/")
    config.checkpoint = os.path.join("./experiments", config.exp_name, "checkpoint/")
    config.test_img_path=os.path.join("./experiments", config.exp_name, "test/origin/")
    config.test_gt_path=os.path.join("./experiments", config.exp_name, "test/groundtruth/")
    config.test_result_path = os.path.join("./experiments", config.exp_name, "test/result/")
    # 创建文件夹
    mkdir_if_not_exist(config.train_img_path)
    mkdir_if_not_exist(config.train_groundtruth_path)
    mkdir_if_not_exist(config.val_img_path)
    mkdir_if_not_exist(config.val_groundtruth_path)
    mkdir_if_not_exist(config.hdf5_path)
    mkdir_if_not_exist(config.checkpoint)
    mkdir_if_not_exist(config.test_img_path)
    mkdir_if_not_exist(config.test_gt_path)
    mkdir_if_not_exist(config.test_result_path)

    return config




