import abc
from abc import ABC
 
class Animal(ABC):
    

    @abc.abstractmethod
    def set_name(self, name):
        pass
    
    @abc.abstractmethod
    def get_name(self):
        pass

    @abc.abstractproperty
    def set_color(self, color):
        pass
    
    @abc.abstractproperty
    def get_color(self):
        pass


class Perro(Animal):

    def set_name(self, name):

        self.__name = name
    
    def get_name(self):

        return self.__name
    
    
    def set_color(self, color):
        self.__color = color
    
    
    def get_color(self):
        return self.__color
 
pet = Perro()
pet.set_name("Pluto")
print(pet.get_name())

pet.set_color("cafe")
print(pet.get_color())