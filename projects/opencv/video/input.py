import cv2 as cv

cap = cv.VideoCapture(0)

# 创建VideoWriter对象
fourcc = cv.VideoWriter_fourcc(*'MJPG')
out = cv.VideoWriter('videos/test1.mp4',fourcc,10.0,(640,480),True)
while cap.isOpened():
    ret,frame = cap.read()
    if not ret:
        print('无法打开摄像头')
        break
    frame = cv.flip(frame,0)
    out.write(frame)
    cv.imshow('frame',frame)
    if cv.waitKey(1) == ord('q'):
        break


cap.release()
out.release()
cv.destroyAllWindows()
