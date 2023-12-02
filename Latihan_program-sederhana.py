class Hero:
    
    def __init__(self, name, health, attpwr, deffpwr):
        self.name = name
        self.health = health
        self.attpwr = attpwr
        self.deffpwr = deffpwr
        
    def serang(self, opponent):
        print(self.name + " Menyerang " + opponent.name)
        opponent.bertahan(self, self.attpwr)
        
    def bertahan(self, opponent, attpwr_lawan):
        print(self.name + " Bertahan dari serangan " + opponent.name) 
        att_diterima = attpwr_lawan/(self.deffpwr/8)
        self.health -= att_diterima
        print("serangan terkena = " + str(att_diterima) + " dan darah tersisa = " + str(self.health)) 
        
        
Serra = Hero("Serra", 1000, 233, 100)
Sora = Hero("Sora", 950, 200, 220)

Sora.serang(Serra)
print('\n') 
Serra.serang(Sora)
print('\n')   
Serra.serang(Sora)
print('\n') 
Sora.serang(Serra)    