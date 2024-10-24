import cv2
fc=cv2.CascadeClassifier("C:/Users/shash/AppData/Local/Programs/Python/Python313/Lib/site-packages/cv2/data/haarcascade_frontalface_default.xml")
vc=cv2.VideoCapture(0)
while True:
  ret , vi=vc.read()
  # Assuming vi is a Bayer BGGR format image
  col = cv2.cvtColor(vi, cv2.COLOR_BGR2GRAY)
  fcs=fc.detectMultiScale(col,scaleFactor=1.1,minNeighbors=5,minSize=(30,30),flags=cv2.CASCADE_SCALE_IMAGE)
  for(x,y,w,h) in fcs:
    cv2.rectangle(vi,(x,y),(x+w,y+h),(0,255,0),2)
  cv2.imshow("Video_Live",vi)
  if cv2.waitKey(20) == ord("m"):
          break
vc.release()
print(vi.shape)
