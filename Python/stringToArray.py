
def StringToFloatArray(data):
    arr = data.split(',')
    for i in range(0, len(arr), 1):
        arr[i] = float(arr[i])
    return arr

def StringToIntArray(data):
    arr = data.split(',')
    for i in range(0, len(arr), 1):
        arr[i] = int(arr[i])
    return arr