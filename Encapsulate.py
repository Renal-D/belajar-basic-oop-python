# getter and setter (get = mengambil var and set = menset var)

class Hero:
    
    def __init__(self, name, role, health):
        self.__name = name
        self.__role = role
        self.__health = health
        
    def getName(self):
        return self.__name
    
    def getHealth(self):
        return self.__health
    
    def diserang(self, damage):
        self.__health -= damage
        

# Game Begin
Seraphine = Hero("Seraphine", 300, 200)

print(Seraphine.__dict__)

# In Game
# Seraphine.__name = "Valentine"
# print(Seraphine.__dict__)        NOTEE = TIDAKKK BOLEEHH DILAKUKANN, Bisa pake Getter
print(Seraphine.getName())
print(Seraphine.getHealth())
Seraphine.diserang(50)
print(Seraphine.getHealth())


# Intinya encapsulasi menjaga variable agar tidak dirubah