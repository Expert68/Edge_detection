# Edge_detection
### 效果可以看我的知乎：https://zhuanlan.zhihu.com/p/44855115
    最近一直忙着提取物体轮廓的相关算法问题，这里就说一下提取物体轮廓的常用的三种方法：sobel算子边缘检测，canny算子边缘检测，以及laplacian算子边缘检测。

这几个算子的原理就不在这里讲解了，可以在百度百科中搜索，讲的蛮详细的，话不多说，直接上代码才是最实在的：

**sobel算子边缘检测：**
```
import cv2
class Sobel_processing:
    def __init__(self, imgfile):
        self.imgfile = imgfile
        self.img = self.sobel_processing()

    def sobel_processing(self):
        img = cv2.imread(self.imgfile, 1)
        imgInfo = img.shape
        height = imgInfo[0]
        width = imgInfo[1]
        cv2.imshow('src', img)
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        gray = cv2.GaussianBlur(gray, (3, 3), 0)
        sobelX = cv2.Sobel(img,cv2.CV_64F,1,0) #X方向的梯度
        sobelY = cv2.Sobel(img,cv2.CV_64F,0,1) #Y方向的梯度
        sobelCombined = cv2.bitwise_or(sobelX,sobelY)
        return sobelCombined

    def imgshow(self):
        cv2.imshow('img', self.img)
        cv2.waitKey(0)
        cv2.destroyAllWindows()

    def save(self,dst_file):
        cv2.imwrite(dst_file, self.img, [cv2.IMWRITE_PNG_COMPRESSION, 0])
        print('save finished')
```
**canny算子边缘检测：**
```
import cv2
class Canny_processing:
    def __init__(self, imgfile):
        self.imgfile = imgfile
        self.img = self.canny_processing()

    def canny_processing(self):
        img = cv2.imread(self.imgfile, 1)
        imgInfo = img.shape
        height = imgInfo[0]
        width = imgInfo[1]
        cv2.imshow('src', img)
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        gray = cv2.GaussianBlur(gray, (3, 3), 0)  #一般都需要做一个blur
        dst = cv2.Canny(img,100,100)
        return dst

    def imgshow(self):
        cv2.imshow('img', self.img)
        cv2.waitKey(0)
        cv2.destroyAllWindows()

    def save(self,dst_file):
        cv2.imwrite(dst_file, self.img, [cv2.IMWRITE_PNG_COMPRESSION, 0])
        print('save finished')
```
**laplacian算子边缘检测：**
```
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
        gray = cv2.GaussianBlur(gray, (3, 3), 0)
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
```

