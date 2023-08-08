"""
This module contains class definition of Animal and its types, along with the factory method
to return appropriate object based on given type
"""

from abc import ABC, abstractmethod


class Animal(ABC):

    def video(self, name, video_path):
        self.name = name
        self.video_path = video_path


    @abstractmethod
    def speak(self):
        pass

class Dog(Animal):

    def video(self, name):
        super().video(name)
        self.video_path = '../tmp/doggie1.mp4'

    def speak(self):
        return "Woof!"


class Cat(Animal):

    def video(self, name):
        super().video(name)
        self.video_path = '../tmp/cat1.mp4'

    def speak(self):
        return "Meow!"


def animal_factory(pet_type: str = None) -> [Animal, None]:
    """
    Returns animal instance of appropriate class based on given type
    :param pet_type: type of pet (cat or dog)
    :return: Animal object based on given type or None:
    """
    animal_types = {
        'dog': Dog,
        'cat': Cat,
    }
    if pet_type and pet_type.lower() in animal_types:
        return animal_types[pet_type.lower()]()

    return None
