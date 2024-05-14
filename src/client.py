import pygame
from network import Network
from player import Player
from constants import BLACK, SCREEN_HEIGHT, SCREEN_WIDTH
import pygame.font
pygame.font.init()
font = pygame.font.SysFont(None, 50)  

win = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Client")

def draw_text(text, font, color, surface, x, y):
    text_obj = font.render(text, True, color)   
    text_rect = text_obj.get_rect()
    text_rect.center = (x, y)
    surface.blit(text_obj, text_rect)

    pygame.display.update()

def redrawWindow(win, player, player2):
    win.fill(BLACK)
    player.draw(win)
    player2.draw(win)
 
    for bullet in player.bullets:
        bullet.draw(win)
    for bullet in player2.bullets:
        bullet.speed = bullet.speed
        bullet.draw(win)

    if player.nid == 1:
        draw_text(f"Player {player.nid} Health: {player.health}", font, (255, 255, 255), win, 200, 50)
        draw_text(f"Player {player2.nid} Health: {player2.health}", font, (255, 255, 255), win, SCREEN_WIDTH - 200, 50)
    else:
        draw_text(f"Player {player2.nid} Health: {player2.health}", font, (255, 255, 255), win, 200, 50)
        draw_text(f"Player {player.nid} Health: {player.health}", font, (255, 255, 255), win, SCREEN_WIDTH - 200, 50)

    pygame.display.update()


def main():
    run = True
    n = Network()
    p = n.getP()
    clock = pygame.time.Clock()

    while run:
        clock.tick(60)
        p2 = n.send(p)
        print(p2)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                pygame.quit()

        p.move()

        to_remove = p.collide(p2.bullets)
        if to_remove != -1:
            p2.bullets.pop(to_remove)
        
        to_remove = p2.collide(p.bullets)
        if to_remove != -1:
            p.bullets.pop(to_remove)

        if p.health <= 0 or p2.health <= 0:
            if p.health <= 0:
                winner = p2.nid
            else:
                winner = p.nid

            draw_text(f"Player {winner} wins!", font, (255, 255, 255), win, SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2)
            pygame.display.update()
            pygame.time.wait(5000)
            run = False
            
        redrawWindow(win, p, p2)

main()