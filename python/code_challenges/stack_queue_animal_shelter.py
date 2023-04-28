from data_structures.queue import Queue


class AnimalShelter:
    """
    solution with assistance from ChatGPT
    """
    def __init__(self):
        self.dogs = []
        self.cats = []

    def enqueue(self, animal):
        if isinstance(animal, Dog):
            self.dogs.append(animal)
        elif isinstance(animal, Cat):
            self.cats.append(animal)

    def dequeue(self, pref):
        if pref == 'dog':
            if self.dogs:
                return self.dogs.pop(0)
            else:
                return None
        elif pref == 'cat':
            if self.cats:
                return self.cats.pop(0)
            else:
                return None
        else:
            return None


class Dog:
    def __init__(self):
        self.type = 'dog'
        self.name = ''


class Cat:
    def __init__(self):
        self.type = 'cat'
        self.name = ''
