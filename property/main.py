class Car():
    def __init__(self, model=None):
        self.model = model
        
class AdvancedCar(Car):
    def __init__(self, model='SUV', enable_auto_run=False):
        super().__init__(model)
        self.enable_auto_run = enable_auto_run

advanced_car = AdvancedCar('SUV')
advanced_car.enable_auto_run = True
print(advanced_car.enable_auto_run)

class Car():
    def __init__(self, model=None):
         self.model = model
       
class AdvancedCar(Car):
    def __init__(self, model='SUV', enable_auto_run=False):
         super().__init__(model)
         self._enable_auto_run = enable_auto_run
    
    @property
    def enable_auto_run(self):
        return self._enable_auto_run

advanced_car = AdvancedCar('SUV')
print(advanced_car.enable_auto_run)

class AdvancedCar(Car):
    def __init__(self, model='SUV',
                 enable_auto_run=False,
                 passwd='123'):
        super().__init__(model)
        self._enable_auto_run = enable_auto_run
        self.passwd = passwd
        
    @property
    def enable_auto_run(self):
        return self._enable_auto_run
    
    @enable_auto_run.setter
    def enable_auto_run(self, is_enable):
        if self.passwd == '456':
            self._enable_auto_run = is_enable
        else:
            raise ValueError
        
advanced_car = AdvancedCar('SUV', passwd='456')
advanced_car.enable_auto_run = True
print(advanced_car.enable_auto_run)

class Car():
    def __init__(self, model=None):
        self.model = model
        
class AdvancedCar(Car):
    def __init__(self, model='SUV', enable_auto_run=False):
        super().__init__(model)
        self.__enable_auto_run = enable_auto_run
        
    @property
    def enable_auto_run(self):
        return self.__enable_auto_run
    
    def run(self):
        print(self.__enable_auto_run)
        print('super fast')
        
advanced_car = AdvancedCar('SUV')
advanced_car.run()