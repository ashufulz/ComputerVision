import cv2
import numpy as np

filename = r'C:\Users\AshutoshFulzele\PycharmProjects\AshProjects\Assets\Videos\CityDriving_4.mp4'  # VT: 4,5,7
cap = cv2.VideoCapture(filename)


def nothing(x):
    pass


cv2.namedWindow('Trackbars')

cv2.createTrackbar('L-H', 'Trackbars', 0, 179, nothing)
cv2.createTrackbar('U-H', 'Trackbars', 0, 179, nothing)
cv2.createTrackbar('L-S', 'Trackbars', 0, 255, nothing)
cv2.createTrackbar('U-S', 'Trackbars', 0, 255, nothing)
cv2.createTrackbar('L-V', 'Trackbars', 0, 255, nothing)
cv2.createTrackbar('U-V', 'Trackbars', 0, 255, nothing)



if __name__ == '__main__':
    while True:
        ret, frame = cap.read()

        if not ret:
            # filename = r'C:\Users\AshutoshFulzele\PycharmProjects\AshProjects\Assets\Videos\CityDriving_3.mp4'  # VT: 4,5,7
            # cap = cv2.VideoCapture(filename)
            continue

        frame = cv2.resize(frame, (1800, 1000))

        hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

        l_h = cv2.getTrackbarPos('L-H', 'Trackbars')
        l_s = cv2.getTrackbarPos('L-S', 'Trackbars')
        l_v = cv2.getTrackbarPos('L-V', 'Trackbars')
        u_h = cv2.getTrackbarPos('U-H', 'Trackbars')
        u_s = cv2.getTrackbarPos('U-S', 'Trackbars')
        u_v = cv2.getTrackbarPos('U-V', 'Trackbars')

        lower = np.array([l_h, l_s, l_v])
        upper = np.array([u_h, u_s, u_v])

        mask = cv2.inRange(hsv, lower, upper)

        result = cv2.bitwise_and(frame, frame, mask=mask)


        cv2.imshow('main', frame)
        cv2.imshow('mask', mask)
        cv2.imshow('result', result)

        if cv2.waitKey(0) & 0xFF == ord('q'):
            cap.release()
            break

    cv2.destroyAllWindows()
