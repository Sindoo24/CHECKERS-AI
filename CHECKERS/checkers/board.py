import pygame
from .constants import DARK_BLUE, LIGHT_BLUE, ROWS, SQUARE_SIZE, COLS, BLACK, WHITE
from .pecies import Pecie

class Board:
    def __init__(self):
        self.board=[]
        self.BLACK_LEFT=self.WHITE_LEFT=12
        self.BLACK_KINGS=self.WHITE_KINGS=0
        self.create_board()

    def draw_squares(self, WIN):
        WIN.fill(LIGHT_BLUE)
        for row in range(ROWS):
            for col in range(row%2,COLS,2):
                pygame.draw.rect(WIN,DARK_BLUE,(row*SQUARE_SIZE,col*SQUARE_SIZE,SQUARE_SIZE,SQUARE_SIZE))

    def evaluate(self):
        return self.WHITE_LEFT - self.BLACK_LEFT + (self.WHITE_KINGS * 0.5 - self.BLACK_KINGS * 0.5)
    
    def get_all_pecies(self,color):
        pecies=[]
        for row in self.board:
            for pecie in row:
                if pecie!=0 and pecie.color==color:
                    pecies.append(pecie)
        return pecies
    def move(self,pecie,row,col):
        self.board[pecie.row][pecie.col],self.board[row][col]=self.board[row][col],self.board[pecie.row][pecie.col]
        pecie.move(row,col)

        if row==ROWS-1 or row==0:
            pecie.make_king()
            if pecie.color==WHITE:
                self.WHITE_KINGS+=1
            else:
                self.BLACK_KINGS+=1


    def get_pecie(self,row,col):
        return self.board[row][col]

    def create_board(self):
        for row in range(ROWS):
            self.board.append([])
            for col in range(COLS):
                if col%2==((row+1)%2):
                    if row<3:
                        self.board[row].append(Pecie(row,col,WHITE))
                    elif row>4:
                        self.board[row].append(Pecie(row,col,BLACK))
                    else:
                        self.board[row].append(0)
                else:
                    self.board[row].append(0)

    def draw(self,WIN):
        self.draw_squares(WIN)
        for row in range(ROWS):
            for col in range(COLS):
                Pecie=self.board[row][col]
                if Pecie!=0:
                    Pecie.draw(WIN)
    
    def remove(self,pecies):
        for pecie in pecies:
            if pecie != 0:
                if self.board[pecie.row][pecie.col] != 0:
                    self.board[pecie.row][pecie.col] = 0
                    if pecie.color == BLACK:
                        self.BLACK_LEFT -= 1
                    else:
                        self.WHITE_LEFT -= 1
        '''for pecie in pecies:
            self.board[pecie.row][pecie.col]=0
            if pecie != 0:
                if pecie.color == BLACK:
                    self.BLACK_LEFT -= 1
                else:
                    self.WHITE_LEFT -= 1'''

    def winner(self):
        if self.BLACK_LEFT<= 0:
            return WHITE
        elif self.WHITE_LEFT <= 0:
            return BLACK
        
        return None 


    def get_valid_moves(self,pecie):
        moves={}
        left=pecie.col-1
        right=pecie.col+1
        row=pecie.row

        if pecie.color==BLACK or pecie.king:
            moves.update(self._traverse_left(row-1,max(row-3,-1),-1,pecie.color,left))
            moves.update(self._traverse_right(row-1,max(row-3,-1),-1,pecie.color,right))

        if pecie.color==WHITE or pecie.king:
            moves.update(self._traverse_left(row+1,min(row+3,ROWS),1,pecie.color,left))
            moves.update(self._traverse_right(row+1,min(row+3,ROWS),1,pecie.color,right))

        return moves
    
    def _traverse_left(self,start,stop,step,color,left,skipped=[]):
        moves={}
        last=[]
        for r in range(start,stop,step):
            if left<0:
                break

            current=self.board[r][left]
            if current==0:
                if skipped and not last:
                    break
                elif skipped:
                    moves[(r,left)]=last+skipped
                else:
                    moves[(r,left)]=last
                
                if last:
                    if last[0] in skipped:
                         break
                    if step==-1:
                        row=max(r-3,0)
                    else:
                        row=min(r+3,ROWS)

                    moves.update(self._traverse_left(r+step,row,step,color,left-1,skipped=last)) 
                    moves.update(self._traverse_right(r+step,row,step,color,left+1,skipped=last))
                break
            elif current.color==color:
                break
            else:
                last=[current]


            left-=1
        return moves

    def _traverse_right(self,start,stop,step,color,right,skipped=[]):
        moves={}
        last=[]
        for r in range(start,stop,step):
            if right>=COLS:
                break
            current=self.board[r][right]
            if current==0:
                if skipped and not last:
                    break
                elif skipped:
                    moves[(r,right)]=last+skipped
                else:
                    moves[(r,right)]=last
                
                if last:
                    if last[0] in skipped:
                        break
                    if step==-1:
                        row=max(r-3,0)
                    else:
                        row=min(r+3,ROWS)

                    moves.update(self._traverse_left(r+step,row,step,color,right-1,skipped=last)) 
                    moves.update(self._traverse_right(r+step,row,step,color,right+1,skipped=last))
                break
            elif current.color==color:
                break
            else:
                last=[current]


            right+=1
        return moves

        
        
                