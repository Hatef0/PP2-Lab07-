# import pygame
# import sys

# pygame.init()
# pygame.mixer.init()

# a = pygame.display.set_mode((300, 300))
# pygame.display.set_caption("Sound Player")

# try:
#     e=[
#     pygame.mixer.Sound(r"/Users/hatefchalak/Desktop/Lab_07/fixed1.wav"),
#     pygame.mixer.Sound(r"/Users/hatefchalak/Desktop/Lab_07/fixed2.wav"),
#     pygame.mixer.Sound(r"/Users/hatefchalak/Desktop/Lab_07/fixed3.wav")
# ]
# except pygame.error as e:
#     print("Error loading sound files:", e)
#     pygame.quit()
#     sys.exit()

# j = 0
# run = True
# while run:
#     for u in pygame.event.get():
#         if u.type == pygame.QUIT:
#             run = False
#         elif u.type == pygame.KEYDOWN:
#             if u.key == pygame.K_q:
#                 j = (j - 1) % 3
#             elif u.key == pygame.K_w:
#                 j = (j + 1) % 3
#             elif u.key == pygame.K_SPACE:
#                 sounds[j].play()
#             elif u.key == pygame.K_TAB:
#                 sounds[j].stop()
#             elif u.key == pygame.K_ESCAPE:
#                 run = False
#     pygame.display.update()

# pygame.quit()


import pygame
import sys

pygame.init()
pygame.mixer.init()

a = pygame.display.set_mode((400, 300))
pygame.display.set_caption("Sound Player")

sounds = [
    pygame.mixer.Sound(r"/Users/hatefchalak/Desktop/Lab_07/fixed1.wav"),
    pygame.mixer.Sound(r"/Users/hatefchalak/Desktop/Lab_07/fixed2.wav"),
    pygame.mixer.Sound(r"/Users/hatefchalak/Desktop/Lab_07/fixed3.wav")
]

j = 0
font = pygame.font.SysFont(None, 30)

run = True
while run:
    for u in pygame.event.get():
        if u.type == pygame.QUIT:
            run = False
        elif u.type == pygame.KEYDOWN:
            if u.key == pygame.K_q:
                j = (j - 1) % len(sounds)
            elif u.key == pygame.K_w:
                j = (j + 1) % len(sounds)
            elif u.key == pygame.K_SPACE:
                sounds[j].play()
            elif u.key == pygame.K_TAB:
                sounds[j].stop()
            elif u.key == pygame.K_ESCAPE:
                run = False

    a.fill((0, 0, 0))
    text = font.render(f"Track {j+1}", True, (255, 255, 255))
    a.blit(text, (150, 130))
    pygame.display.flip()

pygame.quit()
sys.exit()