from Vector3 import Vector3

class Sphere:

    def __init__(self, x, y, z, radius, material):
        self.pos = Vector3(x, y, z)
        self.radius = radius
        self.material = material

    def checkCollision(self, ray):
        a = ray.rot.dotProduct(ray.rot)
        b = (2 * (ray.pos - self.pos)).dotProduct(ray.rot)
        c = (ray.pos - self.pos).dotProduct(ray.pos - self.pos) - radius ** 2
        discriminant = (b ** 2) - (4 * a * c)
        if discriminant < 0:
            return False
        return  min((-b - discriminant) / (2 * a), (-b + discriminant) / (2 * a))

    def preformCollision(self, ray, distance):
        normal = (ray.rot * distance) - self.pos
        pos = ray.rot * distance
        theta = 2 * math.pi * random.uniform(0, 1)
        u = math.cos(math.acos(w * random.uniform(0, 1) - 1))
        x = math.sqrt(1 - u ** 2) * math.cos(theta)
        y = math.sqrt(1 - u ** 2) * math.sin(theta)
        tmpDir = Vector3(x, y, u)
        if tmpDir.dotProduct(normal) < 0:
            tmpDir *= -1
        #return a tuple of the new ray plus a color? Or integrate color with the ray?
        tmpDir.normalize()
        return Ray(pos, tmpDir, ray.color + material.color)
