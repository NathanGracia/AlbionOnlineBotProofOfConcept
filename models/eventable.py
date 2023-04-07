class Eventable:
    def __init__(self, name, path):
        self.name = name
        self.path = path

        self.old_frame = 0
        self.image = None