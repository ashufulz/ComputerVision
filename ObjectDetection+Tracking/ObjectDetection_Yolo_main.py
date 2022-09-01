import cv2
import numpy as np

# Variable Initialization
weights = 'path/to/model_weight_file'
configuration = 'path/to/model_config_file'
classFile = 'path/to/object_class_file'


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

