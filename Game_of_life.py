class Game:
    def hasLoop(self):
        pass

    def __init__(self, initState):
        self.state = initState
        self.prevStates = []

    def step(self):

        self.state = newState
        self.prevStates.append(newState)
        return self.state.__str__()

class State:
    def __init__(self, fileName):
        #fileName -> plane
        self.plane = plane
        self.height = height
        self.width = width

    def __str__(self):
        return ''

s = State("cellAutomat.txt")
g = Game(s)
print(g)
for i in range(15):
    g.step()
    print(g)
    if g.hasLoop():
        break