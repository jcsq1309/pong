import pygame

pygame.init()

# criação da janela
WIDTH = 893
HEIGHT = 1000
size = (WIDTH, HEIGHT)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Breakout Game")
# controlar o tempo
clock = pygame.time.Clock()
fps_rate = 68

# cores utilizadas (rgb)
white = (255, 255, 255)
grey = (212, 218, 212)
black = (0, 0, 0)
blue = (0, 97, 148)

red = (162, 8, 8)
orange = (183, 119, 0)
green = (0, 127, 33)
yellow = (197, 199, 37)

# tamanho das raquetes
paddle_width = 54
paddle_height = 20

# classe para armazenar objetos
all_spites_list = pygame.sprite.Group()

# tijolos
class Brick(pygame.sprite.Sprite):

    def __int__(self, color, width, height):
        super().__init__()
        self.image = pygame.Surface([width, height])
        pygame.draw.rect(self.image, color, [0, 0, width, height]) # criacao do retangulo
        self.rect = self.image.get_rect()

all_bricks = pygame.sprite.Group()

# criacao dos bricks (tijolos)
brick_width = 55
brick_height = 16
x_gap = 7
y_gap = 5
wall_width = 16

# criacao dos tijolos
def bricks():
    for j in range(8):
        for i in range(14):
            if j < 2:
                if i == 0:
                    brick = Brick(RED, brick_width, brick_height)
                    brick.rect.x = wall_width
                    brick.rect.y = 215 + j * (y_gap + brick_height)
                    all_sprites_list.add(brick)
                    all_bricks.add(brick)
                else:
                    brick = Brick(RED, brick_width, brick_height)
                    brick.rect.x = wall_width + brick_width + x_gap + (i - 1) * (brick_width + x_gap)
                    brick.rect.y = 215 + j * (y_gap + brick_height)
                    all_sprites_list.add(brick)
                    all_bricks.add(brick)
            if 1 < j < 4:
                if i == 0:
                    brick = Brick(ORANGE, brick_width, brick_height)
                    brick.rect.x = wall_width
                    brick.rect.y = 215 + j * (y_gap + brick_height)
                    all_sprites_list.add(brick)
                    all_bricks.add(brick)
                else:
                    brick = Brick(ORANGE, brick_width, brick_height)
                    brick.rect.x = wall_width + brick_width + x_gap + (i - 1) * (brick_width + x_gap)
                    brick.rect.y = 215 + j * (y_gap + brick_height)
                    all_sprites_list.add(brick)
                    all_bricks.add(brick)
            if 3 < j < 6:
                if i == 0:
                    brick = Brick(GREEN, brick_width, brick_height)
                    brick.rect.x = wall_width
                    brick.rect.y = 215 + j * (y_gap + brick_height)
                    all_sprites_list.add(brick)
                    all_bricks.add(brick)
                else:
                    brick = Brick(GREEN, brick_width, brick_height)
                    brick.rect.x = wall_width + brick_width + x_gap + (i - 1) * (brick_width + x_gap)
                    brick.rect.y = 215 + j * (y_gap + brick_height)
                    all_sprites_list.add(brick)
                    all_bricks.add(brick)
            if 5 < j < 8:
                if i == 0:
                    brick = Brick(YELLOW, brick_width, brick_height)
                    brick.rect.x = wall_width
                    brick.rect.y = 215 + j * (y_gap + brick_height)
                    all_sprites_list.add(brick)
                    all_bricks.add(brick)
                else:
                    brick = Brick(YELLOW, brick_width, brick_height)
                    brick.rect.x = wall_width + brick_width + x_gap + (i - 1) * (brick_width + x_gap)
                    brick.rect.y = 215 + j * (y_gap + brick_height)
                    all_sprites_list.add(brick)
                    all_bricks.add(brick)


brick_wall = bricks()


def main():
    clock.tick(fps_rate)

    run = True
    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

            all_spites_list.update()

            screen.fill(black)

            # bordas - parametros (surface, color, start_pos, end_pos, espessura)
            pygame.draw.line(screen, grey, [8, 19], [width, 19], 48)
            pygame.draw.line(screen, GREY, [(wall_width / 2) - 1, 0], [(wall_width / 2) - 1, HEIGHT], wall_width)
            pygame.draw.line(screen, GREY, [(WIDTH - wall_width / 2) - 1, 0], [(WIDTH - wall_width / 2) - 1, HEIGHT],
                             wall_width)

            pygame.draw.line(screen, BLUE, [(wall_width / 2) - 1, HEIGHT - 65 + paddle_height / 2 - 54 / 2],
                             [(wall_width / 2) - 1, HEIGHT - 65 + paddle_height / 2 - 54 / 2 + 54], wall_width)
            pygame.draw.line(screen, BLUE, [(WIDTH - wall_width / 2) - 1, HEIGHT - 65 + paddle_height / 2 - 54 / 2],
                             [(WIDTH - wall_width / 2) - 1, HEIGHT - 65 + paddle_height / 2 - 54 / 2 + 54], wall_width)

            pygame.draw.line(screen, RED, [(wall_width / 2) - 1, 212.5],
                             [(wall_width / 2) - 1, 212.5 + 2 * brick_height + 2 * y_gap], wall_width)
            pygame.draw.line(screen, RED, [(WIDTH - wall_width / 2) - 1, 212.5],
                             [(WIDTH - wall_width / 2) - 1, 212.5 + 2 * brick_height + 2 * y_gap], wall_width)

            pygame.draw.line(screen, ORANGE, [(wall_width / 2) - 1, 212.5 + 2 * brick_height + 2 * y_gap],
                             [(wall_width / 2) - 1, 212.5 + 4 * brick_height + 4 * y_gap], wall_width)
            pygame.draw.line(screen, ORANGE, [(WIDTH - wall_width / 2) - 1, 212.5 + 2 * brick_height + 2 * y_gap],
                             [(WIDTH - wall_width / 2) - 1, 212.5 + 4 * brick_height + 4 * y_gap], wall_width)

            pygame.draw.line(screen, GREEN, [(wall_width / 2) - 1, 212.5 + 4 * brick_height + 4 * y_gap],
                             [(wall_width / 2) - 1, 212.5 + 6 * brick_height + 6 * y_gap], wall_width)
            pygame.draw.line(screen, GREEN, [(WIDTH - wall_width / 2) - 1, 212.5 + 4 * brick_height + 4 * y_gap],
                             [(WIDTH - wall_width / 2) - 1, 212.5 + 6 * brick_height + 6 * y_gap], wall_width)

            pygame.draw.line(screen, YELLOW, [(wall_width / 2) - 1, 212.5 + 6 * brick_height + 6 * y_gap],
                             [(wall_width / 2) - 1, 212.5 + 8 * brick_height + 8 * y_gap], wall_width)
            pygame.draw.line(screen, YELLOW, [(WIDTH - wall_width / 2) - 1, 212.5 + 6 * brick_height + 6 * y_gap],
                             [(WIDTH - wall_width / 2) - 1, 212.5 + 8 * brick_height + 8 * y_gap], wall_width)

            all_spites_list.draw(screen)

            pygame.display.update()

        pygame.quit()


    main()