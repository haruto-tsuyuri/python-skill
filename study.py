import multiprocessing as mp
import numpy as np
from matplotlib import pyplot as plt
import matplotlib as mpq
import cv2

from pathlib import Path

p = Path()
img_path = p.glob('data/*.jpg')
images = []
print(img_path)
for index, path in enumerate(img_path, start=0):
    print(path)
    images.append(cv2.imread(str(path), cv2.IMREAD_COLOR))
    images[index] = cv2.resize(images[index], (300, 300))
    new_path = str(p.joinpath(path))
    cv2.imwrite(p.joinpath(path), images[index])
