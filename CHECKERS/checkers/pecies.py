import pygame
from .constants import DARK_BLUE,WHITE,SQUARE_SIZE,GREY,CROWN,BLACK
class Pecie:
    PADDING=10
    OUTLINE=2
    def __init__(self,row,col,color):
        self.row=row
        self.col=col
        self.color=color
        self.king=False
        self.selected=False
        if self.color==BLACK:
            self.direction=-1
        else:
            self.direction=1
        self.x=0
        self.y=0
        self.cal_position()
    def cal_position(self):
        self.x=SQUARE_SIZE*self.col+SQUARE_SIZE//2
        self.y=SQUARE_SIZE*self.row+SQUARE_SIZE//2
    def make_king(self):
        self.king=True
    def draw(self,WIN):
        RADIUS=SQUARE_SIZE//2-self.PADDING
        
        pygame.draw.circle(WIN,GREY,(self.x,self.y),RADIUS+self.OUTLINE)
        pygame.draw.circle(WIN,self.color,(self.x,self.y),RADIUS)
        if self.king:
            WIN.blit(CROWN,(self.x-CROWN.get_width()//2,self.y-CROWN.get_height()//2))

    def move(self,row,col):
        self.row=row
        self.col=col
        self.cal_position()
    def __repr__(self):
        return str(self.color)