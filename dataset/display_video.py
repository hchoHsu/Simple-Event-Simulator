import cv2
import sys

cap = cv2.VideoCapture(sys.argv[1])

if (cap.isOpened() == False):
    print('Error opening video stream or file')
# if (cap2.isOpened() == False):
#     print('Error opening video stream or file2')

while(cap.isOpened() ): # and cap2.isOpened()
    ret, frame1 = cap.read()
    if ret == True:
        cv2.imshow('Frame()', frame1)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    else:
        break
    
cap.release()
cv2.destroyAllWindows()