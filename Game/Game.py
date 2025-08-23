class Game:
    def __init__(self):
        self.player=None
        self.npc=[]

    def move(self, direction):
        if direction.lower() == "w":
            self.y -= 1
        elif direction.lower() == "s":
            self.y += 1
        elif direction.lower() == "a":
            self.x -= 1
        elif direction.lower() == "d":
            self.x+=1
    def interact(self):
        self.npc.append(self.player)
    def attack(self):
        self.npc.append(self.player)
    def heal(self):
        self.npc.append(self.player)

