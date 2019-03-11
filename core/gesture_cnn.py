import os

import cv2
import numpy as np
from PIL import Image
from matplotlib import pyplot as plt
from sklearn.utils import shuffle
from sklearn.model_selection import train_test_split
from keras.models import Sequential
from keras.layers import Dense, Dropout, Activation, Flatten
from keras.layers import Conv2D, MaxPooling2D
from keras.utils import np_utils
from keras import backend as K


if K.backend() == 'tensorflow':
    import tensorflow
    K.set_image_dim_ordering('tf')
else:
    import theano
    K.set_image_dim_ordering('th')  # 'channels_first'


# 输入图像尺寸
img_rows, img_cols = 200, 200

# 选择通道，灰度图片选择1通道，彩色图片选择3通道
img_channels = 1

# 训练集 分批训练大小
batch_size = 32

# 分类种类
nb_classes = 5

# 每个单元被执行次数
nb_epoch = 15

# 要使用的卷积滤波器个数[人工网络神经元]
nb_filters = 32

# 最大池化层
nb_pool = 2

# 卷积内核
nb_conv = 3
