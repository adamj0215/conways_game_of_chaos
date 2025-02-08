# comments for reference in case i get rickrolled and need to recover my mentality
from Tile import Tile, make_random_tile, make_random_tile_thats_on
import pygame
import random
import math

# can you feel the rhythm the algorithm
WIDTH = 1280
HEIGHT = 720

# CELL_SIZE = math.gcd(WIDTH, HEIGHT)
CELL_SIZE = 20

CELLS_X = int(WIDTH / CELL_SIZE)
CELLS_Y = int(HEIGHT / CELL_SIZE)

# Initialize (setup) Pygame
pygame.init()

# Create a window
window = pygame.display.set_mode((WIDTH, HEIGHT))

cells = []

for x in range(CELLS_X):
    inner = []
    for y in range(CELLS_Y):
        inner.append(make_random_tile())
    cells.append(inner)

REFRESH_DELAY = 5
refresh_counter = REFRESH_DELAY

clock = pygame.time.Clock()

# Create an event loop (what runs every frame)
running = True
frozen  = False
while running:
    # Process every event
    for event in pygame.event.get():
        # If we click the X on the window...
        if event.type == pygame.QUIT:
            # Close the program
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            x = min(round(event.pos[0] / CELL_SIZE), len(cells) - 1)
            y = min(round(event.pos[1] / CELL_SIZE), len(cells[x]) - 1)
            cells[x][y] = make_random_tile_thats_on()
        if event.type == pygame.MOUSEMOTION and event.buttons[0]:
            x = min(round(event.pos[0] / CELL_SIZE), len(cells) - 1)
            y = min(round(event.pos[1] / CELL_SIZE), len(cells[x]) - 1)
            cells[x][y] = make_random_tile_thats_on()
        if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
            frozen = not frozen
        if event.type == pygame.KEYDOWN and event.key == pygame.K_f:
            cells = []

            for x in range(CELLS_X):
                inner = []
                for y in range(CELLS_Y):

                        inner.append(make_random_tile_thats_on())
                cells.append(inner)
        if event.type == pygame.KEYDOWN and event.key == pygame.K_c:
            cells = []

            for x in range(CELLS_X):
                inner = []
                for y in range(CELLS_Y):

                        inner.append(Tile())
                cells.append(inner)

    # Fill the screen with gray
    window.fill((128, 128, 128))

    # Draw each cell in a loop
    for x in range(len(cells)):
        for y in range(len(cells[x])):
            pygame.draw.rect(window, cells[x][y].color, (x * CELL_SIZE, y * CELL_SIZE, CELL_SIZE, CELL_SIZE))

    # Show what we drew
    pygame.display.flip()

    refresh_counter -= 1
    if refresh_counter == 0 and not frozen:
        # Change the cells
        new_cells = []
        for x in range(len(cells)):
            inner = []
            for y in range(len(cells[x])):
                # alive cells next to a cell
                neighbors = 0

                if y > 0:
                    neighbors += 1 if not cells[x][y-1].state == 'off' else 0 # up
                    if x > 0:
                        neighbors += 1 if not cells[x-1][y-1].state == 'off' else 0 # up left
                    if x < len(cells) - 1:
                        neighbors += 1 if not cells[x+1][y-1].state == 'off' else 0 # up right
                if y < len(cells[x]) - 1:
                    neighbors += 1 if not cells[x][y+1].state == 'off' else 0 # down
                    if x > 0:
                        neighbors += 1 if not cells[x-1][y+1].state == 'off' else 0 # down left
                    if x < len(cells) - 1:
                        neighbors += 1 if not cells[x+1][y+1].state == 'off' else 0 # down right
                if x > 0:
                    neighbors += 1 if not cells[x-1][y].state == 'off' else 0 # left
                if x < len(cells) - 1:
                    neighbors += 1 if not cells[x+1][y].state == 'off' else 0 # right

                # if 1 neighbor, it dies
                if neighbors < 2:
                    inner.append(Tile())
                
                if neighbors == 2:
                    inner.append(cells[x][y])
                
                # if 3 neighbors, it is alive
                if neighbors == 3:
                    tile = make_random_tile()
                    tile.turn_on()

                    inner.append(tile)

                # if more than 3, it dies
                if neighbors > 3:
                    inner.append(Tile())
            new_cells.append(inner)
        cells = new_cells
        refresh_counter = REFRESH_DELAY
    elif refresh_counter < 0:
        refresh_counter = 1

    clock.tick(60)

pygame.quit()
