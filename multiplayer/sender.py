from settings import Direction

class Sender:
    """
    Отправляемые сообщения
    """
    def __init__(self, remote):
        self.remote = remote

    def start(self):
        self.remote.send('start')

    def score(self, val, car_x):
        self.remote.send('score', {'val': val, 'car_x': car_x})

    def wall(self, arr):
        self.remote.send('acc', arr)

    def end(self, score):
        self.remote.send('end', {'score': score})


    def move(self, direction, car_x):
        self.remote.send('move', {'direction': direction.value, 'car_x': car_x})
    def move_stop(self, car_x):
        self.remote.send('move_stop', {'car_x': car_x})


    def acc(self, car_x):
        self.remote.send('acc', {'car_x': car_x})
    def acc_stop(self, car_x):
        self.remote.send('accelerate_car_stop', {'car_x': car_x})


    def wall_acc(self, car_x):
        self.remote.send('wall_acc', {'car_x': car_x})
    def wall_acc_stop(self, car_x):
        self.remote.send('wall_acc_stop', {'car_x': car_x})
