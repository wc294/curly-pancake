class device:
    def __init__(self,given_height,given_width):
        self.height= given_height
        self.width= given_width 
    def power(self):
        print('computer has powered on')
class computer(device):
    def power(self):
        print('power is off')
    def typing(self):
        print('you typed this earlier')
    def colour(self):
        coloured=ibnput('enter a colour')
        print(coloured)
    
