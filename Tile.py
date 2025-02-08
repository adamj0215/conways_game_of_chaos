import random

def make_random_tile():
    tile = Tile()
    tile.change_color()
    if random.randint(1,2) == 1:
        tile.turn_on()
    
    return tile

def make_random_tile_thats_on():
    tile = make_random_tile()
    tile.turn_on()
    return tile

class Tile:
    def __init__(self):
        self.state = 'off'
        self.color = (0, 0, 0)
    
    def turn_on(self):
        self.state = 'on'
    
    def turn_off(self):
        self.state = 'off'

    def turn_glitched(self):
        self.state = 'glitched'
    
    def change_color(self):
        self.color = (
            random.randint(127, 255),
            random.randint(127, 255),
            random.randint(127, 255)
        )
