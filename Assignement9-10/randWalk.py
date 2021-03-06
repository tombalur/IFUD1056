import math
import random
import pylab


class Location(object):
    '''Location of person in field'''
    def __init__(self, x, y):
        self.x = float(x)
        self.y = float(y)

    def move(self, xc, yc):
        '''Move person to new location
        :param float xc: Distance X
        :param float yc: Distance Y
        :return Location
        '''
        return Location(self.x + float(xc), self.y + float(yc))

    def getCoords(self):
        '''Get postion of person
        :return tuple
        '''
        return self.x, self.y

    def getDist(self, other):
        '''Get distance from start
        :param Location other:
        :return float
        '''
        ox, oy = other.getCoords()
        xDist = self.x - ox
        yDist = self.y - oy
        return math.sqrt(xDist**2 + yDist**2)


class CompassPt(object):
    '''Find which direction the person moves'''
    possibles = ('N', 'S', 'E', 'W')

    def __init__(self, pt):
        if pt in self.possibles:
            self.pt = pt
        else:
            raise ValueError('in CompassPt.__init__')

    def move(self, dist):
        '''Find movement in the X,Y axis
        :param dist: Distance of movement
        :return tuple: Direction in the X,Y axis
        '''
        if self.pt == 'N':
            return (0, dist)
        elif self.pt == 'S':
            return (0, -dist)
        elif self.pt == 'E':
            return (dist, 0)
        elif self.pt == 'W':
            return (-dist, 0)
        else:
            raise ValueError('in CompassPt.move')


class Field(object):
    def __init__(self, drunk, loc):
        self.drunk = drunk
        self.loc = loc

    def move(self, cp, dist):
        oldLoc = self.loc
        xc, yc = cp.move(dist)
        self.loc = oldLoc.move(xc, yc)

    def getLoc(self):
        return self.loc

    def getDrunk(self):
        return self.drunk


class newField(object):
    def __init__(self, fieldsizex, fieldsizey, steplength):
        self.fieldsizex = fieldsizex / steplength
        self.fielfsizey = fieldsizey / steplength


class Drunk(object):
    def __init__(self, name):
        self.name = name

    def move(self, field, time=1):
        if field.getDrunk() != self:
            raise ValueError('Drunk.move called with drunk not in field')
        for i in range(time):
            pt = CompassPt(random.choice(CompassPt.possibles))
            field.move(pt, 1)

    def performTrial(time, f):
        start = f.getLoc()
        distances = [0.0]
        for t in range(1, time + 1):
            f.getDrunk().move(f)
            newLoc = f.getLoc()
            distance = newLoc.getDist(start)
            distances.append(distance)
        return distances


drunk = Drunk('Homer Simpson')
drunk2 = Drunk('Kjell')
for i in range(3):
    f = Field(drunk, Location(0, 0))
    distances = Drunk.performTrial(500, f)
    distances2 = Drunk.performTrial(500,f)
    pylab.plot(distances)
    pylab.plot(distances2)
pylab.title('Homer\'s Random Walk')
pylab.xlabel('Time')
pylab.ylabel('Distance from Origin')


def performSim(time, numTrials):
    distLists = []
    for trial in range(numTrials):
        d = Drunk('Drunk' + str(trial))
        f = Field(d, Location(0, 0))
        distances = Drunk.performTrial(time, f)
        distLists.append(distances)
    return distLists


def ansQuest(maxTime, numTrials):
    means = []
    distLists = performSim(maxTime, numTrials)
    for t in range(maxTime + 1):
        tot = 0.0
        for distL in distLists:
            tot += distL[t]
        means.append(tot / len(distL))
    pylab.figure()
    pylab.plot(means)
    pylab.ylabel('distance')
    pylab.xlabel('time')
    pylab.title('Average Distance vs. Time (' + str(len(distLists)) + ' trials)')


#ansQuest(500, 300)
pylab.show()
