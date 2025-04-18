from dragon import Dragon


class IceDragon(Dragon):
    #Constructor; creates a new IceDragon object with the given name and image.
    def __init__(self, name, image):
        super().__init__(name, image)
        self.name = name
        self.image = image

    def can_breath_fire(self):
        return False