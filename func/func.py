def say_something():
    s = "Hello!"
    return s

f = say_something
print(f())

def what_is_this(color):
    if color == 'red':
        return "tomato"
    elif color == "green":
        return "green pepper"
    else:
        return "I don't know"
    
print(what_is_this("green"))

def menu(entree, drink, dessert):
    print("entree = ", entree)
    print("drink = ", drink)
    print("dessert = ", dessert)
    
menu("beef", "beer", "ice")

def sample_func(x, l=[]):
    l.append(x)
    return l

y = [1, 2, 3]
r = sample_func(100, y)
print(r)

y = [1, 2, 3]
r = sample_func(200, y)
print(r)

def sample_func(x, l=None):
    if l is None:
        l = []
    l.append(x)
    return l

r = sample_func(100)
print(r)

r = sample_func(100)
print(r)

def say_something(*args):
    print(args)
        
say_something("Hello", "ken", "jun")

def say_something(*args):
    for args in args:
        print(args)
    
say_something("Hi!", "Mike", "Nancy")

def menu(entree="beef", drink="wine"):
    print(entree, drink)
    
menu(entree="beef")

def say_something(word, *args):
    print('word =', word)
    for arg in args:
        print(arg)
        
t = ('Mike', 'Nancy')
say_something('Hi!!', *t)

def menu(entree='beef', drink='wine'):
    print(entree, drink)
    
menu(entree='beef', drink='coffee')

def menu(**kwargs):
    print(kwargs)
    
menu(entree='beef', drink='coffee')

def menu(**kwargs):
    for k, v in kwargs.items():
        print(k, v)
        
menu(entree='beef', drink='coffee')

def menu(**kwargs):
    for k, v in kwargs.items():
        print(k, v)
        
d = {
    'entree': 'beef',
    'drink': 'ice coffee',
    'dessert': 'ice'
}
menu(**d)

def menu(food, *args, **kwargs):
    print(food)
    print(args)
    print(kwargs)
    
menu('sisitou', 'apple', 'orange', entree='beef', drink='coffee')

def outer(a, b):
    
    def plus(c, d):
        return c + d
    
    r = plus(a, b)
    print(r)
    
outer(1, 2)

def outer(a, b):
    def inner():
        return a + b
    return inner

f = outer(1, 2)
r = f()
print(r)

def circle_area_func(pi):
    def circle_area(radius):
        return pi * radius * radius
    return circle_area

ca1 = circle_area_func(3.14)
ca2 = circle_area_func(3.14159)
print(ca1(10))
print(ca2(10))

def add_num(a, b):
    return a + b

print('start')
r = add_num(10, 20)
print('end')

print(r)

def print_info(func):
    def wrapper(*args, **kwargs):
        print('start')
        result = func(*args, **kwargs)
        print('end')
        return result
    return wrapper

def add_num(a, b):
    return a + b

f = print_info(add_num)
r = f(10, 20)
print(r)

def print_info(func):
    def wrapper(*args, **kwargs):
        print('start')
        result = func(*args, **kwargs)
        print('end')
        return result
    return wrapper

@print_info
def add_num(a, b):
    return a + b
r = add_num(10, 20)
print(r)

def print_more(func):
    def wrapper(*args, **kwargs):
        print('func:', func.__name__)
        print('args:', args)
        print('kwargs', kwargs)
        result = func(*args, **kwargs)
        print('result:', result)
        return result
    return wrapper

@print_more
def add_num(a, b):
    return a + b

r = add_num(10, 20)
print(r)

def print_more(func):
    def wrapper(*args, **kwargs):
        print('func:', func.__name__)
        print('args:', args)
        print('kwargs', 'kwargs')
        result = func(*args, **kwargs)
        print('result:', result)
        return result
    return wrapper

def print_info(func):
    def wrapper(*args, **kwargds):
        print('start')
        result = func(*args, **kwargds)
        print('end')
        return result
    return wrapper

@print_info
@print_more
def add_num(a, b):
    return a + b

r = add_num(10, 20)
print(r)

@print_more
@print_info
def add_num(a, b):
    return a + b

r = add_num(10, 20)
print(r)