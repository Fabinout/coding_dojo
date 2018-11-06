from src.DeadCell import DeadCell


class LivingCell(object):

    def __init__(self):
        self.neighbors = None

    def withNeighbors(self, *args):
        self.neighbors = args
        return self

    def nextStep(self):
        if self._countAliveNeighbors() in [2, 3]:
            return self
        return DeadCell()

    def isDead(self):
        return False

    def isAlive(self):
        return True

    def _countAliveNeighbors(self):
        return len([n for n in self.neighbors if n.isAlive()])