from math import atan, degrees


# initialising points variables
points = {
    'p0': (2, 3), 'p1': (4, 7), 'p2': (-7, 5), 'p3': (-5, -6), 'p4': (5, -10)
}


class Process:
    '''Runs computation on points declared'''

    def __init__(self, points):
        '''Initialising variables to p0, p1, p2, p3 and p4 respectively'''
        self.p0, self.p1, self.p2, self.p3, self.p4 = points.values()

    def data(self):
        '''Outputs the data used'''
        print('Points for processing')
        for p in points:
            print(p + ':', points[p])
        print('\n\n\n')
        # print(self.p0)

    def distance(self, a1, a2):
        '''Defining general formula for distance'''
        self.dist = ((a1[0] - a2[0])**2 + (a1[1] - a2[1])**2)**(1/2)
        return self.dist

    def bearing(self, a1, a2):
        '''Defines general formula for calculating bearing in degrees'''
        y = a2[1] - a1[1]
        x = a2[0] - a1[0]
        self.bear = degrees(atan(y/x))
        return self.bear

    def consecutive_distance(self):
        '''Calculates the distance between consecutive points'''
        dist1 = self.distance(self.p0, self.p1)
        dist2 = self.distance(self.p1, self.p2)
        dist3 = self.distance(self.p2, self.p3)
        dist4 = self.distance(self.p3, self.p4)
        print(f'The distance between p0 and p1 is {round(dist1, 4)}')
        print(f'The distance between p1 and p2 is {round(dist2, 4)}')
        print(f'The distance between p2 and p3 is {round(dist3, 4)}')
        print(f'The distance between p3 and p4 is {round(dist4, 4)}')
        print('\n\n\n')

    def consecutive_bearing(self):
        '''Calculates the bearing of consecutive points'''
        bear1 = self.bearing(self.p0, self.p1)
        bear2 = self.bearing(self.p1, self.p2)
        bear3 = self.bearing(self.p2, self.p3)
        bear4 = self.bearing(self.p3, self.p4)
        print(f'The bearing between p0 and p1 is {round(bear1, 4)}')
        print(f'The bearing between p1 and p2 is {round(bear2, 4)}')
        print(f'The bearing between p2 and p3 is {round(bear3, 4)}')
        print(f'The bearing between p3 and p4 is {round(bear4, 4)}')
        print('\n\n\n')


var = Process(points)
var.data()
var.consecutive_distance()
var.consecutive_bearing()
# Accessing class objects and printing output
# Process.data()
# Process.consecutive_distance()
# Process.consecutive_bearing()
