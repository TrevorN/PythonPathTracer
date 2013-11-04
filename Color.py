class Color:
    
    def __init__(self, r, g, b):
        self.cps[0] = r
        self.cps[1] = g
        self.cps[2] = b

    def __add__(self, other):
        tmp = []
        for i in range(0, 2):
            tmp.append(self.cps[i] + other.cps[i])
        return tmp

    def __sub__(self, other):
        tmp = []
        for i in range(0, 2):
            tmp.append(self.cps[i] + other.cps[i])
        return tmp

    def __mul__(self, other):
        tmp = []
        for i in range(0, 2):
            tmp.append(self.cps[i] * other)
        return tmp
