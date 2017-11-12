from enum import Enum


colors = {
    'blue': (0, 153, 254), #0099cc
    'red': (255, 0, 0)
}

width = 500
height = 600

name = 'PyRace'

server_port = 1234
server_packet_size = 1024

walls_acceleration_coefficient = 2
car_acceleration_coefficient = 5

class Direction(Enum):
    STRAIGHT = 0
    RIGHT = 1
    LEFT = 2