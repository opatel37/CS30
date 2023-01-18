import pygame
import random
import sys

# Parent class to make and control snakes
class Snake():
    def __init__(self, rgb_color):
        # Set start length
        self.length = 1
        # Set start position in the middle of the map
        # Creates list for all parts of the snake, first item is the head
        # idx 0 = x coord, idx 1 = y coord
        self.positions = [((SCREEN_WIDTH / 2), (SCREEN_HEIGHT / 2))]
        # Set a random start position
        self.direction = random.choice([UP, DOWN, LEFT, RIGHT])
        # Set color of snake
        self.color = rgb_color

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
        # Add one block, size of one grid square, to x, y coords
        new_pos = (((cur_pos[0] + (x*GRID_SIZE))), (cur_pos[1] + (y*GRID_SIZE)))

        return new_pos

    # Check for collisions between head and body segments
    def body_collision(self, new_position):
        # if new positions of snake head hits body reset game
        # positions[2:] - any body part from of an idx of 2 or greater
        # 0 - head so, idx of 2 or more is needed to make collision with body possible
        if len(self.positions) > 2 and new_position in self.positions[2:]:
            self.reset()
        else:
            # Indicate no collision detected
            return True

    # Check for collisions between head and borders
    def border_collision(self, new_position):
        if new_position[0] < 0 or new_position[1] < 0 or new_position[0] > SCREEN_WIDTH or new_position[1] > SCREEN_HEIGHT:
            self.reset()
        else:
            # Indicate no collision detected
            return True

    # If no collisions were detected, update snake positions
    def collision_mangager(self, new_position):
        if self.body_collision(new_position) and self.border_collision(new_position):
            # Add new position of head into positions list
            self.positions.insert(0, new_position)
            # Remove last element, the last bit of the tail - it's moving forward
            if len(self.positions) > self.length:
                self.positions.pop()

    # Reset to init vars
    def reset(self):
        self.length = 1
        self.positions = [((SCREEN_WIDTH / 2), (SCREEN_HEIGHT / 2))]
        self.direction = random.choice([UP, DOWN, LEFT, RIGHT])

    def draw(self, surface):
        # Draw a block for each x, y position of the snake
        for block in self.positions:
            sq = pygame.Rect((block[0], block[1]), (GRID_SIZE, GRID_SIZE))
            pygame.draw.rect(surface, self.color, sq) # Body parts
            pygame.draw.rect(surface, (89, 89, 83), sq, 1)

    def quit(self):
        pygame.quit()
        sys.exit() # stop running program

# Child class to control player 1's snake
class Player1(Snake):
    def handle_keys(self):
        # If player hits quit - x at top right corner
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.quit()
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

# Child class to control player 2's snake
class Player2(Snake):
    def handle_keys(self):
        # If player hits quit - x at top right corner
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.quit()
            # Check for key down event, move snake accordingly
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_w:
                    self.turn(UP)
                elif event.key == pygame.K_s:
                    self.turn(DOWN)
                elif event.key == pygame.K_a:
                    self.turn(LEFT)
                elif event.key == pygame.K_d:
                    self.turn(RIGHT)

class Food():
    def __init__(self):
        self.posiion = (0, 0) # x, y position
        self.color = (0, 255, 0)
        self.randomize_pos()

    def randomize_pos(self):
        self.position = (random.randint(0, GRID_WIDTH-1) * GRID_SIZE, random.randint(0, GRID_HEIGHT-1) * GRID_SIZE)

    def draw(self, surface):
        block = pygame.Rect((self.position[0], self.position[1]), (GRID_SIZE, GRID_SIZE))
        pygame.draw.rect(surface, self.color, block)
        pygame.draw.rect(surface, (89, 89, 83), block, 1)

# Function(s)
def draw_grid(surface):
    # Loop through grid, rows - x, collumns - y
    for y in range(0, int(GRID_HEIGHT)):
        for x in range(0, int(GRID_WIDTH)):
            # Draw black or white squares depending on the position of square on the grid
            if (x + y) % 2 == 0:
                odd_sq = pygame.Rect(x*GRID_SIZE, y*GRID_SIZE, GRID_SIZE, GRID_SIZE)
                pygame.draw.rect(surface, (211, 211, 211), odd_sq)
            else:
                even_sq = pygame.Rect(x*GRID_SIZE, y*GRID_SIZE, GRID_SIZE, GRID_SIZE)
                pygame.draw.rect(surface, (105, 105, 105), even_sq)

# Global Variable(s)
# Screen specs
SCREEN_WIDTH = 400
SCREEN_HEIGHT = 400

# Grid specs
GRID_SIZE = 20
GRID_WIDTH = SCREEN_HEIGHT / GRID_SIZE
GRID_HEIGHT = SCREEN_WIDTH / GRID_SIZE

# Movement controls - (x, y)
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

    # Initialize snakes for each player
    player_1 = Player1((0, 150, 255)) # Blue snake
    player_2 = Player2((255, 22, 12)) # Red snake
    food = Food() # Green food

    # Execute actions to change game characteristics
    while (True):
        clock.tick(10) # tick at 10 fps
        player_1.handle_keys() # handle key inputs
        # player_2.handle_keys() # handle key inputs
        draw_grid(surface)

        # Check for collisions after moving, updates positions if none detected
        player_1.collision_mangager(player_1.move())
        player_2.collision_mangager(player_2.move())

        # Update game if snake ate food, head pos = food pos
        if player_1.get_head_pos() == food.position:
            player_1.length += 1
            food.randomize_pos()

        if player_2.get_head_pos() == food.position:
            player_2.length += 1
            food.randomize_pos()

        player_1.draw(surface)
        player_2.draw(surface)
        food.draw(surface)

        # Draw surface onto screen
        screen.blit(surface, (0, 0))

        # Update to display changes
        pygame.display.update()

main()