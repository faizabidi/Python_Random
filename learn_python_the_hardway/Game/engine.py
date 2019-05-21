import house


# The driving engine to keep the game playing till either the player wins
# or loses the game.
class Engine(object):
    # This init function takes an instance of the Map class as a parameter
    def __init__(self, mapInstance):
        self.mapInstance = mapInstance
        print(type(mapInstance))

    # Play the game starting with this mapInstance
    def play(self):
        currentHouse = self.mapInstance.startHouse()
        lastHouse = self.mapInstance.nextHouse('GameWon')

        # Keep playing till the user wins the game of answers it wrong
        while currentHouse != lastHouse:
            # "nextHouse" is the name of the house to visit next
            nextHouse = currentHouse.enter()
            currentHouse = self.mapInstance.nextHouse(nextHouse)

        # Enter the last house
        currentHouse.enter()
