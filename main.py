import pygame
import random
from board import board, pieces, draw_over, colors, no_moves_left
from game_logic import take_turn, new_pieces

pygame.init()

l=800
h=600
# window
screen=pygame.display.set_mode((l,h))
pygame.display.set_caption("2048")
# setting icon to the window
icon =pygame.image.load("icon.png.png")
pygame.display.set_icon(icon)
#fps
fps=60
#font to use in the game
font = pygame.font.Font('freesansbold.ttf', 24)

board_values=[[0 for t in range(4)] for t in range(4)]
game_over=False
spawn_new=True
counter=0
direction=''
score=0
file =open('data/high_score.txt','r')
high=int(file.readline())

file.close()
high_score =high

full=False
running =True  

# kepping the window running
while running:

    # giving colour to the window
    screen.fill((200,195,170))
    board(screen, font, score, high_score)
    pieces(screen, board_values, font)
    if spawn_new or counter<2:
        board_values,full=new_pieces(board_values)
        counter+=1
        spawn_new=False
    if full and no_moves_left(board_values):
         game_over=True
    if direction !=  '' :
        board_values,score =take_turn(direction,board_values,score)
        direction= ''
        spawn_new=True

    if game_over:
        draw_over(screen, font)
        if high_score>high:
            file=open('data/high_score.txt','w')
            file.write(f'{high_score}')
            file.close()
            high=high_score
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running=False
        if event.type ==pygame.KEYUP:
            if event.key ==pygame.K_UP:
                direction ='UP'
            elif event.key ==pygame.K_DOWN:
                direction='DOWN'
            elif event.key ==pygame.K_RIGHT:
                direction='RIGHT'
            elif event.key ==pygame.K_LEFT:
                direction='LEFT'
            if game_over:
                if event.key ==pygame.K_RETURN:
                    board_values=[[0 for i in range(4)]for i in range(4)]
                    spawn_new=True
                    counter=0
                    score=0
                    direction =''
                    game_over=False
                    file=open('data/high_score.txt','w')
                    file.write(str(high_score))
                    file.close()

         
    if score>high_score:
        high_score=score

    pygame.display.update()
