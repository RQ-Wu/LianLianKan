import numpy as np


def XRoadConnect(data, x1, y1, x2, y2):
    """
    Function to judge if two points are connect in X axis
    :param data:game map data
    :param x1: X position of first point
    :param y1: Y position of first point
    :param x2: X position of second point
    :param y2: X position of second point
    :return: boolean
    """
    flag = True
    if not y1 == y2:
        return False
    x_start = min(x1, x2)
    x_end = max(x1, x2)
    for i in range(x_start + 1, x_end):
        if not data[y1][i] == 0:
            flag = False
            break
    return flag


def YRoadConnect(data, x1, y1, x2, y2):
    """
    Function to judge if two points are connect in Y axis
    :param data: game map data
    :param x1: X position of first point
    :param y1: Y position of first point
    :param x2: X position of second point
    :param y2: X position of second point
    :return: boolean
    """
    flag = True
    if not x1 == x2:
        return False
    y_start = min(y1, y2)
    y_end = max(y1, y2)
    for i in range(y_start + 1, y_end):
        if not data[i][x1] == 0:
            flag = False
            break
    return flag


def oneRoadConnect(data, x1, y1, x2, y2):
    """
    Function to judge if two points are connect in one road
    :param data: game map data
    :param x1: X position of first point
    :param y1: Y position of first point
    :param x2: X position of second point
    :param y2: X position of second point
    :return: boolean
    """
    flag = XRoadConnect(data, x1, y1, x2, y2) or YRoadConnect(data, x1, y1, x2, y2)
    if not data[y1][x1] == data[y2][x2]:
        flag = False
    if data[y1][x1] == 0 and data[y2][x2] == 0:
        flag = False
    if flag:
        data[y1][x1] = data[y2][x2] = 0
        print(data)
        print(1)
    return flag, [[x1, y1], [x2, y2]]


def twoRoadConnect(data, x1, y1, x2, y2):
    """
    Function to judge if two points are connect in two road
    :param data: game map data
    :param x1: X position of first point
    :param y1: Y position of first point
    :param x2: X position of second point
    :param y2: X position of second point
    :return: boolean
    """
    flag = False
    points = [[x1, y1]]
    if not data[y1][x1] == data[y2][x2]:
        return False, []
    if YRoadConnect(data, x1, y1, x1, y2) and XRoadConnect(data, x2, y2, x1, y2) and data[y2][x1] == 0:
        flag = True
        points.append([x1, y2])
    elif XRoadConnect(data, x1, y1, x2, y1) and YRoadConnect(data, x2, y2, x2, y1) and data[y1][x2] == 0:
        flag = True
        points.append([x2, y1])
    if flag:
        data[y1][x1] = data[y2][x2] = 0
        points.append([x2, y2])
    print(data)
    print(2)
    return flag, points


def threeRoadConnect(data, x1, y1, x2, y2):
    """
    Function to judge if two points are connect in three road
    :param data: game map data
    :param x1: X position of first point
    :param y1: Y position of first point
    :param x2: X position of second point
    :param y2: X position of second point
    :return: boolean
    """
    temp_data = np.pad(data, (1, 1), 'constant', constant_values=0)
    # init
    points = [[x1, y1]]
    flagX = False
    flagY = False
    if not data[y1][x1] == data[y2][x2]:
        return False, []
    # Two lines parallel to the X-AXIS
    posX = 0
    for i in range(0, 18):
        if temp_data[y1 + 1][i] == 0 and temp_data[y2 + 1][i] == 0:
            if XRoadConnect(temp_data, i, y1 + 1, x1 + 1, y1 + 1) \
                    and XRoadConnect(temp_data, i, y2 + 1, x2 + 1, y2 + 1) \
                    and YRoadConnect(temp_data, i, y1 + 1, i, y2 + 1):
                flagX = True
                posX = i - 1
    if flagX:
        points.append([posX, y1])
        points.append([posX, y2])

    # Two lines parallel to the Y-AXIS
    posY = 0
    for i in range(0, 10):
        if temp_data[i][x1 + 1] == 0 and temp_data[i][x2 + 1] == 0:
            if YRoadConnect(temp_data, x1 + 1, i, x1 + 1, y1 + 1) \
                    and YRoadConnect(temp_data, x2 + 1, i, x2 + 1, y2 + 1) \
                    and XRoadConnect(temp_data, x1 + 1, i, x2 + 1, i):
                flagY = True
                posY = i - 1
    if flagY and flagX == False:
        points.append([x1, posY])
        points.append([x2, posY])

    if flagX or flagY:
        data[y1][x1] = data[y2][x2] = 0
        points.append([x2, y2])
        print(data)
        print(3)
    return flagX or flagY, points


def connect(data, x1, y1, x2, y2):
    """
    Function to judge if two points are connect
    :param data: game map data
    :param x1: X position of first point
    :param y1: Y position of first point
    :param x2: X position of second point
    :param y2: X position of second point
    :return: boolean
    """
    flag1, points1 = oneRoadConnect(data, x1, y1, x2, y2)
    if flag1:
        return flag1, points1
    flag2, points2 = twoRoadConnect(data, x1, y1, x2, y2)
    if flag2:
        return flag2, points2
    flag3, points3 = threeRoadConnect(data, x1, y1, x2, y2)
    if flag3:
        return flag3, points3
    return False, []
