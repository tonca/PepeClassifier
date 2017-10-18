import glob
import numpy as np
from PIL import Image
from keras.preprocessing.image import ImageDataGenerator
import pickle


def load_class(class_path):

    print(class_path)
    img_list = glob.glob(class_path)

    print (len(img_list))

    imgs = np.array([np.array(
        Image.open(fname)
        .convert('RGB')
        .resize((256,256), Image.ANTIALIAS)
    ) for fname in img_list[0:1000]])

    return imgs

def unison_shuffled_copies(a, b):

    assert len(a) == len(b)
    p = np.random.permutation(len(a))
    
    return a[p], b[p]

if __name__ == '__main__':

    image_path = "data"
    pepe_path = "pepes"
    other_path = "other"

    pepe_imgs = load_class("%s/%s/*" % (image_path, pepe_path))
    print (pepe_imgs.shape)

    other_imgs = load_class("%s/%s/*" % (image_path, other_path))
    print (other_imgs.shape)

    X_train = np.concatenate((pepe_imgs,other_imgs))
    #print (X_train)

    print (X_train.shape)

    Y_train = np.concatenate((np.ones(pepe_imgs.shape[0]),np.zeros(other_imgs.shape[0])))

    print (Y_train)

    X_train, Y_train = unison_shuffled_copies(X_train,Y_train)

    x_file = open("data/processed/X_train.pkl", 'wb')
    y_file = open("data/processed/Y_train.pkl", 'wb')
    
    pickle.dump(X_train, x_file)
    pickle.dump(Y_train, y_file)


