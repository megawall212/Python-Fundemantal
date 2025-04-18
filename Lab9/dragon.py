from cow import Cow

class Dragon(Cow):
    def __init__(self, name, image):
        # Initialize the Cow part of the Dragon
        super().__init__(name)
        self.set_image(image)

    def can_breath_fire(self):
        return True
