class Car(object):
    def __init__(self,model,color,company,speedLimit):
        self.model=model
        self.color=color
        self.company=company
        self.speedLimit=speedLimit

    def start(self):
        print('started')

    def stop(self):
        print('stopped')
    
    def accelarate(self):
        print('accelarating')
    
    def changeGear(self,gear):
        print('Gear changed to ',gear)
    
Audi=Car('A6','Green','audi',200)
print(Audi.color)
Audi.start()
Audi.stop()
Audi.accelarate()
Audi.changeGear(3)