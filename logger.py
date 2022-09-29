f = lambda color: lambda string: print(color + string + "\33[0m")

black = f("\33[30m")
red = f("\33[31m")
green = f("\33[32m")
yellow = f("\33[33m")
blue = f("\33[34m")
megenta = f("\33[35m")
cyan = f("\33[36m")
white = f("\33[37m")

def log(type, msg):
    if type == 'action':
        blue(msg)
    elif type == 'success':
        green(msg)
    elif type == 'failed':
        red(msg)
    else:
        cyan(msg)