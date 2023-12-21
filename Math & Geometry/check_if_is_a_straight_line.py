class Solution:
    def checkStraightLine(self, coordinates):
        x1,y1 = coordinates.pop()
        x2,y2 = coordinates.pop()
        if not x1 - x2:
            x0 = x1
            for x,y in coordinates:
                if not x0 == x:
                    return False
            return True


        a = float((y1-y2)/(x1-x2))
        b = float((y2*x1-y1*x2)/(x1-x2))

        for x,y in coordinates:
            if not a*x + b == y:
                return False
        return True