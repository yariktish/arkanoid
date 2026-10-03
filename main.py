import pygame
pygame.init()


window = pygame.display.set_mode((500, 500))
window.fill((0, 171, 253))


clock = pygame.time.Clock()


class Area():
    def __init__(self, x=0, y=0, width=10, height=10, color=(0, 171, 253)):
        self.rect = pygame.Rect(x, y, width, height)
        self.fill_color = color
    def color(self, new_color):
        self.fill_color = new_color
    def fill(self):
        pygame.draw.rect(window, self.fill_color, self.rect)
    def colliderect(self, rect):
        return self.rect.colliderect(rect)


class Picture(Area):
    def __init__(self, file_name, x=0, y=0, width=10, height=10, color=(0, 171, 253)):
        super().__init__(x=x, y=y, width=width, height=height, color=(0, 171, 253))
        self.image = pygame.image.load(file_name)
    def draw(self):#размещение картоочки
        window.blit(self.image, (self.rect.x, self.rect.y))


move_left = False
move_right = False

ball = Picture('ball.png', 200, 200, 50, 50)
platform = Picture('platform.png', 350, 350, 120, 50)

start_x = 0
start_y = 0

speed_x = 3
speed_y = 3

platform_y = 350

enemies = list()
n = 9
for j in range(3):
    x = start_x + (27 * j)
    y = start_y + (55 * j)
    for i in range(n):
        enemy = Picture('enemy.png', x, y, 50, 50)
        enemies.append(enemy)
        x += 55
    n -= 1


while True:
    platform.fill()
    ball.fill()
    ball.rect.x += speed_x
    ball.rect.y += speed_y
    for enemy in enemies:
        enemy.draw()
        if enemy.rect.colliderect(ball.rect):
            enemies.remove(enemy)
            enemy.fill()
            speed_y *= -1
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                move_right = True
            elif event.key == pygame.K_LEFT:
                move_left = True
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_RIGHT:
                move_right = False
            elif event.key == pygame.K_LEFT:
                move_left = False
    if move_right:
        platform.rect.x += 5
    elif move_left:
        platform.rect.x -= 5
    platform.draw()
    ball.draw()
    if ball.colliderect(platform.rect):
        speed_y *= -1
    if ball.rect.y < 0:
        speed_y *= -1
    if ball.rect.x >= 450 or ball.rect.x <= 0:
        speed_x *= -1
    if ball.rect.y > (platform_y + 20):
        font1 = pygame.font.SysFont('verdana', 80).render('Game over', True, (230, 0, 0))
        window.blit(font1, (100, 200))
        break
    if len(enemies) == 0:
        font1 = pygame.font.SysFont('verdana', 80).render('You win', True, (230, 0, 0))
        window.blit(font1, (100, 200))
        break
    clock.tick(40)
    pygame.display.update()
pygame.display.update()
