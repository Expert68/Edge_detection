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

p = Sobel_processing('1.png')
p.imgshow()
