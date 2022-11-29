import pygame

size = width, height = 800, 400
screen = pygame.display.set_mode(size)

running = True
x_pos = 0
while running:
    # внутри игрового цикл еще один цикл
    # приема и обработки сообщений
    events = pygame.event.get()
    for event in events:

        # при закрытии окна
        if event.type == pygame.QUIT:
            running = False

    # отрисовка и изменение свойств объектов
    # ...
    screen.fill((0, 0, 0))
    pygame.draw.circle(screen, (255, 0, 0), (x_pos, 200), 20)
    x_pos += 1

    # обновление экрана
    pygame.display.flip()

pygame.quit()