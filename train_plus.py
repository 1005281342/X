# Importing the Keras libraries and packages
from keras.models import Sequential
from keras.layers import Convolution2D
from keras.layers import MaxPooling2D
from keras.layers import Flatten
from keras.layers import Dense

# 初始化CNN
classifier = Sequential()

# 输入 卷积
classifier.add(Convolution2D(32, (3, 3), padding="valid", input_shape=(64, 64, 1), activation='relu'))
# 池化
classifier.add(MaxPooling2D(pool_size=(2, 2)))

# 卷积
classifier.add(Convolution2D(32, (3, 3), activation='relu'))

# 池化
classifier.add(MaxPooling2D(pool_size=(2, 2)))

# 扁平化
classifier.add(Flatten())

# 全连接
classifier.add(Dense(units=64, activation='relu'))
classifier.add(Dense(units=6, activation='softmax'))

# Compiling the CNN
classifier.compile(optimizer='adam', loss='categorical_crossentropy',
                   metrics=['accuracy'])  # categorical_crossentropy for more than 2

# Step 2 - Preparing the train/test data and training the model

# Code copied from - https://keras.io/preprocessing/image/
if __name__ == '__main__':

    from keras.preprocessing.image import ImageDataGenerator

    # 读取训练集
    train_datagen = ImageDataGenerator(
        rescale=1. / 255,
        shear_range=0.2,
        zoom_range=0.2,
        horizontal_flip=True)

    training_set = train_datagen.flow_from_directory('data/train',
                                                     target_size=(64, 64),
                                                     batch_size=5,
                                                     color_mode='grayscale',
                                                     class_mode='categorical')

    # 读取测试集
    test_datagen = ImageDataGenerator(rescale=1. / 255)

    test_set = test_datagen.flow_from_directory('data/test',
                                                target_size=(64, 64),
                                                batch_size=5,
                                                color_mode='grayscale',
                                                class_mode='categorical')
    # 拟合
    classifier.fit_generator(
        training_set,
        steps_per_epoch=600,
        epochs=6,
        validation_data=test_set,
        validation_steps=30)

    # 保存模型
    model_json = classifier.to_json()
    with open("model-bw.json", "w") as json_file:
        json_file.write(model_json)
    classifier.save_weights('model-bw.h5')
