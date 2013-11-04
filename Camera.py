class Camera:

    def __init__(self, pos, rot, scene, resx, resy, focalLength, width):
        self.pos = pos
        self.rot = rot
        self.scene = scene
        self.resx = resx
        self.resy = resy
        self.focalLength = focalLength
        self.width = width
        self.image = {}
        for x in range(0, resx):
            for y in range(0, resy):
                image[(x, y)] = Color(0, 0, 0)

    def getPixelRay(self, x, y):
        pixDistance = self.width/self.resx
        x = pixDistance * x - ((pixDistance * self.width) / 2)
        z = pixDistance * y - ((pixDistance * self.width) / 2)
        y = 5
        return Ray(Vector3(0, 0, 0), Vector3(x, y, z), Color(100, 100, 100))

    def takeSample(self):
        for x in range(0, self.resx):
            for y in range(0, self.resy):
                self.image[(x, y)] += self.getPixelRay(x, y).cast(scene, 5).color

