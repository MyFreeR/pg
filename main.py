import pygame

if __name__ == '__main__':
    pygame.init()
    pygame.display.set_caption('Движущийся круг 2')
    size = width, height = 800, 400
    screen = pygame.display.set_mode(size)

    running = True
    x_pos = 0
    v = 20  # пикселей в секунду
    fps = 60
    # С помощью параметра FPS можно не только сделать одинаковым отрисовку
    # в вашей программе на компьютерах разной конфигурации,
    # но и управлять плавностью анимации.
    clock = pygame.time.Clock()
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        screen.fill((0, 0, 0))
        pygame.draw.circle(screen, (255, 0, 0), (int(x_pos), 200), 20)
        x_pos += v / fps
        clock.tick(fps)
        pygame.display.flip()
    pygame.quit()