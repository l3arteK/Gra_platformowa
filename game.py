import pygame

WIDTH = 1200
HEIGHT = 720


class Button:
    def __init__(self, x_cord, y_cord, file_name):
        self.x_cord = x_cord
        self.y_cord = y_cord
        self.button_img = pygame.image.load(f"{file_name}.png")
        self.hovered_button_image = pygame.image.load(f"{file_name}_hovered.png")
        self.hitbox = pygame.Rect(self.x_cord, self.y_cord, self.button_img.get_width(), self.button_img.get_height())

    def tick(self):
        if self.hitbox.collidepoint(pygame.mouse.get_pos()):
            if pygame.mouse.get_pressed()[0]:
                return True

    def draw(self, window):
        if self.hitbox.collidepoint(pygame.mouse.get_pos()):
            window.blit(self.hovered_button_image, (self.x_cord, self.y_cord))
        else:
            window.blit(self.button_img, (self.x_cord, self.y_cord))


class Physic:
    def __init__(self, x, y, acc, max_vel, width, height):
        self.x_cord = x
        self.y_cord = y
        self.hor_velocity = 0
        self.ver_velocity = 0
        self.acc = acc
        self.max_vel = max_vel
        self.width = width
        self.height = height
        self.previous_x = x
        self.previous_y = y
        self.jumping = False
        print(self.x_cord, self.y_cord)

    def physic_tick(self, beams):
        self.ver_velocity += 0.7
        self.hitbox = pygame.Rect(self.x_cord, self.y_cord, self.width, self.height)
        for beam in beams:
            if beam.hitbox.colliderect(self.hitbox):  # cofanie obiektu do miejsca z poprzedniej klatki
                if self.x_cord + self.width >= beam.x_cord + 1 > self.previous_x + self.width:  # kolizja z prawej strony
                    self.x_cord = self.previous_x
                    self.ver_velocity += 0.7
                if self.x_cord <= beam.x_cord + beam.width - 1 < self.previous_x:  # kolizja z lewej strony
                    self.x_cord = self.previous_x
                    self.ver_velocity += 0.7
                if self.y_cord + self.height >= beam.y_cord + 1 > self.previous_y:  # kolizja z góry
                    self.y_cord = self.previous_y
                    self.ver_velocity = 0
                    self.jumping = False
                if self.y_cord <= beam.x_cord + beam.width - 1 < self.previous_y:
                    self.y_cord = self.previous_y
                    self.hor_velocity = 0
        self.previous_x = self.x_cord
        self.previous_y = self.y_cord


class Portal:
    def __init__(self, x, y):
        self.x_cord = x
        self.y_cord = y
        self.width = 20
        self.height = 20
        self.hitbox = pygame.Rect(self.x_cord, self.y_cord, self.width, self.height)

    def draw(self, win):
        pygame.draw.rect(win, (255, 255, 255), self.hitbox)

    def tick(self, x, y):
        self.player_hitbox = pygame.Rect(x, y, 50, 50)
        if self.hitbox.colliderect(self.player_hitbox):
            return True


class Player(Physic):
    def __init__(self):

        self.width = 50
        self.height = 50
        self.x_cord = 50
        self.y_cord = 500
        self.ciekawosc = 100
        self.score = 0
        super().__init__(self.x_cord, self.y_cord, 0.5, 5, self.width, self.height)

    def tick(self, KEYS, beams, coins):
        self.physic_tick(beams)
        if KEYS[pygame.K_a] and self.x_cord > 0 and self.hor_velocity > self.max_vel * -1:
            self.hor_velocity -= self.acc
        if KEYS[pygame.K_d] and self.x_cord < WIDTH - self.width and self.hor_velocity < self.max_vel:
            self.hor_velocity += self.acc
        if KEYS[pygame.K_SPACE] and not self.jumping:
            self.ver_velocity -= 15
            self.jumping = True
        if not (KEYS[pygame.K_d] or KEYS[pygame.K_a]):
            if self.hor_velocity > 0:
                self.hor_velocity -= self.acc
            elif self.hor_velocity < 0:
                self.hor_velocity += self.acc
        self.x_cord += self.hor_velocity
        self.y_cord += self.ver_velocity
        self.hitbox = pygame.Rect(self.x_cord, self.y_cord, self.width, self.height)

        for coin in coins:
            if coin.hitbox.colliderect(self.hitbox):
                coins.remove(coin)
                self.score += 1

    def draw(self, window):
        pygame.draw.rect(window, [200, 150, 100], self.hitbox)


class Beam:
    def __init__(self, x, y, width, height):
        self.x_cord = x
        self.y_cord = y
        self.width = width
        self.height = height
        self.hitbox = pygame.Rect(self.x_cord, self.y_cord, self.width, self.height)

    def draw(self, win):
        pygame.draw.rect(win, (120, 120, 120), self.hitbox)


class Coin:
    def __init__(self, x, y):
        self.x_cord = x
        self.y_cord = y
        self.width = 20
        self.height = 20
        self.hitbox = pygame.Rect(self.x_cord, self.y_cord, self.width, self.height)

    def draw(self, win):
        pygame.draw.rect(win, (255, 255, 0), self.hitbox)
