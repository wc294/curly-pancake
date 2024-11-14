class vehicle:
    def __init__(self, given_name, given_speed, given_size):
        self.name= given_name
        self.switch=given_speed
        self.fix= given_size
    def switch_on(self):
        print('switch on')
    def drive(self):
        print('drive')
    def fix(self):
        print('fix')

class car(vehicle):
    def switch_on(self):
        print('switching car on')
    def drive(self):
        func=input('manual or automatic')
        print(func)
    def fix(self):
        print('mot while you wait...')
    def driver(self):
        print('you have a license to drive')

class moto0rbike(vehicle):
    def switch_on(self):
        print('obnoxious revving')
    def drive(self):
        print('vroom vrooom')
    def fix(self):
        print('fixing bike wheel stuff')
    
        