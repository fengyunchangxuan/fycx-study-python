import numpy as np
import cv2 as cv

# # 鼠标回调函数
# # def draw_circle(event, x, y, flags, param):
# #     if event == cv.EVENT_LBUTTONDBLCLK:
# #         cv.circle(img, (x, y), 100, (255, 0, 0), -1)

# drawing = False # 如果按下鼠标，则为真
# mode = True # 如果为真，绘制矩形。按 m 键可以切换到曲线
# ix,iy = -1,-1
# # 鼠标回调函数
# def draw_circle(event,x,y,flags,param):
#     global ix,iy,drawing,mode
#     if event == cv.EVENT_LBUTTONDOWN:
#         drawing = True
#         ix,iy = x,y
#     elif event == cv.EVENT_MOUSEMOVE:
#         if drawing == True:
#             if mode == True:
#                 cv.rectangle(img,(ix,iy),(x,y),(0,255,0),-1)
#             else:
#                 cv.circle(img,(x,y),5,(0,0,255),-1)
#     elif event == cv.EVENT_LBUTTONUP:
#         drawing = False
#         if mode == True:
#             cv.rectangle(img,(ix,iy),(x,y),(0,255,0),-1)
#         else:
#             cv.circle(img,(x,y),5,(0,0,255),-1)

# # 创建一个黑色的图像，一个窗口，并绑定到窗口的功能
# img = np.zeros((512, 512, 3), np.uint8)
# cv.namedWindow('image')
# # cv.setMouseCallback('image', draw_circle)
# cv.setMouseCallback('image', draw_circle)
# while(1):
#     cv.imshow('image', img)
#     if cv.waitKey(20) & 0xFF == 27:
#         break
# cv.destroyAllWindows()

def nothing(x):
    pass
# 创建一个黑色的图像，一个窗口
img = np.zeros((300,512,3), np.uint8)
cv.namedWindow('image')
# 创建颜色变化的轨迹栏
cv.createTrackbar('R','image',0,255,nothing)
cv.createTrackbar('G','image',0,255,nothing)
cv.createTrackbar('B','image',0,255,nothing)
# 为 ON/OFF 功能创建开关
switch = '0 : OFF \n1 : ON'
cv.createTrackbar(switch, 'image',0,1,nothing)
while(1):
    cv.imshow('image',img)
    k = cv.waitKey(1) & 0xFF
    if k == 27:
        break
    # 得到四条轨迹的当前位置
    r = cv.getTrackbarPos('R','image')
    g = cv.getTrackbarPos('G','image')
    b = cv.getTrackbarPos('B','image')
    s = cv.getTrackbarPos(switch,'image')
    if s == 0:
        img[:] = 0
    else:
        img[:] = [b,g,r]
cv.destroyAllWindows()




