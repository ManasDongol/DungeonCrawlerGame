class Player:
    def __init__(self, playerName):
        self.playerName = playerName
        self.x=0;
        self.y=0;


    def move(self, direction):
        if direction == "north":
            self.y -= 1
        elif direction == "south":
            self.y += 1
        elif direction == "west":
            self.x -= 1
        elif direction == "east":
            self.x += 1

