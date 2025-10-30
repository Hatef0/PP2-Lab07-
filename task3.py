# import pygame

# pygame.init()
# t = pygame.time.Clock()

# a = pygame.display.set_mode((500,500))
# pygame.display.set_caption("ball")

# x,y=250,250

# pygame.draw.circle(a, (200,0,0), (x,y), 25, 0)

# run = True
# while run:
#     a.fill((255,255,255))
#     for i in pygame.event.get():
#         if i.type == pygame.QUIT:
#             run = False
#             pygame.quit()

#     u = pygame.key.get_pressed()
#     if u[pygame.K_w] and y-20>=25:
#         y-=20
#     elif u[pygame.K_d] and x+20<=475:
#         x+=20
#     elif u[pygame.K_a] and x-20>=25:
#         x-=20
#     elif u[pygame.K_s] and y+20<=475:
#         y+=20

#     pygame.draw.circle(a, (200,0,0), (x,y), 25, 0)
#     pygame.display.update()
#     t.tick(25)



import pygame

pygame.init()
clock = pygame.time.Clock()

screen = pygame.display.set_mode((500, 500))
pygame.display.set_caption("Moving Red Ball")

x, y = 250, 250
radius = 25
speed = 20

running = True
while running:
    screen.fill((255, 255, 255))
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    keys = pygame.key.get_pressed()

    if keys[pygame.K_UP] and y - speed >= radius:
        y -= speed
    if keys[pygame.K_DOWN] and y + speed <= 500 - radius:
        y += speed
    if keys[pygame.K_LEFT] and x - speed >= radius:
        x -= speed
    if keys[pygame.K_RIGHT] and x + speed <= 500 - radius:
        x += speed

    pygame.draw.circle(screen, (255, 0, 0), (x, y), radius)
    pygame.display.flip()
    clock.tick(30)

pygame.quit()