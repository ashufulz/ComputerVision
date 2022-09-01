import cv2
import numpy as np

# Variable Initialization
video = r'C:\Users\ashut\PycharmProjects\NumPython\DataScience\Projects\CV\IMP Files\_ASSETS_\CityDriving_3.mp4'
output_video_path = r'C:\Users\ashut\PycharmProjects\NumPython\DataScience\Projects\CV\IMP Files\_ASSETS_\Saved'

file_name = video.split("\\")[-1].split('.')[0]
file_ext = video.split("\\")[-1].split('.')[1]

OUTPUT_PATH = output_video_path + "\\" + file_name + '.' + file_ext

MODEL = 'v3'

weights = fr'C:\Users\ashut\PycharmProjects\NumPython\DataScience\Projects\CV\IMP Files\_ASSETS_\Models\Pre-trained\YOLO\Yolo_{MODEL}\yolo{MODEL}.weights'
configuration = fr'C:\Users\ashut\PycharmProjects\NumPython\DataScience\Projects\CV\IMP Files\_ASSETS_\Models\Pre-trained\YOLO\Yolo_{MODEL}\yolo{MODEL}.cfg'
classFile = r'C:\Users\ashut\PycharmProjects\NumPython\DataScience\Projects\CV\IMP Files\COCO_Names.txt'

FOUR_CC = cv2.VideoWriter_fourcc(*'MP4V')

WIN_WIDTH = 1280
WIN_HEIGHT = 720

OUTPUT = cv2.VideoWriter(OUTPUT_PATH, FOUR_CC, 25.0, (WIN_WIDTH, WIN_HEIGHT))


class ObjectDetection:
    def __init__(self):
        self.net = cv2.dnn.readNet(weights, configuration)
        self.layer_names = self.net.getLayerNames()
        self.output_layers = [self.layer_names[i - 1] for i in self.net.getUnconnectedOutLayers()]

        print('Loaded YOLO network successfully...')

    def load_classes(self):
        with open(classFile, 'r') as f:
            classes = [line.strip() for line in f.readlines()]

        colors = np.random.uniform(0, 255, size=(len(classes), 3))
        return classes, colors

    def detect(self, frame):
        height, width, channels = frame.shape

        # Detection objects
        blob = cv2.dnn.blobFromImage(image=frame, scalefactor=0.001, size=(416, 416),
                                     mean=(0, 0, 0), swapRB=True, crop=False)

        self.net.setInput(blob)
        outs = self.net.forward(self.output_layers)

        class_ids = []
        confidences = []
        boxes = []

        for out in outs:
            for detection in out:
                scores = detection[5:]
                class_id = np.argmax(scores)
                confidence = scores[class_id]

                if confidence > 0.1:
                    center_x = int(detection[0] * width)
                    center_y = int(detection[1] * height)
                    w = int(detection[2] * width)
                    h = int(detection[3] * height)

                    # Box coordinates
                    x = int(center_x - w / 2)
                    y = int(center_y - h / 2)

                    boxes.append([x, y, w, h])
                    confidences.append(float(confidence))
                    class_ids.append(class_id)

        return boxes, confidences, class_ids

