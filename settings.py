from enum import Enum


colors = {
    'blue': (0, 153, 254), #0099cc
    'red': (255, 0, 0)
}

width = 800
height = 600

name = 'PyRace'

server_port = 1234
server_packet_size = 1024

class Direction(Enum):
    STRAIGHT = 0
    RIGHT = 1
    LEFT = 2