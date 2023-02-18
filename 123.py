class Person:
    def __init__(self, name, age, job):
self.name = name
self.age = age
self.job = job

def get_name(self):
return self.name

def set_name(self, name):
self.name = name

def get_age(self):
return self.age

def set_age(self, age):
self.age = age

def get_job(self):
return self.job

def set_job(self, job):
self.job = job


class Person: # класс с полной инкапсуляцией через @property

def __init__(self, name, age, job): # инициализация атрибутов экземпляра класса
self._name = name # _ - для отметки "внутренности" (доступ к атрибуту через @property)
self._age = age # _ - для отметки "внутренности" (доступ к атрибуту через @property)
self._job = job # _ - для отметки "внутренности" (доступ к атрибу