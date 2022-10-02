import cv2
import numpy as np

WIDTH = 90
HEIGHT = 35

TOTAL_SLOTS = 104


class Slots:
    def __init__(self):

        self.all_cols = [
            (115, 440), (116, 475), (117, 510), (118, 545), (119, 583), (120, 622),
            (200, 150), (200, 187), (201, 225), (202, 265), (203, 300), (204, 335), (204, 370),
            (205, 405), (205, 440), (206, 475), (207, 510), (208, 545), (209, 583), (210, 622),
            (395, 150), (395, 186), (395, 223), (405, 259), (405, 298), (405, 333), (406, 368), (406, 402),
            (406, 438), (407, 472), (407, 508), (407, 543), (408, 581), (408, 620), (408, 657),
            (505, 150), (505, 186), (505, 223), (495, 259), (495, 298), (495, 333), (496, 368), (496, 402),
            (496, 438), (497, 472), (497, 508), (497, 543), (498, 581), (498, 618), (498, 657),
            (690, 112), (690, 173), (690, 235), (695, 293), (695, 329), (696, 366), (696, 400),
            (698, 470), (699, 505), (700, 540), (701, 578), (702, 615), (703, 655),
            (795, 125), (795, 186), (795, 247), (785, 293), (785, 329), (786, 366), (786, 400),
            (788, 470), (789, 505), (790, 540), (791, 578), (792, 615), (793, 655),
            (990, 180), (991, 216), (991, 249), (992, 285), (992, 320), (993, 354), (993, 387),
            (993, 422), (994, 458), (994, 493), (994, 528), (995, 565), (995, 605), (995, 648),
            (1080, 180), (1081, 216), (1081, 249), (1082, 285), (1082, 320), (1083, 354), (1083, 387),
            (1083, 422), (1084, 458), (1084, 493), (1084, 528), (1085, 565), (1085, 605), (1085, 648)
            ]

        self.aCol = [(115, 440), (116, 475), (117, 510), (118, 545), (119, 583), (120, 622)]

        self.bCol = [(200, 150), (200, 187), (201, 225), (202, 265), (203, 300), (204, 335), (204, 370), (205, 405),
                     (205, 440), (206, 475), (207, 510), (208, 545), (209, 583), (210, 622)]

        self.cCol = [(395, 150), (395, 186), (395, 223), (405, 259), (405, 298), (405, 333), (406, 368), (406, 402),
                     (406, 438), (407, 472), (407, 508), (407, 543), (408, 581), (408, 620), (408, 657)]

        self.dCol = [(505, 150), (505, 186), (505, 223), (495, 259), (495, 298), (495, 333), (496, 368), (496, 402),
                     (496, 438), (497, 472), (497, 508), (497, 543), (498, 581), (498, 618), (498, 657)]

        self.eCol = [(690, 112), (690, 173), (690, 235), (695, 293), (695, 329), (696, 366), (696, 400),
                     (698, 470), (699, 505), (700, 540), (701, 578), (702, 615), (703, 655)]

        self.fCol = [(795, 125), (795, 186), (795, 247), (785, 293), (785, 329), (786, 366), (786, 400),
                     (788, 470), (789, 505), (790, 540), (791, 578), (792, 615), (793, 655)]

        self.gCol = [(990, 180), (991, 216), (991, 249), (992, 285), (992, 320), (993, 354), (993, 387),
                     (993, 422), (994, 458), (994, 493), (994, 528), (995, 565), (995, 605), (995, 648)]

        self.hCol = [(1080, 180), (1081, 216), (1081, 249), (1082, 285), (1082, 320), (1083, 354), (1083, 387),
                     (1083, 422), (1084, 458), (1084, 493), (1084, 528), (1085, 565), (1085, 605), (1085, 648)]

        print('Created parking slots')

    def process(self, frame):
        COUNTER = 0

        org_frame = frame
        gray = cv2.cvtColor(org_frame, cv2.COLOR_BGR2GRAY)
        blur = cv2.GaussianBlur(gray, (5, 5), 1)
        thresh = cv2.adaptiveThreshold(blur, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY_INV, 25, 16)
        median = cv2.medianBlur(thresh, 5)
        dilate = cv2.dilate(median, (np.ones((1, 1), np.uint8)), iterations=1)

        # self.pixel(dilate, frame)

        for pts in self.all_cols:
            image = dilate[pts[1]:pts[1] + HEIGHT, pts[0]:pts[0] + WIDTH]
            count = cv2.countNonZero(image)

            # black mask to display non-zero pixels
            # cv2.rectangle(org_frame, (pts[0], pts[1]), (pts[0] + int(WIDTH / 3), pts[1] + int(HEIGHT / 3)),
            #               (0, 0, 0), -1)

            # Available space
            if count <= 330:
                COUNTER += 1
                cv2.rectangle(org_frame, (pts[0], pts[1]), (pts[0] + WIDTH, pts[1] + HEIGHT), (0, 255, 0), 2)       # green rect
                # cv2.putText(org_frame, str(count), (pts[0] + 2, pts[1] + 10), cv2.FONT_ITALIC, 0.35, (0, 255, 0), 1)

            # Parked space
            else:
                pass
                # cv2.rectangle(org_frame, (pts[0], pts[1]), (pts[0] + WIDTH, pts[1] + HEIGHT), (0, 0, 255), 1)       # red rect
                # cv2.putText(org_frame, str(count), (pts[0] + 2, pts[1] + 10), cv2.FONT_ITALIC, 0.35, (0, 0, 255), 1)

        # main counter mask
        cv2.rectangle(org_frame, (10, 10), (400, 70), (0, 0, 0), -1)
        cv2.putText(org_frame, f'{COUNTER}/{TOTAL_SLOTS} Slots Available', (25, 50), cv2.FONT_ITALIC, 1,
                    (255, 255, 255), 2)

    def createBoxROI(self, frame):
        for pts in self.all_cols:
            cv2.rectangle(frame, (pts[0], pts[1]), (pts[0] + WIDTH, pts[1] + HEIGHT), (255, 255, 255), 2)

    def mainCode(self, video):
        while True:
            """
            .   @param CAP_PROP_POS_FRAMES: current frame's number
            .   @param CAP_PROP_FRAME_COUNT: total number/length of frames
            """

            if video.get(cv2.CAP_PROP_POS_FRAMES) == video.get(cv2.CAP_PROP_FRAME_COUNT):
                video.set(cv2.CAP_PROP_POS_FRAMES, 0)

            ret, frame = video.read()

            frame = cv2.resize(frame, (1280, 720))

            # making ROI around box
            # self.createBoxROI(frame)

            self.process(frame)

            cv2.imshow('main', frame)

            if cv2.waitKey(5) & 0xFF == ord('q'):
                video.release()
                break

    cv2.destroyAllWindows()
