
"""
This program divide the whole screen (frame) into 9 equal parts. Each part is known as a Quadrant.
1. This can be used to retrieve the 4 points of each quadrant
2. It can also be used to crop some part of the whole frame for better visualization
"""


class quadPoints():
    def __init__(self, height, width):
        self.height = height
        self.width = width

    def Q11(self):
        p1 = (0, 0)
        p2 = (int(self.width / 3), 0)
        p3 = (int(self.width / 3), int(self.height / 3))
        p4 = (0, int(self.height / 3))
        return p1, p2, p3, p4

    def Q12(self):
        p1 = (int(self.width / 3), 0)
        p2 = (int(2 * self.width / 3), 0)
        p3 = (int(2 * self.width / 3), int(self.height / 3))
        p4 = (int(self.width / 3), int(self.height / 3))
        return p1, p2, p3, p4

    def Q13(self):
        p1 = (int(2 * self.width / 3), 0)
        p2 = (int(self.width), 0)
        p3 = (int(self.width), int(self.height / 3))
        p4 = (int(2 * self.width / 3), int(self.height / 3))
        return p1, p2, p3, p4

    def Q21(self):
        p1 = (0, int(self.height / 3))
        p2 = (int(self.width / 3), int(self.height / 3))
        p3 = (int(self.width / 3), int(2 * self.height / 3))
        p4 = (0, int(2 * self.height / 3))
        return p1, p2, p3, p4

    def Q22(self):
        p1 = (int(self.width / 3), int(self.height / 3))
        p2 = (int(2 * self.width / 3), int(self.height / 3))
        p3 = (int(2 * self.width / 3), int(2 * self.height / 3))
        p4 = (int(self.width / 3), int(2 * self.height / 3))
        return p1, p2, p3, p4

    def Q23(self):
        p1 = (int(2 * self.width / 3), int(self.height / 3))
        p2 = (int(self.width), int(self.height / 3))
        p3 = (int(self.width), int(2 * self.height / 3))
        p4 = (int(2 * self.width / 3), int(2 * self.height / 3))
        return p1, p2, p3, p4

    def Q31(self):
        p1 = (0, int(2 * self.height / 3))
        p2 = (int(self.width / 3), int(2 * self.height / 3))
        p3 = (int(self.width / 3), int(self.height))
        p4 = (0, int(self.height))
        return p1, p2, p3, p4

    def Q32(self):
        p1 = (int(self.width / 3), int(2 * self.height / 3))
        p2 = (int(2 * self.width / 3), int(2 * self.height / 3))
        p3 = (int(2 * self.width / 3), int(self.height))
        p4 = (int(self.width / 3), int(self.height))
        return p1, p2, p3, p4

    def Q33(self):
        p1 = (int(2 * self.width / 3), int(2 * self.height / 3))
        p2 = (int(self.width), int(2 * self.height / 3))
        p3 = (int(self.width), int(self.height))
        p4 = (int(2 * self.width / 3), int(self.height))
        return p1, p2, p3, p4


class quadFrames:
    def __init__(self, height, width):
        self.height = height
        self.width = width

    def Q11(self):
        p1 = (0, 0)
        p2 = (int(self.width / 3), int(self.height / 3))
        return p1, p2

    def Q12(self):
        p1 = (int(self.width / 3), 0)
        p2 = (int(2 * self.width / 3), int(self.height / 3))
        return p1, p2

    def Q13(self):
        p1 = (int(2 * self.width / 3), 0)
        p2 = (int(self.width), int(self.height / 3))
        return p1, p2

    def Q21(self):
        p1 = (0, int(self.height / 3))
        p2 = (int(self.width / 3), int(2 * self.height / 3))
        return p1, p2

    def Q22(self):
        p1 = (int(self.width / 3), int(self.height / 3))
        p2 = (int(2 * self.width / 3), int(2 * self.height / 3))
        return p1, p2

    def Q23(self):
        p1 = (int(2 * self.width / 3), int(self.height / 3))
        p2 = (int(self.width), int(2 * self.height / 3))
        return p1, p2

    def Q31(self):
        p1 = (0, int(2 * self.height / 3))
        p2 = (int(self.width / 3), int(self.height))
        return p1, p2

    def Q32(self):
        p1 = (int(self.width / 3), int(2 * self.height / 3))
        p2 = (int(2 * self.width / 3), int(self.height))
        return p1, p2

    def Q33(self):
        p1 = (int(2 * self.width / 3), int(2 * self.height / 3))
        p2 = (int(self.width), int(self.height))
        return p1, p2
