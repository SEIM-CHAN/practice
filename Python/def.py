from unittest import result


def say_something():
    s = 'hi'
    return s


result = say_something()
print(result)


def what_is_this(color):
    if color == 'red':
        return 'tomato'
    elif color == 'green':
        return 'green pepper'
    else:
        return "I don't know"


result = what_is_this('green')
print(result)


# num: int = 10

def add_num(a: int, b: int) -> int:
    return a + b


r = add_num(10, 20)
print(r)
