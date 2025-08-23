#start of the main game loop
from Utils.Display import display

print("Welcome to dungeon crawler ! "
      "\nYou have been trapped deep within a dungeon while exploring !,"
      " \ncomplete the given mission and escape !")

def main():
    Obj=display(12,12,40)
    display.createworld(Obj)

main()