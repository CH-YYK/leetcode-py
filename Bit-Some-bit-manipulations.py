## get bit
def getbit(num, i):
    """
    get bit at ith position to the last
    """
    return num & (1 << i) != 0


def setbit(num, i):
    """
    set bit at ith position to the last as 1
    """
    return num | (1 << i)


def clearbit(num, i):
    """
    clear the bit at ith position to the last
    """
    mask = ~(1 << i)
    return num & mask


def clearbitsMSBthroughI(num, i):
    """
    clear all bits through i [i to end]
    """
    mask = (1 << i) - 1
    return num & mask


def clearbitsIthrough0(num, i):
    mask = (-1 << (i+1))
    return num & mask


def updateBit(num, i, bitIs1):
    value = 1 if bitIs1 else 0
    mask = ~(1 << i)
    return (num & mask) | (value << i)
