import cv2, time

fc = cv2.CascadeClassifier(r'C:\Users\ashut\PycharmProjects\NumPython\DataScience\Projects\CV\IMP Files\HaarCascades\haarcascade_frontalface_default.xml')

video = cv2.VideoCapture(0)

while True:
    check, frame = video.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    face = fc.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5)

    for x, y, w, h in face:
        img = cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 255), 0)        # 5th param = thickness
        img[y:y+h, x:x+w] = cv2.medianBlur(img[y:y+h, x:x+w], 35)               # 2nd param = blur intensity

    cv2.imshow('Main', frame)
    key = cv2.waitKey(1)
    if key == ord('q'):
        break

video.release()
cv2.destroyAllWindows()







