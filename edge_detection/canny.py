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

p = Canny_processing('1.png')
p.imgshow()