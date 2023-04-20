def request():
    temperature = input('Enter temperature')
    print(determine(temperature))
    return temperature


def determine (temperature):
    if (float(temperature)<30):
        return 'Cold'
    elif(float(temperature)<40):
        return 'Warm'
    elif(float(temperature)>40):
        return 'Hot'



request()
