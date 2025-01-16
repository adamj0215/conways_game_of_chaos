# comments for reference in case i get rickrolled and need to recover my mentality
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
        inner.append(random.randint(0, 1))
    cells.append(inner)

REFRESH_DELAY = 3
refresh_counter = REFRESH_DELAY

clock = pygame.time.Clock()

# Create an event loop (what runs every frame)
running = True
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
            cells[x][y] = 1
        if event.type == pygame.MOUSEMOTION and event.buttons[0]:
            x = min(round(event.pos[0] / CELL_SIZE), len(cells) - 1)
            y = min(round(event.pos[1] / CELL_SIZE), len(cells[x]) - 1)
            cells[x][y] = 1
    
    # Fill the screen with gray
    window.fill((128, 128, 128))

    # Draw each cell in a loop
    for x in range(len(cells)):
        for y in range(len(cells[x])):
            pygame.draw.rect(window, (
                random.randint(1, 255) * cells[x][y],
                random.randint(1, 255) * cells[x][y],
                random.randint(1, 255) * cells[x][y]
            ), (x * CELL_SIZE, y * CELL_SIZE, CELL_SIZE, CELL_SIZE))

    # Show what we drew
    pygame.display.flip()

    refresh_counter -= 1
    if refresh_counter == 0:
        # Change the cells
        new_cells = []
        for x in range(len(cells)):
            inner = []
            for y in range(len(cells[x])):
                # alive cells next to a cell
                neighbors = 0

                if y > 0:
                    neighbors += cells[x][y-1] # up
                    if x > 0:
                        neighbors += cells[x-1][y-1] # up left
                    if x < len(cells) - 1:
                        neighbors += cells[x+1][y-1] # up right
                if y < len(cells[x]) - 1:
                    neighbors += cells[x][y+1] # down
                    if x > 0:
                        neighbors += cells[x-1][y+1] # down left
                    if x < len(cells) - 1:
                        neighbors += cells[x+1][y+1] # down right
                if x > 0:
                    neighbors += cells[x-1][y] # left
                if x < len(cells) - 1:
                    neighbors += cells[x+1][y] # right

                # if 1 neighbor, it dies
                if neighbors < 2:
                    inner.append(0)
                
                if neighbors == 2:
                    inner.append(cells[x][y])
                
                # if 3 neighbors, it is alive
                if neighbors == 3:
                    inner.append(1)

                # if more than 3, it dies
                if neighbors > 3:
                    inner.append(0)
            new_cells.append(inner)
        cells = new_cells
        refresh_counter = REFRESH_DELAY

    clock.tick(60)

pygame.quit()
