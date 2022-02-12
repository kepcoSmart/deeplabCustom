# 'deeplabCustom'
* 'deeplabCustom' is designed to perform the semantic segmentation of images based on the Model Garden for TensorFlow (https://github.com/tensorflow/models).
* In particular, 'deeplabCustom' provides a couple of functions, which can be utilized to effectively train and test the semantic segmentation network.
* Before using them, please install all the required libraries (https://github.com/tensorflow/models/blob/master/research/deeplab/g3doc/installation.md).

# Description
* 'deeplabCustomTrain.py' is used to train the semantic segmentation model.
* 'deeplabCustomTest.py' is used to test the trained model.

# Requirement
* All the files in a folder 'deeplab' needs to overwrite the original data ('./models/research/deeplab').
* All the files in a folder 'utils' needs to overwrite the original data ('./models/research/deeplab/utils').
* All the files in a folder 'datasets' needs to overwrite the original data ('./models/research/deeplab/datasets').
* All the files in a folder 'trainSet' needs to be located in the following directory: './models/research/deeplab/datasets'.
* All the files in a folder 'testSet' needs to be located in the following directory: './models/research/deeplab/datasets'.
* In deeplabCustom, all the images are divided into a set of sub-images with a fixed size of 224 x 224, from which 60%, 20%, and 20% of the dataset are extracted for training, validation, and testing stages, respectively. Thus, please change the number of images for your custom dataset.
  * For 'deeplabCustomTrain.py': './models/research/deeplab/datasets/data_generator.py'
  * For 'deeplabCustomTest.py': './models/research/deeplab/datasets/data_generator_test.py'

# Environment
'deeplabCustom' is tested on the following environment:
Content|Version
---|---|
Ubuntu|18.04.6 LTS|
Python|3.6.9|
CUDA|10.0|
CUDNN|7.6.0|
Tensorflow|1.15.0|
