# Измените класс Person так, чтобы его методы 
# оперировали внутренним состоянием, 
# а не использовали цепочку вызовов объектов

class Room:
    def get_name(self):
        return 42


class Street:
    def get_room(self) -> Room:
        return Room()


class City:
    def get_street(self) -> Street:
        return Street()

    def population(self):
        return 100500


class Country:
    def get_city(self) -> City:
        return City()


class Planet:
    def get_contry(self) -> Country:
        return Country()


class Person:
    def __init__(self, room, population):
        self.room = room
        self.population = population

    def get_person_room(self):
        return self.room

    def get_city_population(self):
        return self.population


# TODO после выполнения задания попробуйте
# сделать экземпляр класса person и вызвать новые методы.

person_1 = Person(40, 1000)
person_2 = Person(400, 31000)

print(person_1.get_person_room())
print(person_1.get_city_population())
print(person_2.get_person_room())
print(person_2.get_city_population())
