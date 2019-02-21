import glob
import numpy as np
from PIL import Image
import h5py


def load_class(class_path):

    print(class_path)
    img_list = glob.glob(class_path)

    print (len(img_list))

    imgs = np.array([np.array(
        Image.open(fname)
        .convert('RGB')
        .resize((64,64), Image.ANTIALIAS)
    ) for fname in img_list[0:900]])

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

    X = np.concatenate((pepe_imgs,other_imgs))
    #print (X)

    print (X.shape)

    Y = np.concatenate((np.ones(pepe_imgs.shape[0]),np.zeros(other_imgs.shape[0])))

    print (Y.shape)

    X, Y = unison_shuffled_copies(X,Y)

    # Save data
    out_file = "data/processed/dataset.h5"    

    h5f = h5py.File(out_file, 'w')
    h5f.create_dataset('X', data=X)
    h5f.create_dataset('Y', data=Y)
    h5f.close()
    


