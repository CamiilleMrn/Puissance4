from initGame import *

contentCase = ("X","O",".")

def emptyGrid(gridGame):
    for i in range(nb_lines):
        for j in range(nb_columns):
            gridGame.grid[i][j] = 0

def gridCase(color):
    return contentCase(color)

def grid(inGame):
    for i in range(nb_lines,0,-1) : 
        print(i,end=" ")
        for j in range(1,nb_columns+1) :
            print(contentCase(inGame.grille[i][j]),end=" ")
        print(i)


