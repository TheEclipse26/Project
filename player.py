import pygame


class Player(pygame.sprite.Sprite):
    def __init__(self, pos):
        super().__init__()
        self.image = pygame.Surface((32, 64))
        self.image.fill("red")
        self.rect = self.image.get_rect(topleft=pos)
        # player_now = pygame.image.load("Red_Square.png").convert_alpha()
        # player_1 = pygame.image.load("e/graphics/player/player_walk_1.png").convert_alpha()
        # player_2 = pygame.image.load("e/graphics/player/player_walk_2.png").convert_alpha()
        # self.player_walk = [player_1, player_2]
        # self.player_walk = [player_now]
        # self.player_index = 0
        # self.player_jump = pygame.image.load("e/graphics/player/jump.png").convert_alpha()
        # self.image = self.player_walk[self.player_index]
        # self.image = self.player_walk[self.player_index]

        # self.jump_sound = pygame.mixer.Sound("e/audio/jump.mp3")
        # self.jump_sound.set_volume(0.5)

        # Player movement
        self.direction = pygame.math.Vector2(0, 0)
        self.speed = 8
        self.gravity = 0.8
        self.jump_speed = -16

    def get_input(self):
        keys = pygame.key.get_pressed()
        # if keys[pygame.K_SPACE] and self.rect.bottom >= 400:
        #     self.gravity = -20
        #     # self.jump_sound.play()
        if keys[pygame.K_RIGHT]:
            self.direction.x = 1
        elif keys[pygame.K_LEFT]:
            self.direction.x = -1
        else:
            self.direction.x = 0

        if keys[pygame.K_SPACE] and self.direction.y == 0:
            self.jump()

    def apply_gravity(self):
        self.direction.y += self.gravity
        self.rect.y += self.direction.y

    # def animation_state(self):
    #     if self.rect.bottom < 300:
    #         self.image = self.player_jump
    #     else:
    #         self.player_index += 0.1
    #         if self.player_index >= len(self.player_walk):
    #             self.player_index = 0
    #         self.image = self.player_walk[int(self.player_index)]

    def jump(self):
        self.direction.y = self.jump_speed

    def update(self):
        self.get_input()
        # self.animation_state()
