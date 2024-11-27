from .animal import Animal
from .animal_exotico import Animal_Exotico

class Gato(Animal):
    def __init__(self, nombre:str, raza:str, edad:int, peso:float) -> None:
        super().__init__(nombre,edad,peso)
        self.raza = raza
        
        

    @staticmethod
    def hacer_sonido() -> str:
        return "miau,miau,miau"


    
    @property
    def raza(self) -> str:
        """ Devuelve el valor del atributo privado 'raza' """
        return self.__raza
    
    @raza.setter
    def raza(self, value:str) -> None:
        """ 
        Establece un nuevo valor para el atributo privado 'raza'
    
        Valida que el valor enviado corresponda al tipo de dato del atributo
        """ 
        if isinstance(value, str):
            self.__raza = value
        else:
            raise ValueError('Expected str')
        
        
