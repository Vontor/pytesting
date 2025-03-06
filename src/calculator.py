def add(a, b):
    return a + b

def add_wrong(a, b):
    return a + b + 1

def substract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def multiply_wrong(a, b):
    return a*b + 1

def divide(a, b):
    if b == 0:
        raise ValueError("Nemužete dělit nulou!!!")
    else:
        return a / b

