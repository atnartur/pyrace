def is_collision(car, walls):
    screen_w = walls.size[0]
    car_x, car_y = car.x, car.y
    car_w, car_h = car.img.get_width(), car.img.get_height()
    collision = False
    i = 0
    while i < len(walls.coordinates) and not collision:
        y, width, direction = walls.coordinates[i]
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

