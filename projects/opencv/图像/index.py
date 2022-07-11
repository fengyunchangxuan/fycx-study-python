import cv2 as cv  # opencv库
from matplotlib import pyplot as plt

image = cv.imread('images/yangmi.jpg')

# cv.namedWindow('image', cv.WINDOW_NORMAL)
# cv.imshow('image', image)
# key = cv.waitKey(0)
# if key == 27:
#     cv.destroyAllWindows()
# elif key == ord('s'):
#     cv.imwrite('yangmi.png',image)
#     cv.destroyWindow('image')

plt.imshow(image,cmap='gray',interpolation='bicubic')
plt.xticks([]),plt.yticks([])
plt.show()