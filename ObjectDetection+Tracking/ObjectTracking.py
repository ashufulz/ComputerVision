from ObjectDetection_Yolo_main import ObjectDetection
import cv2
import math

# --- Variable Initialization -------------------
video = r'C:\Users\ashut\PycharmProjects\NumPython\DataScience\Projects\CV\IMP Files\_ASSETS_\Videos\TrafficFlow_5.mp4'

center_points_prev_frame = []
tracking_objects = {}
track_id = 1

WIN_WIDTH = 1280
WIN_HEIGHT = 720

FOUR_CC = cv2.VideoWriter_fourcc(*'MP4V')
OUTPUT_PATH = r'C:\Users\ashut\PycharmProjects\NumPython\DataScience\Projects\CV\IMP Files\_ASSETS_\Videos\Saved\Tracking_2.mp4'

OUTPUT = cv2.VideoWriter(OUTPUT_PATH, FOUR_CC, 25.0, (WIN_WIDTH, WIN_HEIGHT))

MIN_DISTANCE = 25
# ------------------------------------------------

od = ObjectDetection()

# Loading Video
capture = cv2.VideoCapture(video)
count = 0

while True:
    ret, frame = capture.read()
    count += 1

    if not ret:
        print('Error reading in frames!')
        break

    # if ret:
    frame = cv2.resize(frame, (WIN_WIDTH, WIN_HEIGHT))
    center_points_curr_frame = []

    (boxes, confidences, class_ids) = od.detect(frame=frame)

    indexes = cv2.dnn.NMSBoxes(boxes, confidences, 0.5, 0.4)

    if len(indexes) > 0:
        for i in indexes.flatten():
            x, y, w, h = boxes[i]
            # print('Frame', count, ' ', x, y, w, h)
            cx = int((x + x + w) / 2)
            cy = int((y + y + h) / 2)
            center_points_curr_frame.append((cx, cy))

            cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)

    if count <= 2:
        for pt1 in center_points_curr_frame:
            for pt2 in center_points_prev_frame:
                distance = math.hypot(pt2[0] - pt1[0], pt2[1] - pt1[1])
                # print('d1', distance)

                if distance <= MIN_DISTANCE:
                    tracking_objects[track_id] = pt1
                    track_id += 1

    else:
        tracking_objects_copy = tracking_objects.copy()
        center_points_curr_frame_copy = center_points_curr_frame.copy()

        for object_id, pt2 in tracking_objects_copy.items():
            object_exists = False
            for pt1 in center_points_curr_frame_copy:
                distance = math.hypot(pt2[0] - pt1[0], pt2[1] - pt1[1])
                # print('d2', distance)

                # Updating object's position
                if distance <= MIN_DISTANCE:
                    tracking_objects[object_id] = pt1
                    object_exists = True
                    if pt1 in center_points_curr_frame:
                        center_points_curr_frame.remove(pt1)
                    continue

            # Removing objects not in frame
            if not object_exists:
                tracking_objects.pop(object_id)

            # if not object_exists:
            #     # print(pt2[0], pt2[1], MIN_DISTANCE, object_id)
            #     if pt2[0] <= MIN_DISTANCE or pt2[1] <= MIN_DISTANCE:
            #         tracking_objects.pop(object_id)     # remove objects from list
            #     else:
            #         # assign the same object id
            #         print(object_id)

        # Adding IDs to new objects
        for pt in center_points_curr_frame:
            tracking_objects[track_id] = pt
            track_id += 1

    for object_id, pt in tracking_objects.items():
        # cv2.circle(frame, pt, 3, (0, 0, 255), -1)
        cv2.putText(frame, str(object_id), (pt[0] - 10, pt[1]), 0, 1, (0, 0, 255), 2)

    # print('track', tracking_objects)
    # print('cur', center_points_curr_frame)
    # print('prv', center_points_prev_frame)

    cv2.imshow('main', frame)

    # Save the frames
    # OUTPUT.write(frame)

    # Making a copy of the all the center points in current frame
    center_points_prev_frame = center_points_curr_frame.copy()

    if cv2.waitKey(0) & 0xFF == ord('q'):
        capture.release()
        break

cv2.destroyAllWindows()

