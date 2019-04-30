# VesselNet
A DenseBlock-Unet for Retinal Blood Vessel Segmentation

![TestResult](https://i.imgur.com/pPMANyZ.jpg)

- [Project Structure](#project-structure)
    - [First to run](#first-to-run)
    - [Pretrained Model](#pretrained-model)
    - [Test your own image](#test-your-own-image)
- [Reference](#reference)

## Result Evaluation
Tried With 40 images of DRIVE dataset and DenseBlock-Unet model.
Results on DRIVE database:

|Methods|AUC ROC on DRIVE|
|-:|-:|
|Liskowski|0.9790|
|Retina-Unet|0.9790|
|VesselNet|0.9841|

## Project Structure
You can find model parameter in **configs/segmention_config.json**.

### First to run
**please run main_trainer.py first time**, then you will get data_route in experiment dir. Put your data in there, now you can run `main_trainer.py` again to train a model. 

### Pretrained Model
The model is trained with *DRIVE dataset* on my own desktop (intel i7-7700hq,24g,gtx1050 2g) within 30 minutes.
Dataset and pretrained model can be found [here][2]. For Chinese, you can download [here][6].

### Test your own image
If u want to test your own image, put ur image to **(VesselNet)/test/origin**, and change the img_type of predict settings in **configs/segmention_config.json**, run `main_test.py` to get your result. The result is in **(VesselNet)/test/result**

## Reference
This project is based on the following 2 papers:

[U-Net: Convolutional Networks for Biomedical Image Segmentation](8)

[Densely Connected Convolutional Networks](7)

[2]: https://drive.google.com/file/d/1RALItn7a-XIe-ebsghk6HL-T0btJI9w7/view?usp=sharing
[3]: https://arxiv.org/pdf/1608.06993.pdf
[4]: https://github.com/liuzhuang13/DenseNet 
[5]: https://github.com/orobix/retina-unet
[6]: https://pan.baidu.com/s/1EnKeNTGimzVRa9QedWjxlg
[7]: https://arxiv.org/pdf/1608.06993.pdf
[8]: https://arxiv.org/pdf/1505.04597.pdf



