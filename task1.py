# import pygame
# import datetime

# pygame.init()

# a = pygame.display.set_mode((1000,650))
# pygame.display.set_caption("Second")

# b = pygame.image.load("/Users/hatefchalak/Desktop/Lab_07/clock.png")
# b = pygame.transform.scale(b,(1000, 650))

# h = pygame.image.load(r"/Users/hatefchalak/Desktop/Lab_07/rightarm.png")
# h = pygame.transform.scale(h,(1000,700))

# c = pygame.image.load(r"/Users/hatefchalak/Desktop/Lab_07/leftarm.png")
# c = pygame.transform.scale(c,(40,640))

# run = True
# while run:
#     for i in pygame.event.get():
#         if i.type == pygame.QUIT:
#             run = False
#             pygame.quit()
#     a.blit(b,(0,0))

#     x=datetime.datetime.now().hour%12
#     e = c.get_rect(center=(490,320))
#     f = pygame.transform.rotate(c,x*(-30))
#     g = f.get_rect(center=e.center)
#     a.blit(f,g)

#     x=datetime.datetime.now().minute
#     e = h.get_rect(center=(505,340))
#     f = pygame.transform.rotate(h,x*(-6)+55)
#     g = f.get_rect(center=e.center)
#     a.blit(f,g)

#     pygame.display.update()
# ----------------------------------------------------------------------
# import pygame
# import datetime

# pygame.init()

# a = pygame.display.set_mode((1000,650))
# pygame.display.set_caption("Mickey Clock")

# b = pygame.image.load("/Users/hatefchalak/Desktop/Lab_07/clock.png")
# b = pygame.transform.scale(b,(1000, 650))

# h = pygame.image.load(r"/Users/hatefchalak/Desktop/Lab_07/rightarm.png")
# h = pygame.transform.scale(h,(1000,700))

# c = pygame.image.load(r"/Users/hatefchalak/Desktop/Lab_07/leftarm.png")
# c = pygame.transform.scale(c,(40,640))

# t = pygame.time.Clock()
# run = True
# while run:
#     for i in pygame.event.get():
#         if i.type == pygame.QUIT:
#             run = False
#             pygame.quit()
    
#     a.blit(b,(0,0))
    
#     now = datetime.datetime.now()
#     minutes = now.minute
#     seconds = now.second

#     e = h.get_rect(center=(500,325))
#     f = pygame.transform.rotate(h, -6 * minutes)
#     g = f.get_rect(center=e.center)
#     a.blit(f,g)

#     e = c.get_rect(center=(500,325))
#     f = pygame.transform.rotate(c, -6 * seconds)
#     g = f.get_rect(center=e.center)
#     a.blit(f,g)

#     pygame.display.update()
#     t.tick(30)
# ----------------------------------------------------------------------

import pygame
import datetime

pygame.init()

a = pygame.display.set_mode((1000,650))
pygame.display.set_caption("Mickey Clock")

b = pygame.image.load("/Users/hatefchalak/Desktop/Lab_07/clock.png")
b = pygame.transform.scale(b,(1000, 650))

h = pygame.image.load(r"/Users/hatefchalak/Desktop/Lab_07/rightarm.png")
h = pygame.transform.scale(h,(1000,700))

c = pygame.image.load(r"/Users/hatefchalak/Desktop/Lab_07/leftarm.png")
c = pygame.transform.scale(c,(40,640))

t = pygame.time.Clock()
run = True
while run:
    for i in pygame.event.get():
        if i.type == pygame.QUIT:
            run = False
            pygame.quit()
    
    a.blit(b,(0,0))
    
    now = datetime.datetime.now()
    minutes = now.minute
    seconds = now.second

    corrected_minutes = (minutes - 10) % 60

    e = h.get_rect(center=(500,325))
    f = pygame.transform.rotate(h, -6 * corrected_minutes)
    g = f.get_rect(center=e.center)
    a.blit(f,g)

    e = c.get_rect(center=(500,325))
    f = pygame.transform.rotate(c, -6 * seconds)
    g = f.get_rect(center=e.center)
    a.blit(f,g)

    pygame.display.update()
    t.tick(30)

