import pygame
from checkers.constants import HEIGHT,WIDTH,SQUARE_SIZE,WHITE,BLACK
from minimax.algorithm import minimax
from checkers.Game import Game


FPS=60
WIN=pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption("checkers")

pygame.font.init()

def get_row_col_from_mouse(pos):
    x,y=pos
    row=y//SQUARE_SIZE
    col=x//SQUARE_SIZE
    return row,col

def draw_winner(text):
    font = pygame.font.SysFont("comicsans", 80)
    # Create the text surface (Blue text)
    draw_text = font.render(text, 1, (0, 0, 255))
    # Calculate position to center it
    x = WIDTH // 2 - draw_text.get_width() // 2
    y = HEIGHT // 2 - draw_text.get_height() // 2
    # Draw text
    WIN.blit(draw_text, (x, y))
    pygame.display.update()



def main():
    run=True
    clock=pygame.time.Clock()
    game=Game(WIN)

    


    while run:
        clock.tick(FPS)

        if game.turn==WHITE:
            value,new_board=minimax(game.get_board(),4,WHITE,game)
            game.ai_move(new_board)

        winner = game.winner()
        
        if winner is not None:
            # Determine the message
            if winner == WHITE:
                msg = "White Wins!"
            elif winner == BLACK:
                msg = "Black Wins!"
            else:
                msg = "Tie Game!"
            
            # Draw the board one last time so we see the final move
            game.update()
            
            # Display the message
            draw_winner(msg)
            
            # Wait 3 seconds so the player can read it, then close
            pygame.time.delay(3000)
            run = False

        
        '''if game.winner()!=None:
            print(game.winner())
            run=False'''

        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                run=False
            if event.type==pygame.MOUSEBUTTONDOWN:
                pos=pygame.mouse.get_pos()
                row,col=get_row_col_from_mouse(pos)
                game.select(row,col)
                
        if run: # Only update if the game is still running
            game.update()

        game.update()
    pygame.quit()
main()