import pygame
from game import *

pygame.init()
FPS = 60

window = pygame.display.set_mode((WIDTH, HEIGHT))


def game_over(window, keys):
    text_img = pygame.font.Font.render(pygame.font.SysFont("arial", 72), "Game over", True, (255, 255, 255))
    text_img2 = pygame.font.Font.render(pygame.font.SysFont("arial", 48), "Naciśnij spacje by zrestartować", True,
                                        (255, 255, 255))

    window.blit(text_img, (WIDTH / 2 - text_img.get_width() / 2, HEIGHT / 2 - 100))
    window.blit(text_img2, (WIDTH / 2 - text_img2.get_width() / 2, HEIGHT / 2))
    keys = pygame.key.get_pressed()
    if keys[pygame.K_SPACE]:
        level_one()


def level_one():
    player = Player()
    run = True
    beams = [
        Beam(10, 650, 100, 40),
        Beam(175, 500, 100, 40),
        Beam(500, 675, 100, 40),
        Beam(700, 600, 100, 40),
        Beam(850, 450, 100, 40),
        Beam(1100, 650, 100, 40)
    ]
    coins = [
        Coin(220, 470)
    ]
    portal = Portal(1120, 630)
    while run:
        pygame.time.Clock().tick(60)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                quit()
        KEYS = pygame.key.get_pressed()
        player.tick(KEYS, beams, coins)
        window.fill((0, 0, 0))
        for beam in beams:
            beam.draw(window)
        for coin in coins:
            coin.draw(window)
        portal.draw(window)
        if portal.tick(player.x_cord, player.y_cord):
            level_two()
        if player.y_cord > HEIGHT + 5:
            game_over(window, KEYS)
        player.draw(window)
        pygame.display.update()


def level_two():
    player = Player()
    run = True
    beams = [
        Beam(10, 650, 100, 40),
        Beam(175, 500, 300, 40),
        Beam(350, 350, 100, 40),
        Beam(500, 200, 100, 40),
        Beam(1100, 650, 100, 40),
        Beam(675, 400, 100, 40),
        Beam(800, 200, 100, 40)
    ]
    coins = [
        Coin(545,175)
    ]
    # portal = Portal(1120, 630)
    while run:
        pygame.time.Clock().tick(60)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                quit()
        KEYS = pygame.key.get_pressed()
        player.tick(KEYS, beams, coins)
        window.fill((0, 0, 0))
        for beam in beams:
            beam.draw(window)
        for coin in coins:
            coin.draw(window)
        # portal.draw(window)
        if player.y_cord > HEIGHT + 5:
            game_over(window, KEYS)
        player.draw(window)
        pygame.display.update()


def main():
    run = True
    play_button = Button(320, 350, "play_button")
    while run:
        pygame.time.Clock().tick(60)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
        if play_button.tick():
            level_two()
        window.fill((0, 0, 92))
        play_button.draw(window)
        pygame.display.update()


if __name__ == "__main__":
    main()
