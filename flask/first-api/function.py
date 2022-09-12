from ast import Delete
from typing_extensions import Self
from unicodedata import name


class Person():
    array =[]
    def __init__(self,name,id) ->None:
       Self.name=name
       Self.id=id

    def __str__(self) -> str: