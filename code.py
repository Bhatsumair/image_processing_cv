import cv2
import numpy
pic = numpy.zeros([300,300,3])
head = cv2.circle(pic,(150,60), 50, (0,255,0), -1)
eye = cv2.circle(pic,(180,45), 8, (0,0,0), -1)
mouth = cv2.line(pic,(180,90),(220,90),(0,0,0),5)
cv2.imshow('mypic', pic)
cv2.waitKey()
cv2.destroyAllWindows()
#Take 2 images and combine them to form a single image. For example collage.
import pandas
import cv2
img1 = cv2.resize(cv2.imread('tom.png'), (300,300))
cv2.imshow('mypic', img1)
cv2.waitKey()
cv2.destroyAllWindows()
img2 = cv2.resize(cv2.imread('jerry.png'),(300,300))
cv2.imshow('mypic', img2)
cv2.waitKey()
cv2.destroyAllWindows()
image = numpy.hstack((img1,img2))
cv2.imshow('mypic', image)
cv2.waitKey()
cv2.destroyAllWindows()
image.shape
(300, 600, 3)
#Take 2 images crop some parts of both images and swap them.
pic = numpy.copy(image)
pic[0:150,90:190] = image[0:150,370:470]
pic[0:150,370:470] = image[0:150,90:190]
cv2.imshow('mypic', pic)
cv2.waitKey()
cv2.destroyAllWindows()