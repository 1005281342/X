# coding = <utf-8>

"""
here is an example for SIGNS data load and visualize

训练集: 1080张彩色图片（RGB），每张图64×64像素，手势对应数值[0~5]（均匀分布）.
测试集: 120张彩色图片（RGB），每张图64×64像素，手势对应数值[0~5]（均匀分布）.
"""
import math
import h5py
import scipy.misc
import numpy as np
import matplotlib.pyplot as plt


def load_dataset():
    """
    SIGNS data loading

    @return: train_set_x_orig, train_set_y_orig, test_set_x_orig, test_set_y_orig, classes
    """
    train_dataset = h5py.File('datasets/train_signs.h5', "r")
    train_set_x_orig = np.array(train_dataset["train_set_x"][:])  # train set features
    train_set_y_orig = np.array(train_dataset["train_set_y"][:])  # train set labels

    test_dataset = h5py.File('datasets/test_signs.h5', "r")
    test_set_x_orig = np.array(test_dataset["test_set_x"][:])  # test set features
    test_set_y_orig = np.array(test_dataset["test_set_y"][:])  # test set labels

    classes = np.array(test_dataset["list_classes"][:])  # the list of classes

    train_set_y_orig = train_set_y_orig.reshape((1, train_set_y_orig.shape[0]))
    test_set_y_orig = test_set_y_orig.reshape((1, test_set_y_orig.shape[0]))

    return train_set_x_orig, train_set_y_orig, test_set_x_orig, test_set_y_orig, classes


X_train_orig, Y_train_orig, X_test_orig, Y_test_orig, classes = load_dataset()


def get_picture(index: int=1, how_many: int=1, test_db=True):
    m = index-1
    n = m + how_many

    img_x = X_test_orig[m:n]
    img_y = Y_test_orig[0, m:n]
    if test_db:
        if index+how_many > 120:
            raise Exception("只有120张验证图片")
    else:
        img_x = X_train_orig[m:n]
        img_y = Y_train_orig[0, m:n]
        if index+how_many > 1080:
            raise Exception("只有1080张训练图片")

    n_x = int(math.sqrt(how_many))
    n_y = how_many // n_x

    for i in range(n - m):
        plt.subplot(n_x, n_y, i + 1)
        plt.axis("off")
        plt.imshow(img_x[i])
        plt.title('label=%d' % (img_y[i]))
    plt.show()

    return img_x


if __name__ == '__main__':

    # load data
    # print("X_test_orig", X_test_orig)
    # print("Y_train_orig", Y_train_orig)
    # print("X_test_orig", X_test_orig)
    # print("Y_test_orig", Y_test_orig)
    # print("classes", classes)
    # display some (10 images)
    a = math.sqrt(20)
    print(a)
    get_picture(110, 8, False)  # 使用训练集， 第110张图片起共8张图片
    get_picture(110, 8, True)  # 使用测试集， 第110张图片起共8张图片

    x = get_picture(1, 1)
    print(type(x))
    image_raw = scipy.misc.imread('test.png')
    print(type(image_raw))
    # print(x == image_raw)

    # m = 110
    # n = m + 1
    # img_x = X_test_orig[m:n]
    # img_y = Y_test_orig[0, m:n]
    # # display
    # for i in range(n-m):
    #     plt.subplot(1, 1, i + 1)
    #     plt.axis("off")
    #     plt.imshow(img_x[i])
    #     plt.title('label=%d' % (img_y[i]))
    # plt.show()

    print(" - PY131 - ")
