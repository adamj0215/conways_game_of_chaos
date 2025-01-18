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
        if random.randint(0, 1) == 0:
            inner.append([0,0,0])
        else:
            inner.append([
                random.randint(128,255),
                random.randint(128,255),
                random.randint(128,255)
            ])
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
            cells[x][y] = [
                random.randint(128,255),
                random.randint(128,255),
                random.randint(128,255)
            ]
        if event.type == pygame.MOUSEMOTION and event.buttons[0]:
            x = min(round(event.pos[0] / CELL_SIZE), len(cells) - 1)
            y = min(round(event.pos[1] / CELL_SIZE), len(cells[x]) - 1)
            cells[x][y] = [
                random.randint(128,255),
                random.randint(128,255),
                random.randint(128,255)
            ]
        if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
            frozen = not frozen
        if event.type == pygame.KEYDOWN and event.key == pygame.K_f:
            cells = []

            for x in range(CELLS_X):
                inner = []
                for y in range(CELLS_Y):

                        inner.append([
                            random.randint(128,255),
                            random.randint(128,255),
                            random.randint(128,255)
                        ])
                cells.append(inner)
        if event.type == pygame.KEYDOWN and event.key == pygame.K_c:
            cells = []

            for x in range(CELLS_X):
                inner = []
                for y in range(CELLS_Y):

                        inner.append([
                            0, 0, 0
                        ])
                cells.append(inner)

    # Fill the screen with gray
    window.fill((128, 128, 128))

    # Draw each cell in a loop
    for x in range(len(cells)):
        for y in range(len(cells[x])):
            pygame.draw.rect(window, cells[x][y], (x * CELL_SIZE, y * CELL_SIZE, CELL_SIZE, CELL_SIZE))

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
                    neighbors += 1 if not cells[x][y-1] == [0,0,0] else 0 # up
                    if x > 0:
                        neighbors += 1 if not cells[x-1][y-1] == [0,0,0] else 0 # up left
                    if x < len(cells) - 1:
                        neighbors += 1 if not cells[x+1][y-1] == [0,0,0] else 0 # up right
                if y < len(cells[x]) - 1:
                    neighbors += 1 if not cells[x][y+1] == [0,0,0] else 0 # down
                    if x > 0:
                        neighbors += 1 if not cells[x-1][y+1] == [0,0,0] else 0 # down left
                    if x < len(cells) - 1:
                        neighbors += 1 if not cells[x+1][y+1] == [0,0,0] else 0 # down right
                if x > 0:
                    neighbors += 1 if not cells[x-1][y] == [0,0,0] else 0 # left
                if x < len(cells) - 1:
                    neighbors += 1 if not cells[x+1][y] == [0,0,0] else 0 # right

                # if 1 neighbor, it dies
                if neighbors < 2:
                    inner.append([0,0,0])
                
                if neighbors == 2:
                    inner.append(cells[x][y])
                
                # if 3 neighbors, it is alive
                if neighbors == 3:
                    inner.append([
                        random.randint(128,255),
                        random.randint(128,255),
                        random.randint(128,255)
                    ])

                # if more than 3, it dies
                if neighbors > 3:
                    inner.append([0,0,0])
            new_cells.append(inner)
        cells = new_cells
        refresh_counter = REFRESH_DELAY
    elif refresh_counter < 0:
        refresh_counter = 1

    clock.tick(60)

pygame.quit()
