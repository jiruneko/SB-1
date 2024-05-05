# class Person():
#     def say_hello(self):
#         print("Good morning")

# person = Person()
# person.say_hello()

# class Person():
#     def __init__(self):
#         print('First')
        
# person = Person()

# class Person():
#     def __init__(self, name):
#         self.name = name
#         print(self.name)
        
# person = Person('Mike')

# class Person():
#     def __init__(self, name='Default'):
#         self.name = name
#         print(self.name)
        
# person = Person()

# class Person():
#     def __init__(self, name):
#         self.name = name
#         print(self.name)
    
#     def say_something(self):
#         print('I am {}. Hello'.format(self.name))
        
# person = Person('Mike')
# person.say_something()

# class Person():
#     def __init__(self, name):
#         self.name = name
        
#     def say_something(self):
#         print('I am {}. hello'.format(self.name))
#         self.run(10)
        
#     def run(self, num):
#         print('run' * num)
        
# person = Person('Mike')
# person.say_something()

# class Person():
#     def __init__(self, name):
#         self.name = name

#     def __del__(self):
#         print('good bye')
        
# person = Person("a")
# print('############')

# class car():
#     pass

# class MyCar():
#     pass

# class Car():
#     def run(self):
#         print('run')
        
# class MyCar(Car):
#     pass

# car = Car()
# car.run()
# my_car = MyCar()
# my_car.run()

# class Car():
#     def run(self):
#         print('run')
        
# class AdvancedCar(Car):
#     def auto_run(self):
#         print('auto run')
        
# advanced_car = AdvancedCar()
# advanced_car.run()
# advanced_car.auto_run()

# class Car():
#     def run(self):
#         print('run')
        
# class MyCar(Car):
#     def run(self):
#         print('fast')

# class AdvancedCar(Car):
#     def run(self):
#         print('super fast')
        
# car = Car()
# car.run()
# print('###############')
# my_car = MyCar()
# my_car.run()
# print('###############')
# advanced_car = AdvancedCar()
# advanced_car.run()

# class Car():
#     def __init__(self, model=None):
#         self.model = model

# class MyCar(Car):
#     pass

# class AdvancedCar(Car):
#     pass

# mycar = MyCar('sedan')
# print(mycar.model)
# advanced_car = AdvancedCar('SUV')
# print(advanced_car.model)

# class Car():
#     def __init__(self, model=None):
#         self.model = model
        
# class AdvancedCar(Car):
#     def __init__(self, model='SUV', enable_auto_run=False):
#         super().__init__(model)
#         self.enable_auto_run = enable_auto_run
