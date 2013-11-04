from Ray import Ray

class Ray:

    def __init__(self, pos, rot, color):
        self.pos = pos
        self.rot = rot
        self.color = color

    def cast(self, scene, longevity):
        toSample = 0
        for form in scene:
            if toSample == 0:
                toSample = (form.checkCollision(self), form)
            else:
                dist = form.checkCollision(self)
                if dist < toSample[0]:
                    toSample = (dist, form)
        if(longevity < 0):
            return toSample[1].preformCollision(self, toSample[2])
        else:
            return toSample[1].preformCollision(self, toSample[2]).cast(scene, longevity - 1)
