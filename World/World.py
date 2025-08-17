class World:
    def __init__(self,width,height):
        self.map=[[None for i in range(width)] for j in range(height)]
        self.entities=[]
