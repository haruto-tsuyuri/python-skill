import os
import sys

import numpy as np
from PIL import Image

from mnist import load_mnist

sys.path.append(os.pardir)


def img_show(img):
    pil_img = Image.fromarray(np.uint8(img))
    pil_img.show()


(x_train, t_train), (x_test, t_test) = \
    load_mnist(flatten=True, normalize=False)

img = x_train[0]
label = t_train[0]
print(label)
img = img.reshape(28, 28)
img_show(img)
