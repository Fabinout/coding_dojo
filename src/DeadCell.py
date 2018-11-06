from src.LivingCell import LivingCell


class DeadCell(object):

    def __init__(self):
        self.neighbors = None

    def withNeighbors(self, *args):
        self.neighbors = args
        return self

    def isAlive(self):
        return False

    def isDead(self):
        return True

    def nextStep(self):
        if self._countAliveNeighbors() == 3:
            return self
        return self

    def _countAliveNeighbors(self):
        return len([n for n in self.neighbors if n.isAlive()])