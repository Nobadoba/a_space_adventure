import pygame
pygame.init()
back = 'red'
title_pos = (75, 200)
stand_pos = (10, 360)
char_pos = (160, 360)
font = pygame.font.Font("Minecraft.ttf", 42)
screen_width = 800
screen_height = 500
screen = pygame.display.set_mode([screen_width, screen_height])

timer = pygame.time.Clock()


def typewrite(text_list, type):
    # Makes the variables accessible
    global timer, msg
    counter = 0
    speed = 3
    active_message = 0
    done = False
    message = text_list[active_message]
    run = True
    while run:
        timer.tick(60)  # Code runs at 60fps
        if type != 'title':
            pygame.draw.rect(screen, 'black', [0, screen_height - 150, screen_width, 200])
        if counter < speed * len(message):  # Counts how many characters to write (* speed)
            counter += 1
        elif counter >= speed * len(message):  # If the message is finished, stop counting
            done = True
        for events in pygame.event.get():
            if events.type == pygame.QUIT:  # You can exit the program even if the code is running
                pygame.quit()
                exit()
            if events.type == pygame.KEYDOWN:
                if events.key == pygame.K_RETURN and not done:
                    speed = 1
                elif events.key == pygame.K_RETURN and done and active_message < len(text_list) - 1:
                    # Print the next message
                    active_message += 1
                    message = text_list[active_message]
                    # Resets the counter for the next message
                    counter = 0
                    speed = 3
                    done = False
                elif done and active_message == len(text_list) - 1:
                    run = False
        # returns the text, updates for every character
        # Speed decreases the amount of text stored every frame
        snip = font.render(message[0:counter//speed], True, 'white')
        if type == 'stand':
            screen.blit(snip, (10, 360))
        if type == 'char':
            screen.blit(snip, (160, 360))
        if type == 'title':
            snip = pygame.font.Font("Minecraft.ttf", 75).render(message[0:counter // speed], True, 'black')
            screen.blit(snip, (75, 200))
        pygame.display.flip()
    return 'fin'


def choose(opt_1, opt_2, mes):
    up = False
    run = True
    while run:
        font_new = pygame.font.Font("Minecraft.ttf", 40)
        txt = font_new.render(opt_1, True, 'white')
        screen.blit(txt, (500, 370))
        txt = font_new.render(opt_2, True, 'white')
        screen.blit(txt, (500, 430))
        txt = font_new.render(mes, True, 'white')
        screen.blit(txt, (10, 370))
        for events in pygame.event.get():
            if events.type == pygame.QUIT:  # You can exit the program even if the code is running
                pygame.quit()
                exit()
            if events.type == pygame.KEYDOWN:
                if events.key == pygame.K_DOWN:  # arrow moves down
                    pygame.draw.rect(screen, 'black', [465, screen_height - 150, 30, 200])
                    up = True
                    pygame.draw.polygon(screen, 'white', ((470, 430), (485, 430 + 10), (470, 430 + 20)))
                elif events.key == pygame.K_UP:  # arrow moves up
                    pygame.draw.rect(screen, 'black', [465, screen_height - 150, 30, 200])
                    up = False
                    pygame.draw.polygon(screen, 'white', ((470, 375), (485, 375 + 10), (470, 375 + 20)))
                if events.key == pygame.K_RETURN and up:
                    return opt_2
                if events.key == pygame.K_RETURN and not up:
                    return opt_1
        pygame.display.flip()


