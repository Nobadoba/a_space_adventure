from functions import *
import txt

pygame.display.set_caption('AN ADVENTURE IN SPACE')

speed = 3
y_pos = 300
z_pos= "ApolloIsDumb"
x_pos = 300
pas = 0

# ==== start sequence backdrop ====
space = pygame.image.load('graphics/space.png')
space = pygame.transform.scale(space, (screen_width, screen_height))


# ==== spaceship animation ====
spaceship = [
    pygame.transform.scale(pygame.image.load('graphics/spaceship_1.png').convert_alpha(), (80, 100)),
    # Backdrop stays transparent
    pygame.transform.scale(pygame.image.load('graphics/spaceship_2.png').convert_alpha(), (80, 100))
]
s_rect = [
    spaceship[0].get_rect(),
    spaceship[1].get_rect()
]
for i in s_rect:  # both frames are affected
    i.topleft = (300, 200)
last_update = pygame.time.get_ticks()
animation_cooldown = 500  # the frame changes every 0.5 seconds
frame = 0

# ===='creates' the earth====
earth = pygame.transform.scale(pygame.image.load('graphics/earth.png').convert_alpha(), (700, 700))
earth.get_rect()  # for collision detection

status_1 = True

while True:
    # update animation
    screen.blit(space, (0, 0))
    screen.blit(earth, (10, -1000 + 30 * pas))
    screen.blit(spaceship[frame], s_rect[frame])
    while status_1:
        typewrite(txt.Intro.first, 'stand')
        status_1 = False

    pygame.draw.rect(screen, 'black', [0, screen_height - 150, screen_width, 200])
    screen.blit(font.render(txt.Intro.first[-1], True, 'white'), stand_pos)
    timer.tick(60)  # den kører på 60 fps
    for event in pygame.event.get():
        if event.type == pygame.QUIT:  # you can exit the code
            pygame.quit()
            exit()
    current_time = pygame.time.get_ticks()
    if current_time - last_update >= animation_cooldown:  # makes the frame change, if the cooldown is over
        frame += 1
        pas += 0.5
        last_update = current_time
        if frame >= len(spaceship):  # the number of frames is consistent with the amount of frames in the animation
            frame = 0
    key = pygame.key.get_pressed()
    if key[pygame.K_w] or key[pygame.K_UP]:  # spaceship moves up
        s_rect[0].y -= speed
        s_rect[1].y -= speed
    if key[pygame.K_s] or key[pygame.K_DOWN]:  # spaceship moves down
        s_rect[0].y += speed
        s_rect[1].y += speed
    if key[pygame.K_a] or key[pygame.K_LEFT] and s_rect[frame].x != 0:  # spaceship moves left
        s_rect[0].x -= speed
        s_rect[1].x -= speed
    if key[pygame.K_d] or key[pygame.K_RIGHT] and s_rect[frame].x != 600:  # spaceship moves right
        s_rect[0].x += speed
        s_rect[1].x += speed
    if s_rect[0].y < -250:  # if you move too far up, you get moved down automatically
        s_rect[0].y = 300
        s_rect[1].y = 300
        pas += 1

    pygame.display.flip()

    # screen.fill("white")
    """
    typewrite(['Hej, Lena', 'Velkommen til dette eksamensprojekt', 'Haber du syntes det er ok.'], 'stand')
    screen.fill("white")
    typewrite(['AN ADVENTURE'], 'title')
    screen.fill("white")
    typewrite(['IN SPACE'], 'title')

    
    pygame.draw.rect(screen, 'black', [0, screen_height - 150, screen_width, 200], )
    if choose("Fine", 'Bad', "How are you doing?") == 'Fine':
        typewrite(['That is awesome!', 'I am happy for you!'], 'stand')
    else:
        typewrite(["I'm sorry.", 'I hope you will feel better someday.'], 'stand')"""
