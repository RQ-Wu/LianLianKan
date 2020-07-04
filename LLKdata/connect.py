import numpy as np

def XRoadConnect(data, x1, y1, x2, y2):
    """
    判断x轴上是否连通
    :param data:
    :param x1: 第一个点的x轴坐标
    :param y1: 第一个点的y轴坐标
    :param x2: 第二个点的x轴坐标
    :param y2: 第二个点的y坐标
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
    判断y轴上是否连通
    :param data:
    :param x1: 第一个点的x轴坐标
    :param y1: 第一个点的y轴坐标
    :param x2: 第二个点的x轴坐标
    :param y2: 第二个点的y坐标
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
    判断是否能直线相连
    :param data:
    :param x1: 第一个点的x轴坐标
    :param y1: 第一个点的y轴坐标
    :param x2: 第二个点的x轴坐标
    :param y2: 第二个点的y坐标
    :return: boolean
    """
    flag = XRoadConnect(data,x1, y1, x2, y2) or YRoadConnect(data,x1, y1, x2, y2)
    if not data[y1][x1] == data[y2][x2]:
        flag = False
    if data[y1][x1] == 0 and data[y2][x2] == 0:
        flag = False
    if flag:
        data[y1][x1] = data[y2][x2] = 0
        print(data)
        print(1)
    return flag


def twoRoadConnect(data, x1, y1, x2, y2):
    flag = False
    if not data[y1][x1] == data[y2][x2]:
        return False
    if YRoadConnect(data, x1, y1, x1, y2) and XRoadConnect(data, x2, y2, x1, y2) and data[y2][x1] == 0:
        flag = True
    if XRoadConnect(data, x1, y1, x2, y1) and YRoadConnect(data, x2, y2, x2, y1) and data[y1][x2] == 0:
        flag = True
    if flag:
        data[y1][x1] = data[y2][x2] = 0
    print(data)
    print(2)
    return flag


def threeRoadConnect(data, x1, y1, x2, y2):
    temp_data = np.pad(data, (1, 1), 'constant', constant_values=0)
    flag = False
    if not data[y1][x1] == data[y2][x2]:
        return False
    # 两条与x轴平行
    for i in range(0, 18):
        if temp_data[y1][i] == 0 and temp_data[y2][i] == 0:
            if XRoadConnect(temp_data,i,y1+1,x1+1,y1+1) and XRoadConnect(temp_data,i,y2+1,x2+1,y2+1) and YRoadConnect(
                    temp_data,i,y1+1,i,y2+1):
                flag = True

    # 两条与y轴平行
    for i in range(0, 10):
        if temp_data[i][x1+1] == 0 and temp_data[i][x2+1] == 0:
            if YRoadConnect(temp_data, x1+1, i, x1+1, y1+1) and YRoadConnect(temp_data, x2+1, i, x2+1, y2+1) and XRoadConnect(
                    temp_data, x1+1, i, x2+1, i):
                flag = True
    if flag:
        data[y1][x1] = data[y2][x2] = 0
        print(data)
        print(3)
    return flag

def connect(data, x1, y1, x2, y2):
    return oneRoadConnect(data, x1, y1, x2, y2) or \
           twoRoadConnect(data, x1, y1, x2, y2) or \
           threeRoadConnect(data, x1, y1, x2, y2)