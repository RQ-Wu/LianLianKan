class readQssTool:
    @staticmethod
    def readQss(styleFile):
        with open(styleFile,'r') as f:
            return f.read()