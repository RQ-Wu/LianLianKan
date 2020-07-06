import numpy as np
from collections import Counter
from LLKGame.connect import *

class GameMap:
    def __init__(self):
        self.data = np.random.randint(1, 8, [8, 16])
        flag = True
        while flag:
            flag = False
            for i in range(1, 8):
                if not Counter(self.data.flatten())[i] % 2 == 0:
                    self.data = np.random.randint(1, 8, [8, 16])
                    flag = True
            if not flag:
                break
        '''self.data = np.array([[1,1,2,0,0,2],
                     [2,3,3,4,0,1],
                     [3,5,2,2,0,2]])'''

    def getData(self):
        return self.data


if __name__ == '__main__':
    gameData = GameMap()
    print(gameData.getData())
    print()
    threeRoadConnect(gameData.getData(),2,0,3,2)
    threeRoadConnect(gameData.getData(), 5, 0, 5, 2)
