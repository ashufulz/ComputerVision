from SlotMaker import Slots
import cv2

video = cv2.VideoCapture('path\to\ParkingLot.mp4')

Slots().mainCode(video)
