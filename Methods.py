class Hero:
    jumlah_hero = 0
    
    def __init__(self, name, role, power, health):
        # instance variables
        self.name = name
        self.role = role
        self.power = power
        self.health = health
        Hero.jumlah_hero += 1
    
    #void methods    
    def siapa(self):
        print(f'Saya adalah {self.name} role {self.role}')
        
    # methods tanpa argument
    def healthUp(self,up):
        self.health += up
        
    def getHealth(self):
        return self.health    
    
hero1 = Hero('Serra', 'Mage', 5000,100)
hero2 = Hero('Sora', 'Fighter', 2000,2000)

hero1.siapa()
hero1.healthUp(50)

print(hero1.getHealth())    