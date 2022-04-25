from initGame import *

def IsInGrid(inGame, column) : 
    if column < 1 or column > nb_columns :
        return False
    else :
        return inGame.grid[nb_lines][column] == 0 

def chosenColumn(inGame, column) :
    line = 1
    while inGame.grille[line][column] != 0 :
        line = line + 1
    return line
    
def pawnPlace(ioGame, column, color) :
    ioGame.grid[chosenColumn(ioGame, column)][column] = color

def pawnAligned(inGame, line, column, dirX, dirY) :
    lin = line + dirY 
    col = column + dirX 
    color = inGame.grid[line][column]
    nbPawns = 1

    while inGame.grid[lig][col] == color : 
        nbPions = nbPions + 1
        lig = lig + dirY ; col = col + dirX
        lig = line - dirY ; col = column - dirX
    while inGame.grid[lig][col] == color : 
        nbPions = nbPions + 1
        lig = lig - dirY ; col = col - dirX
    return nbPions