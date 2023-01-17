import pygame
import random
import sys


class Snake(object):
    def __init__(self):
        # Set start length
        self.length = 1
        # Set start position in the middle of the map
        # Creates list for all parts of the snake, first item is the head
        # idx 0 = x coord, idx 1 = y coord
        self.positions = [((SCREEN_WIDTH / 2), (SCREEN_HEIGHT / 2))]
        # Set a random start position
        self.direction = random.choice([UP, DOWN, LEFT, RIGHT])
        # Set color of snake
        self.color = (0, 150, 255)

    def get_head_pos(self):
        # Get position of the head of the snake, item at idx 0 from list positions property 
        return self.positions[0]

    def turn(self, point):
        # point = direction 
        # depending on which direction the snake is going, limit it's turning ability
        # Should not be able to reverse into itself
        if self.length > 1 and (point[0] * -1, point[1] * -1) == self.direction:
            return
        else:
            self.direction = point
    
    def move(self):
        # Set get current position
        cur_pos = self.get_head_pos()
        # Set current direction
        x, y = self.direction
        # Using grid size and screen width calc new pos of the head
        # Add one to x, y coords... explain % part
        new_pos = (((cur_pos[0] + (x*GRID_SIZE)) % SCREEN_WIDTH), (cur_pos[1] + (y*GRID_SIZE)) % SCREEN_HEIGHT)
        # if new positions of snake head hits body reset game
        # positions[2:] = any body part from of an idx of 2 or greater
        # 0 = head so, idx of 2 or more is needed to make collision with body possible
        if len(self.positions) > 2 and new_pos in self.positions[2:]:
            self.reset()
        else:
            # Add new position of head into positions list
            self.positions.insert(0, new_pos)
            # Remove lass element, the last bit of the tail - it's moving forward
            if len(self.positions) > self.length:
                self.positions.pop()

    # Reset to init vars - functionize later
    def reset(self):
        self.length = 1
        self.positions = [((SCREEN_WIDTH / 2), (SCREEN_HEIGHT / 2))]
        self.direction = random.choice([UP, DOWN, LEFT, RIGHT])

    def draw(self, surface):
        # Draw a block for each x, y position of the snake
        for block in self.positions:
            sq = pygame.Rect((block[0], block[1]), (GRID_SIZE, GRID_SIZE))
            pygame.draw.rect(surface, self.color, sq) # Body parts
            pygame.draw.rect(surface, (89, 89, 83), sq, 1) # Outline?

    def handle_keys(self):
        # If player hits quit - x at top right corner
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit() 
                sys.exit() # Running program
            # Check for key down event, move snake accordingly
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    self.turn(UP)
                elif event.key == pygame.K_DOWN:
                    self.turn(DOWN)
                elif event.key == pygame.K_LEFT:
                    self.turn(LEFT)
                elif event.key == pygame.K_RIGHT:
                    self.turn(RIGHT)

class Food(object):
    def __init__(self):
        self.posiion = (0, 0) # x, y position
        self.color = (255, 0, 0)
        self.randomize_pos()

    def randomize_pos(self):
        self.position = (random.randint(0, GRID_WIDTH-1) * GRID_SIZE, random.randint(0, GRID_HEIGHT-1) * GRID_SIZE)

    def draw(self, surface):
        block = pygame.Rect((self.position[0], self.position[1]), (GRID_SIZE, GRID_SIZE))
        pygame.draw.rect(surface, self.color, block)
        pygame.draw.rect(surface, (89, 89, 83), block, 1)

def draw_grid(surface):
    # Loop through grid, rows - x, collumns - y
    for y in range(0, int(GRID_HEIGHT)):
        for x in range(0, int(GRID_WIDTH)):
            # Draw black or white squares depending on the position of square on the grid
            if (x + y) % 2 == 0:
                white_sq = pygame.Rect(x*GRID_SIZE, y*GRID_SIZE, GRID_SIZE, GRID_SIZE)
                pygame.draw.rect(surface, (255, 255, 255), white_sq)
            else:
                black_sq = pygame.Rect(x*GRID_SIZE, y*GRID_SIZE, GRID_SIZE, GRID_SIZE)
                pygame.draw.rect(surface, (0, 0, 0), black_sq)


# Global Variable(s)
# Screen specs
SCREEN_WIDTH = 500
SCREEN_HEIGHT = 500

# Grid specs
GRID_SIZE = 20
GRID_WIDTH = SCREEN_HEIGHT / GRID_SIZE
GRID_HEIGHT = SCREEN_WIDTH / GRID_SIZE

# Movement controls
UP = (0, -1)
DOWN = (0, 1)
LEFT = (-1, 0)
RIGHT = (1, 0)



def main():

    # Initialize any imported modules
    pygame.init()

    # Keep track of actions at current time
    clock = pygame.time.Clock()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT), 0, 32)

    # Draw surface (screen/visuals)
    surface = pygame.Surface(screen.get_size())
    surface = surface.convert()
    draw_grid(surface)

    snake = Snake()
    food = Food()

    # Initialize score
    score = 0
    while (True):
        clock.tick(10) # tick at 10 fps
        snake.handle_keys() # handle key inputs
        draw_grid(surface)
        snake.move()
        # Update game if snake ate food, head pos = food pos
        if snake.get_head_pos() == food.position:
            snake.length += 1
            score += 1
            food.randomize_pos()

        snake.draw(surface)
        food.draw(surface)
        # blit - draw surface onto screen (surface, (x, y)) - top left corner
        # surface - the pannel inside the screen in which you draw objects
        # screen - the 'canvas' that you update and draw the surface onto
        screen.blit(surface, (0, 0))
        
        # Display score - write in magenta
        # text = myfont.render("Score {0}".format(score), 1, (0, 255, 0))
        # text = pygame.font.SysFont("Arial", 36)
        # screen.blit(text, (5, 10))
        pygame.display.update()

main()