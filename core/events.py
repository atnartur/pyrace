from settings import Direction
from multiplayer.remote import Remote


class Events:
    instance = None
    acceleration_timeout = 1

    @staticmethod
    def get_instance(car, walls):
        if Events.instance is None:
            Events.instance = Events(car, walls)
        return Events.instance

    def __init__(self, car, walls):
        self.car = car
        self.walls = walls
        self.acceleration_coefficient = 1
        Remote.sender.wall(self.walls.coordinates)
        self.car.acc_stop_callback = self.accelerate_car_stop

    def is_collision(self):
        screen_w = self.walls.size[0]
        car_x, car_y = self.car.x, self.car.y
        car_w, car_h = self.car.img.get_width(), self.car.img.get_height()
        collision = False
        i = 0
        while i < len(self.walls.coordinates) and not collision:
            y, width, direction = self.walls.coordinates[i]
            in_width = False
            in_height = False
            if car_y - car_h/2 <= y <= car_y + car_h/2:
                in_height = True
            if direction and (car_x - car_w/2 <= width):
                in_width = True
            elif not direction and (car_x + car_w/2 >= screen_w - width):
                in_width = True
            collision = in_height and in_width
            i += 1
        return collision

    def score_update(self, score):
        Remote.sender.score(score, self.car.x)

    def shift_left(self):
        self.car.direction = Direction.LEFT
        Remote.sender.move(Direction.LEFT, self.car.x)

    def shift_right(self):
        self.car.direction = Direction.RIGHT
        Remote.sender.move(Direction.RIGHT, self.car.x)

    def accelerate(self, k):
        self.walls.acceleration_coefficient = k
        self.walls.is_accelerated = True
        Remote.sender.wall_acc(self.car.x)

    def accelerate_car(self, k):
        self.car.acceleration_coefficient = k
        self.car.is_accelerated = True
        Remote.sender.acc(self.car.x)

    def accelerate_car_stop(self):
        Remote.sender.acc_stop(self.car.x)

    def end(self, score):
        Remote.sender.end(score)
        Remote.stop()

    def wall_generated(self, wall):
        Remote.sender.wall([wall])