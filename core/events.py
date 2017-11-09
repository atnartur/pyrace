class Events:
    instance = None

    @staticmethod
    def get_instance(car, walls):
        if Events.instance is None:
            Events.instance = Events(car, walls)
        return Events.instance

    def __init__(self, car, walls):
        self.car = car
        self.walls = walls

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
            else:
                continue
            if direction and (car_x - car_w/2 <= width):
                in_width = True
            elif not direction and (car_x + car_w/2 >= screen_w - width):
                in_width = True
            else:
                continue
            collision = in_height and in_width
        return collision

    def shift_left(self):
        self.car.x -= 1

    def shift_right(self):
        self.car.x += 1
