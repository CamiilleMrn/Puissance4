nb_lines = int(6)
nb_columns = int(7)
red , yellow = 1 , 2

class Player :
    
    def __init__(self, color, name=''):
        self.color = int(color)
        self.name = str(name)

class Game :

    def __init__(self, play1, play2):
        self.grid = []
        for lines in range(nb_lines):
            self.grid.append(list(nb_columns)*[0])
        playerRed = Player(red,play1)
        playerYellow = Player(yellow,play2)
        self.players = (playerRed,playerYellow)





