class readQssTool:
    @staticmethod
    def readQss(styleFile):
        """
        Read the qss file content
        :param styleFile: file path
        :return: string(qss file content)
        """
        with open(styleFile,'r') as f:
            return f.read()