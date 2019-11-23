#EXAMPLES OF USER DEFINED OBJECTS

class Daughter():

    #GENERAL ATTRIBUTE
    gender = 'female'

    #SPECIFIED ATTRIBUTES
    def __init__(self,name,species,age):
        self.name = name
        self.species = species
        self.age = age

    #PRINTING METHOD
    def __str__(self):
        return 'Name: {}, Species: {}, Age: {}, Gender: {}'.format(self.name, self.species, self.age, self.gender)


Kleio = Daughter(name='Kleio',species='human',age=0)
Kheera = Daughter(name='Kheera',species='cat',age=2)

print(Kleio.name)
print(Kheera.species)
print(Kleio.age,Kheera.gender)
print(Kleio)
print(Kheera)