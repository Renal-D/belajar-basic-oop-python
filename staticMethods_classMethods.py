class Hero: 
    #  private class variable
    __jumlah = 0
    
    def __init__(self, name):
        self.__name = name
        Hero.__jumlah += 1
    
    def getJumlah(self): #khusus object
        return Hero.__jumlah
    
    def getJumlah1(): # khusus class
        return Hero.__jumlah
    
    # static methods (decorators)
    @staticmethod
    def getJumlah2():
        return Hero.__jumlah
    
    # class methods -- polymorpism
    @classmethod
    def getJumlah3(cls):
        return cls.__jumlah

Tifany = Hero('Tifany')
print(Hero.getJumlah1())        
carmine = Hero('Carmine')
print(Hero.getJumlah2())
virgo = Hero('Virgo')
print(virgo.getJumlah3())
