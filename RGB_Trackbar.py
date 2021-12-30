import cv2
import numpy as np

filename = r'C:\Users\AshutoshFulzele\PycharmProjects\AshProjects\Assets\Videos\CityDriving_4.mp4'  # VT: 4,5,7
cap = cv2.VideoCapture(filename)


def nothing(x):
    pass


cv2.namedWindow('Trackbars')

cv2.createTrackbar('L-R', 'Trackbars', 0, 255, nothing)
cv2.createTrackbar('U-R', 'Trackbars', 0, 255, nothing)
cv2.createTrackbar('L-G', 'Trackbars', 0, 255, nothing)
cv2.createTrackbar('U-G', 'Trackbars', 0, 255, nothing)
cv2.createTrackbar('L-B', 'Trackbars', 0, 255, nothing)
cv2.createTrackbar('U-B', 'Trackbars', 0, 255, nothing)



if __name__ == '__main__':
    while True:
        ret, frame = cap.read()

        if not ret:
            # filename = r'C:\Users\AshutoshFulzele\PycharmProjects\AshProjects\Assets\Videos\CityDriving_3.mp4'  # VT: 4,5,7
            # cap = cv2.VideoCapture(filename)
            continue

        frame = cv2.resize(frame, (1000, 800))

        rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

        l_r = cv2.getTrackbarPos('L-R', 'Trackbars')
        l_g = cv2.getTrackbarPos('L-G', 'Trackbars')
        l_b = cv2.getTrackbarPos('L-B', 'Trackbars')
        u_r = cv2.getTrackbarPos('U-R', 'Trackbars')
        u_g = cv2.getTrackbarPos('U-G', 'Trackbars')
        u_b = cv2.getTrackbarPos('U-B', 'Trackbars')

        lower = np.array([l_r, l_g, l_b])
        upper = np.array([u_r, u_g, u_b])

        mask = cv2.inRange(rgb, lower, upper)

        result = cv2.bitwise_and(frame, frame, mask=mask)


        cv2.imshow('main', frame)
        cv2.imshow('mask', mask)
        cv2.imshow('result', result)

        if cv2.waitKey(10) & 0xFF == ord('q'):
            cap.release()
            break

    cv2.destroyAllWindows()
