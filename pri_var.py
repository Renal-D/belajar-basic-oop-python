class Hero:
    #class variables
    jumlah = 0
    __privateJumlah = 0
    
    def __init__(self, name, power):
        self.name = name
        self.power = power
        
        # instance variable private
        self.__private = "private"
        
        #instance variable protected
        self._protected = "protected"
        
Serra = Hero('Serra', 500)

print(Serra.__dict__)
print(Serra._protected)
Serra._protected = "testing"
print(Serra.__dict__)
# print(Serra.__private)
print(Serra._protected)

print(Hero.__dict__)
print(Hero.jumlah)
print(Hero.__privateJumlah)