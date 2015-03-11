from hero import *
from wumpus import *

def main():
    print("\n\n\n")
    hero = Hero('Hero')
    wumpus = Wumpus(hero.getposition())
    while hero.getposition() != wumpus.getposition():
        print(hero)
        print(wumpus)
        wumpus.hunt()
    print(hero)
    print(wumpus)

if __name__ == "__main__":
    main()
