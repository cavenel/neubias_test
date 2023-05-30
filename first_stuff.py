from skimage import imread
from skimage.filters import threshold_otsu
from skimage.measure import label

def otsu_labeling(image):
    thresh = threshold_otsu(image)
    binary = image > thresh
    label = label(binary)
    return label