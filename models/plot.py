from eventable import Eventable


class Plot(Eventable):
    def __init__(self, name, path, is_collectable = 0):
        super().__init__(name, path)
        self.is_collectable = is_collectable
