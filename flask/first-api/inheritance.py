from typing_extensions import Self
from unicodedata import name

from numpy import double


class Person():
    def_init_(self,name,dob)->None:
    Self.name=name
    Self.dob=dob 

    def greet(self):
        print()

    class Engineer(Person):
       def_init_(self,name,dob,country)->None:
       Person._init_(self,name,dob)cd 
       Self.country=country
    def start(self):
        print(f"{self.name}")