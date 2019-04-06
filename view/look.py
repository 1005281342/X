from keras.utils import plot_model
from train_plus import classifier

plot_model(model=classifier, to_file='model.png', show_shapes=True)