class Point:

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def clone(self):
        return Point(self.x, self.y)

pt = Point(1, 2)
print(id(pt))

pt_clone = pt.clone()
print(id(pt_clone))