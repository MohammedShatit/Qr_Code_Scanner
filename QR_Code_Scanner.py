#importing libraries
import cv2
import numpy as np
from pyzbar.pyzbar import decode

cap = cv2.VideoCapture(0) #capturing from the video input
cap.set(3,640) #setting the window size
cap.set(4,480)
#img = cv2.imread('QrCode.jpg') #used for decoding a qr/bar code from an image

while True:
    ret, frame = cap.read() #recieving frames from the video input
    for code in decode(frame): #decode method of pyzbar lib
        data = code.data.decode('utf-8')

        vertices = np.array([code.polygon], np.int32) #getting the qr/bar coordinates
        vertices = vertices.reshape((-1,1,2))
        cv2.polylines(frame, [vertices], True, (255,0,0), 5) #drawing a rectangle around the code
        pts = code.rect
        font = cv2.FONT_HERSHEY_SIMPLEX
        cv2.putText(frame, data, (pts[0], pts[1]), font, 0.9, (255,0,0), 2) #showing the decoded message on top

    cv2.imshow('QRcodeScanner', frame) #displaying the video
    if cv2.waitKey(1) == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()