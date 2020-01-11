'''
1232. Check If It Is a Straight Line
'''


class Solution:
    def checkStraightLine(self, coordinates):
        if len(coordinates) <= 2:
            return True

        if coordinates[0][0] - coordinates[1][0] == 0:
            for i in range(2, len(coordinates)):
                if coordinates[i][0] != coordinates[0][0]:
                    return False
            return True

        m = (coordinates[0][1] - coordinates[1][1]) / (coordinates[0][0] - coordinates[1][0])
        y0 = coordinates[0][1]
        x0 = coordinates[0][0]

        for i in range(2, len(coordinates)):
            x = coordinates[i][0]
            y = coordinates[i][1]

            if y - y0 != m * (x - x0):
                return False

        return True


