import cv2
import numpy as np

class Laplacian_processing:
    def __init__(self, imgfile):
        self.imgfile = imgfile
        self.img = self.laplacian_processing()

    def laplacian_processing(self):
        img = cv2.imread(self.imgfile, 1)
        imgInfo = img.shape
        height = imgInfo[0]
        width = imgInfo[1]
        cv2.imshow('src', img)
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        dst = cv2.Laplacian(img,cv2.CV_64F)
        dst = np.uint8(np.absolute(dst))
        return dst

    def imgshow(self):
        cv2.imshow('img', self.img)
        cv2.waitKey(0)
        cv2.destroyAllWindows()

    def save(self,dst_file):
        cv2.imwrite(dst_file, self.img, [cv2.IMWRITE_PNG_COMPRESSION, 0])
        print('save finished')

p = Laplacian_processing('1.png')
p.imgshow()