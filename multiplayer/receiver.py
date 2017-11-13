from settings import Direction, width
from settings import walls_acceleration_coefficient, car_acceleration_coefficient


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
        self.player.car.x = width + data['car_x']
        self.player.car.direction = Direction(data['direction'])

    def score(self, data):
        self.player.car.x = width + data['car_x']
        self.player.info_panel.score = data['val']

    def acc(self, data):
        self.player.car.x = width + data['car_x']
        self.player.car.is_accelerated = True
        self.player.car.acceleration_coefficient = car_acceleration_coefficient

    def acc_stop(self, data):
        self.player.car.x = width + data['car_x']
        self.player.car.is_accelerated = False

    def wall_acc(self, data):
        self.player.car.x = width + data['car_x']
        self.player.walls.is_accelerated = True
        self.player.walls.acceleration_coefficient = walls_acceleration_coefficient

    def wall_acc_stop(self, data):
        self.player.car.x = width + data['car_x']
        self.player.walls.is_accelerated = False

    def end(self, data):
        self.player.end(data['score'])
