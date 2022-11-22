## This project was developed by SKKU Smart Construction Lab directed by Professor SH Sim. which was sponsored by KEPCO E&C Smart Convergence Lab.

# 'deeplabCustom'
* 'deeplabCustom' is designed to perform the semantic segmentation of images based on the Model Garden for TensorFlow (https://github.com/tensorflow/models).
* In particular, 'deeplabCustom' provides a couple of functions, which can be utilized to effectively train and test the semantic segmentation network.
* Before using them, please install all the required libraries (https://github.com/tensorflow/models/blob/master/research/deeplab/g3doc/installation.md).

# Description
* 'deeplabCustomTrain.py' is used to train the semantic segmentation model.
* 'deeplabCustomTest.py' is used to test the trained model.

# Requirement
* We first need to add libraries to PYTHONPATH in './models/research'.
  * $ export PYTHONPATH=$PYTHONPATH:`pwd`:`pwd`/slim
* All the files in a folder 'deeplab' need to overwrite the original data in the following directory:
  * './models/research/deeplab'
* All the files in a folder 'utils' need to overwrite the original data in the following directory:
  * './models/research/deeplab/utils'
* All the files in a folder 'datasets' need to overwrite the original data in the following directory:
  * './models/research/deeplab/datasets'
* All the files in a folder 'trainSet' need to be located in the following directory:
  * './models/research/deeplab/datasets/trainSet'
* All the files in a folder 'testSet' need to be located in the following directory:
  * './models/research/deeplab/datasets/testSet'

# Customization
* In deeplabCustom, all the images are divided into a set of sub-images with a fixed size of 224 x 224, from which 60%, 20%, and 20% of the dataset are extracted for training, validation, and testing stages, respectively. Thus, please change the number of images for your custom dataset.
  * In 'deeplabCustomTrain.py': './models/research/deeplab/datasets/data_generator.py'
  * In 'deeplabCustomTest.py': './models/research/deeplab/datasets/data_generator_test.py'
* The pretrained models can be downloaded (https://github.com/tensorflow/models/blob/master/research/deeplab/g3doc/model_zoo.md), which must be located in the following directory.
  * './models/research/deeplab'

# Environment
* 'deeplabCustom' is tested on the following environment:

Content|Version
---|---|
Ubuntu|18.04.6 LTS|
Python|3.6.9|
CUDA|10.0|
CUDNN|7.6.0|
Tensorflow|1.15.0|

# Example
* 'deelabCustom' is used for the semantic segmentation of concrete cracks in a set of images taken by the unmanned aerial vehicle (UAV).

![Example](https://user-images.githubusercontent.com/99420897/153723508-aaba8d59-7d8f-40a2-baa0-ae0e3efc1368.jpg)
