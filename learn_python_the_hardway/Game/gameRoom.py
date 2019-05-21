import engine
import house


class Map(object):
    def __init__(self, houseName):
        self.houseName = houseName
        print(f"From Map class: {houseName}")

    # Create a dictionary mapping
    houses = {
        'Targaryen': house.Targaryen(),
        'Lannister': house.Lannister(),
        'Stark': house.Stark(),
        'Baratheon': house.Baratheon(),
        'Tyrell': house.Tyrell(),
        'GameWon': house.GameWon(),
        'GameOver': house.GameOver()
    }

    # Get the next house to visit
    # "val" is basically returning a class
    def nextHouse(self, houseName):
        val = Map.houses.get(houseName)
        return val

    # This house is where we start the game
    def startHouse(self):
        return self.nextHouse(self.houseName)


def main():
    # Start with House Targaryen and get an instance of Map class
    mapInstance = Map('Targaryen')
    engineInstance = engine.Engine(mapInstance)
    engineInstance.play()


if __name__ == '__main__':
    main()
