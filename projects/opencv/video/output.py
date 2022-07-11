import cv2 as cv

# cap = cv.VideoCapture(0)
cap = cv.VideoCapture('videos/test1.mp4')

if not cap.isOpened():
    print('无法打开相机')
    exit()

while True:
    # 逐帧捕获
    ret, frame = cap.read()
    if not ret:
        print('错误')
        break
    # 我们在框架上的操作到这里
    gray = cv.cvtColor(frame, cv.COLOR_RGB2GRAY)
    # 显示结果帧
    cv.imshow('frame', gray)
    if cv.waitKey(1) == ord('q'):
        break
cap.release()
cv.destroyAllWindows()