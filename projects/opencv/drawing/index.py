import numpy as np
import cv2 as cv

# 创建黑色的图像
# img = np.zeros((512, 512, 3), np.uint8)
img = np.zeros((512, 512, 3), np.uint8)
# 绘制一条厚度为5的蓝色对角线
cv.line(img, (0, 0), (511, 511), (255, 0, 0), 5)

# 要绘制矩形，您需要矩形的左上角和右下角。这次，我们将在图像的右上角绘制一个绿色矩形。
cv.rectangle(img, (384, 0), (510, 128), (0, 255, 0), 3)

# 要绘制一个圆，需要其中心坐标和半径。我们将在上面绘制的矩形内绘制一个圆。
cv.circle(img, (447, 63), 63, (0, 0, 255), -1)
