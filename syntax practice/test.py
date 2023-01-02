def add_binary(a,b):
    sum = a+b
    return print(bin(sum)[3:])


def add_binary2(x,y):
    return print(format(x+y, 'b'))

add_binary2(2,105)