
"""
Eye Landmarks:
        37      38                          43      44
    36      L       39                  42      R       45
        41      40                          47      46


        p2      p3                      Eye-Aspect-Ratio
    p1              p4                  (||p2-p6|| + ||p3-p5||) / 2 * ||p1-p4||
        p6      p5

"""

import cv2
import dlib
import numpy as np
from imutils import face_utils

faceLandmarks = r'C:\Users\ashut\PycharmProjects\NumPython\DataScience\Projects\CV\IMP Files\FaceLandmarks\shape_predictor_68_face_landmarks.dat'

cap = cv2.VideoCapture(0)  # Default webcam

detector = dlib.get_frontal_face_detector()
predictor = dlib.shape_predictor(faceLandmarks)

# Vision status
eyeStatus = ''
mouthStatus = ''
sleep = 0
drowsy = 0
active = 0

color = (0, 0, 0)


# Calculating Euclidean Distance
def computeDistance(pt1, pt2):
    dist = np.linalg.norm(pt1 - pt2)
    return dist


# Calculating Eye Points
def blinked(p1, p2, p3, p4, p5, p6):
    upDown = computeDistance(p2, p6) + computeDistance(p3, p5)
    leftRight = computeDistance(p1, p4)
    eye_ratio = upDown / (2.0 * leftRight)
    # cv2.putText(frame, str(ratio), (10, 20), cv2.FONT_ITALIC, 1, (0, 0, 255), 1)

    if eye_ratio > 0.25:
        return 2                        # Full open
    elif 0.21 < eye_ratio <= 0.25:
        return 1                        # Half open
    else:
        return 0                        # Closed


# Calculating Mouth Points
def yawned(pt1, pt2, pt3, pt4):
    upDown = computeDistance(pt2, pt4)
    leftRight = computeDistance(pt1, pt3)
    mouth_ratio = upDown / leftRight

    if 0.1 <= mouth_ratio <= 0.8:
        return 1                        # Yawning
    else:
        return 0                        # Not yawning


while True:
    ret, frame = cap.read()
    frame = cv2.flip(frame, 1)

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    faces = detector(gray)

    for face in faces:
        x1 = face.left()
        y1 = face.top()
        x2 = face.right()
        y2 = face.bottom()

        # face_frame: object = frame.copy()
        face_frame = frame.copy()
        cv2.rectangle(face_frame, (x1, y1), (x2, y2), (0, 255, 0), 2)

        landmark = predictor(gray, face)
        landmarks = face_utils.shape_to_np(landmark)

        # Eye Landmark points
        # The numbers are actually (LandmarkNumber - 1) because Python indexing starts from 0
        left_blink = blinked(landmarks[36], landmarks[37], landmarks[38], landmarks[39], landmarks[40], landmarks[41])
        right_blink = blinked(landmarks[42], landmarks[43], landmarks[44], landmarks[45], landmarks[46], landmarks[47])

        # Mouth Landmark points
        # The numbers are actually (LandmarkNumber - 1) because Python indexing starts from 0
        lips = yawned(landmarks[60], landmarks[62], landmarks[64], landmarks[66])

        # Giving status based on eye blinks and yawns
        if left_blink == 0 or right_blink == 0:
            sleep += 1
            drowsy = 0
            active = 0
            if sleep > 15:
                eyeStatus = 'SLEEPY'
                mouthStatus = None
                color = (0, 0, 255)

        elif (left_blink == 1 or right_blink == 1) and lips == 1:
            sleep = 0
            drowsy += 1
            active = 0
            if drowsy > 10:
                eyeStatus = 'DROWSY!'
                mouthStatus = 'YAWNING'
                color = (0, 200, 255)

        elif (left_blink == 2 or right_blink == 2) and lips == 0:
            sleep = 0
            drowsy = 0
            active += 1
            if active > 15:
                eyeStatus = 'ACTIVE'
                mouthStatus = None
                color = (0, 255, 0)

        if mouthStatus is not None:
            cv2.rectangle(frame, (15, 5), (160, 65), (0, 0, 0), -1)
            cv2.putText(frame, eyeStatus, (20, 30), cv2.FONT_ITALIC, 1, color, 2)
            cv2.putText(frame, mouthStatus, (20, 60), cv2.FONT_ITALIC, 1, color, 2)
        else:
            cv2.rectangle(frame, (15, 5), (140, 35), (0, 0, 0), -1)
            cv2.putText(frame, eyeStatus, (20, 30), cv2.FONT_ITALIC, 1, color, 2)
            cv2.putText(frame, mouthStatus, (20, 60), cv2.FONT_ITALIC, 1, color, 2)
            # draw single

        # Display all Facial Landmarks
        for n in range(68):
            x, y = landmarks[n]
            cv2.circle(face_frame, (x, y), 1, (255, 255, 255), -1)

    cv2.imshow('main', frame)
    cv2.imshow('landmarks', face_frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        cap.release()
        break

cv2.destroyAllWindows()
