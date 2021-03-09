import cv2
import numpy as np

krnl = np.ones((7,7), np.uint8)                 # Defining a kernel

''' COMMENT / UNCOMMENT EVERY TASK TO MAKE IT RUN '''
# ----------------------
# 1. FILTERS & EFFECTS
# ----------------------

# Showing original image
img = cv2.imread('logo.jpg')

# Grayscaled image
imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Blurred image
imgBlur = cv2.GaussianBlur(imgGray, (7,7), 0)                       # Only use odd number matrix

# Showing edges of the image
imgCanny = cv2.Canny(img, 100, 100)                                 # Edge detection

# To make edges thicker
imgDilate = cv2.dilate(imgCanny, krnl, iterations=5)

# To make edges thinner
imgErode = cv2.erode(imgDilate, krnl, iterations=9)


# cv2.imshow('Main Image', img)
# cv2.imshow('Gray Scaled', imgGray)
# cv2.imshow('Blurred', imgBlur)
# cv2.imshow('Canny', imgCanny)
# cv2.imshow('Dilated', imgDilate)
# cv2.imshow('Eroded', imgErode)


# -------------------
# 2. LINES & SHAPES
# -------------------
# img0 = np.zeros((512, 512, 3), np.uint8)            # Black BG; (512, 512, 3) indicates 512x512 image size with 3 channels(RGB)
# img1 = np.ones((512, 512))                          # White BG, (512, 512) indicates 512x512 image size with no channels(Hence, Black and White)
#
# cv2.line(img0, (0,0), (400,400), (0,255,0), 3)
# cv2.rectangle(img0, (100, 100), (300, 300), (0, 0, 255), cv2.FILLED)
# cv2.circle(img0, (100,100), 50, (255,255,0), cv2.FILLED)
# cv2.putText(img0, 'Shapes', (200, 50), cv2.FONT_HERSHEY_COMPLEX, 1, (100,150,100), 2)

# cv2.line(img1, (0,0), (400,400), (0,255,0), 3)
# cv2.rectangle(img1, (100, 100), (300, 300), (0, 0, 255), cv2.FILLED)
# cv2.circle(img1, (100,100), 50, (0,0,255), cv2.FILLED)
# cv2.putText(img1, 'Shapes', (200, 50), cv2.FONT_HERSHEY_COMPLEX, 1, (100,150,100), 2)


# cv2.imshow('0', img0)
# cv2.imshow('1', img1)


# ---------
# 3. WARP
# ---------
# img = cv2.imread('img.jpg')
#
# width, height = 250, 350
# pts1 = np.float32([[135,120], [265,120], [135,300], [265,300]])
# pts2 = np.float32([[0,0], [width,0], [0,height], [width,height]])
#
# matrix = cv2.getPerspectiveTransform(pts1, pts2)
#
# final = cv2.warpPerspective(img, matrix, (width,height))
#
# cv2.imshow('Main', img)
# cv2.imshow('Final', final)


# ------------------------
# 4. COLOR DETECTION
# ------------------------
# Webcam
cap = cv2.VideoCapture(0)       # 0: Default webcam; 1/2/3/...: External cameras


# Creating Trackbar
def hey():                      # Creating blank function
    pass


# cv2.namedWindow('TrackBars')
# # cv2.resizeWindow('TrackBars', 640, 240)
# cv2.createTrackbar('Hue Min', 'TrackBars', 0, 179, hey)
# cv2.createTrackbar('Hue Max', 'TrackBars', 50, 179, hey)
# cv2.createTrackbar('Sat Min', 'TrackBars', 0, 255, hey)
# cv2.createTrackbar('Sat Max', 'TrackBars', 255, 255, hey)
# cv2.createTrackbar('Val Min', 'TrackBars', 50, 255, hey)
# cv2.createTrackbar('Val Max', 'TrackBars', 255, 255, hey)


# --------------------------
# 5. CONTOURS & SHAPES
# --------------------------
# def getContours(image):
#     contours, hierarchy = cv2.findContours(image, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
#
#     for cnt in contours:
#         area = cv2.contourArea(cnt)
#         print(cnt, area)
#         cv2.drawContours(imgC, cnt, -1, (255,0,0), 3)
#
#
# main = cv2.imread('s1.jpg')
# img = cv2.resize(main, (300, 300))
# imgC = img.copy()
# imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
# imgBlur = cv2.GaussianBlur(imgGray, (7,7), 1)
# imgCanny = cv2.Canny(imgGray, 200, 200)
#
# getContours(imgCanny)
#
# cv2.imshow('Main', img)
# cv2.imshow('Gray', imgGray)
# cv2.imshow('Blur', imgBlur)
# cv2.imshow('Edges', imgCanny)
# cv2.imshow('Main C', imgC)


while True:
    '''UNCOMMENT THIS TO USE WITH TASK 4'''
    # ----------------------------------------
    # success, img = cap.read()
    # img = cv2.flip(img, 1)
    #
    # imgHSV = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    #
    # hmin = cv2.getTrackbarPos('Hue Min', 'TrackBars')
    # hmax = cv2.getTrackbarPos('Hue Max', 'TrackBars')
    # smin = cv2.getTrackbarPos('Sat Min', 'TrackBars')
    # smax = cv2.getTrackbarPos('Sat Max', 'TrackBars')
    # vmin = cv2.getTrackbarPos('Val Min', 'TrackBars')
    # vmax = cv2.getTrackbarPos('Val Max', 'TrackBars')
    #
    # lower = np.array([hmin, smin, vmin])
    # upper = np.array([hmax, smax, vmax])
    # mask = cv2.inRange(imgHSV, lower, upper)
    # result = cv2.bitwise_and(img, img, mask=mask)
    #
    # cv2.imshow('Main', img)
    # cv2.imshow('HSV', imgHSV)
    # cv2.imshow('Mask', mask)
    # cv2.imshow('Result', result)
    # ----------------------------------------

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

    cv2.waitKey(1)


# Releasing camera and all other resources
cap.release()
cv2.destroyAllWindows()



