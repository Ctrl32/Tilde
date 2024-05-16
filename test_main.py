import pygame
import UI_gb
import UI
import test_UI

pygame.init()


win_size = UI_gb.ui_surf_size

running = True

win = pygame.display.set_mode(win_size, pygame.RESIZABLE)


while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    UI_gb.ui_surf_size = win.get_size()
    
    ui_surf = UI.update()
    win.blit(ui_surf, (0, 0))

    pygame.display.flip()

pygame.quit()