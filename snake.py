import pygame

def GameRender():
    background_color = (124, 252, 0)
    (width, height) = (400, 400)

    screen = pygame.display.set_mode((width, height))
    pygame.display.set_caption("Snake Clone")
    screen.fill(background_color)

    pygame.display.flip()

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

class Snake():
    def __init__(self, start_pos_x: int, start_pos_y: int, size: int, color = (255, 255, 255)):
        self.start_pos_x = start_pos_x
        self.start_pos_y = start_pos_y
        self.size = size
        self.color = color

    def draw(self):
        snakeRect = pygame.Rect(self.x, self.y, self.size, self.size)
        pygame.draw.rect(self.screen, self.color, snakeRect, border_radius=4)

if __name__ == "__main__":
    GameRender()
    Snake(200, 200, 100)