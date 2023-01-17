import classes
import pygame

# Set width and height of window
WIDTH, HEIGHT = 900, 500
WINDOW = pygame.display.set_mode((WIDTH, HEIGHT))
# Set window display name
pygame.display.set_caption("Crossy Road Mini-Game")

WHITE = (255, 255, 255)

# Run main function
def main():

    # Repeatdly run events
    run = True
    while run:
        
        # Loop through events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        WINDOW.fill(WHITE)
        pygame.display.update()

    pygame.quit

# Check if main.py file is ran directly, call on main funct if so
if __name__ == "__main__":
    main()
