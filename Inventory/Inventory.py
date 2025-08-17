class Inventory:
    def __init__(self):
        self.items=[]
    def addItem(self,item):
        if self.items>5:
            return False
        else:
            self.items.append(item)
            return True
    def removeItem(self,item):
        if item in self.items:
            self.items.remove(item)
            return True
        else:
            return False
    def viewInventory(self):
        for item in self.items:
            print("item: ",item)