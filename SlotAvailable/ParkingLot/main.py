from SlotMaker import Slots
import cv2

video = cv2.VideoCapture(
    r'C:\Users\ashut\PycharmProjects\NumPython\DataScience\Projects\CV\IMP Files\_ASSETS_\Videos\ParkingLot_1_LT.mp4')

Slots().mainCode(video)
