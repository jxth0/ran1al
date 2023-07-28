import pygame, sys
from random import randint, choice

FPS = 60
SCREEN_WIDTH = 700
SCREEN_HEIGHT = 550
PLAYER_SPEED = 6
PLAYER_SIZE = (50,50)
ENEMY_SIZE = (25,25)
GRAVITY = 0.3
screen = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))
pygame.display.set_caption('Square Game')
clock = pygame.time.Clock()

class Player(pygame.sprite.Sprite):
    def __init__(self,pos,groups,obstacles):
        super().__init__(groups)
        self.obstacles = obstacles
        self.image = pygame.Surface(PLAYER_SIZE)
        self.image.fill((0,255,25))
        self.rect = self.image.get_rect(center = pos)
        self.speed = PLAYER_SPEED
        self.gravity = GRAVITY
        self.direction = 1
        self.jump = False
        self.in_air = True
        self.vel_y = 0
    
    def keys_inputs(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_d]:
            self.direction = 1
            self.move()
        if keys[pygame.K_a]:
            self.direction = -1
            self.move()
        if keys[pygame.K_w]:
            self.vel_y = -10

    def move(self):
        self.rect.x += self.speed * self.direction
    
    def collision(self):
        for obstacle in self.obstacles.sprites():
            if self.rect.colliderect(obstacle.rect):
                if self.in_air:
                    if self.jump:
                        self.rect.top = obstacle.bottom
                    else:
                        self.rect.bottom = obstacle.top
                else:
                    if self.direction == 1:
                        self.rect.right = obstacle.rect.left
                    if self.direction == -1:
                        self.rect.left = obstacle.rect.right

    def apply_gravity(self):
        if self.vel_y < 10: self.vel_y += self.gravity
        self.rect.y += self.vel_y

    def draw(self):
        screen.blit(self.image,self.rect)

    def update(self):
        self.keys_inputs()
        self.apply_gravity()
        self.collision()
        self.draw()

class Enemy(pygame.sprite.Sprite):
    def __init__(self,pos,groups):
        super().__init__(groups)
        self.image = pygame.Surface(ENEMY_SIZE)
        self.rect = self.image.get_rect(center = pos)
        self.vel_y = 0
    
    def draw(self):
        screen.blit(self.image,self.rect)

    def update(self):
        self.draw()

enemy_group = pygame.sprite.Group()
player = Player()


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    screen.fill((0,0,0))

    player.update()
    enemy_group.update()

    pygame.display.update()
    clock.tick(FPS)