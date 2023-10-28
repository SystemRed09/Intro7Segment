import turtle


class Segment:
    def __init__(self):
        self.segmentCords = 0, 0
        self.segmentTurtle: turtle = turtle.Turtle()
        self.segmentTurtle.penup()
        self.segmentTurtle.speed(0)
        self.lit = False

    def setShape(self, shape):
        self.segmentTurtle.shape(shape)

    def setSegmentCords(self, x, y):
        self.segmentTurtle.setposition(x, y)

    def flip(self):
        if self.lit:
            self.segmentTurtle.color('black')
            self.lit = False
        else:
            self.segmentTurtle.color('red')
            self.lit = True


class SevenSegmentDisplay:
    def __init__(self):
        self.segments: list[Segment] = [Segment() for i in range(7)]
        for i in (0, 3, 6):
            self.segments[i].setShape('horizontalRectangle')
        for i in (1, 2, 4, 5):
            self.segments[i].setShape('verticalRectangle')

        segmentCordsIn = [[0, 60], [50, 50], [50, -10], [0, -60], [-10, -10], [-10, 50], [0, 0]]
        for i, _cords in enumerate(segmentCordsIn):
            self.segments[i].setSegmentCords(_cords[0], _cords[1])

    def setDisplayCords(self, x, y):
        segmentCordsIn = [[0, 60], [50, 50], [50, -10], [0, -60], [-10, -10], [-10, 50], [0, 0]]
        for i in range(segmentCordsIn.__len__()):
            segmentCordsIn[i][0] += x
            segmentCordsIn[i][1] += y

        for i, _cords in enumerate(segmentCordsIn):
            self.segments[i].setSegmentCords(_cords[0], _cords[1])


# ----
def initialize():
    turtle.register_shape('verticalRectangle', ((0, 0), (0, 10), (50, 10), (50, 0)))
    turtle.register_shape('horizontalRectangle', ((0, 0), (10, 0), (10, 50), (0, 50)))