class Vector3:

    def __init__(self, x, y, z):
        self.cps = [x, y, z]

    def dotProduct(self, other):
        product = 0
        for i in range(0, 2):
            product += self.cps[i] * other.cps[i]
        return product

    def crossProduct(self, other):
        x = self.cps[1] * other.cps[2] - self.cps[2] * other.cps[1]
        y = self.cps[2] * other.cps[0] - self.cps[0] * other.cps[2]
        z = self.cps[0] * other.cps[1] - self.cps[1] * other.cps[0]
        return Vector3(x, y, z)

    def angleBetween(self, other):
        return math.acos(self.dotProduct(other) / (self.magnitude() * other.magnitude()))

    def magnitude(self):
        return math.sqrt(self.cps[0] ** 2 + self.cps[1] ** 2 + self.cps[2] ** 2)

    def normalize(self):
        mag = self.magnitude()
        for i in range(0, 2):
            self.cps[i] /= mag

    def normalized(self):
        mag = self.magnitude()
        return Vector3(self.cps[0] / mag, self.cps[1] / mag, self.cps[2] / mag)

    def distance(self, other):
        return math.sqrt((self.cps[0] - other.cps[0]) ** 2 + (self.cps[1] - other.cps[1]) ** 2 + (self.cps[2] - self.cps[2]) ** 2)

    def __sub__(self, other):
        nu = []
        for i in range(0, 2):
            nu.append(self.cps[i] - other.cps[i])
        return Vector3(nu[0], nu[1], nu[2])

    def __mul__(self, other):
        nu = []
        for i in range(0, 2):
            nuvales.append(self.cps[i] * other)
        return Vector3(nu[0], nu[1], nu[2])

