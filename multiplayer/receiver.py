class Receiver:
    """
    Обработка принимаемых сообщений
    """
    def __init__(self, remote):
        self.remote = remote
        self.player = None

    def wall(self, data):
        for wall in data:
            self.player.walls.coordinates.append(wall)

    def move(self, data):
        pass

    def score(self, data):
        pass

    def acc(self, data):
        pass

    def acc_stop(self, data):
        pass

    def wall_acc(self, data):
        pass

    def wall_acc_stop(self, data):
        pass

    def end(self, data):
        pass