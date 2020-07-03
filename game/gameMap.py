import numpy as np
from collections import Counter

class Map:
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

    def getData(self):
        return self.data


