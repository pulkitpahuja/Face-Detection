import cv2
cv2.__version__
cap=cv2.VideoCapture(0)
font=cv2.FONT_HERSHEY_SIMPLEX

while True:
    _,frame=cap.read()
    frame=cv2.resize(frame,(500,500))
    cv2.imshow("frame",frame)
    cv2.line(frame,(0,0),(150,150),(255,255,255),15)
##    cv2.rectangle(frame,(20,20),(40,40),(0,0,0),4)
    cv2.putText(frame,"hi",(100,100),font,2,(0,0,0),4,cv2.LINE_AA)
    if cv2.waitKey(1) & 0xFF==ord('q'):
        break

cv2.destroyAllWindows()
