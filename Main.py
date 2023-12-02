# class Hero:  #template 
#     pass


# hero1 = Hero() #object
# hero2 = Hero()
# hero3 = Hero()

# hero1.name = 'Serra'
# hero1.role = 'Mage'
# hero1.power = 500

# hero2.name = 'Renna'
# hero2.role = 'Marksman'
# hero2.power = 400

# hero3.name = 'Sora'
# hero3.role = 'Fighter'
# hero3.power = 600

# print(hero1)
# print(hero1.__dict__)
# print(hero1.name)

class Hero:
    
    def __init__(self):
        print('Start')
        
hero1 = Hero()