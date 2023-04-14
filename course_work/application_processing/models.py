from django.db import models
from datetime import datetime
from course_work import settings

class Priority(models.Model):
    name = models.CharField(max_length=30)

    def __str__(self) -> str:
        return self.name

class Statuses(models.Model):
    name = models.CharField(max_length=30)

    def __str__(self) -> str:
        return self.name

class Service_objects(models.Model):
    name = models.CharField(max_length=30)

    def __str__(self) -> str:
        return self.name

class Positions(models.Model):
    name = models.CharField(max_length=60)

    def __str__(self) -> str:
        return self.name

class Roles(models.Model):
    name = models.CharField(max_length=30)

    def __str__(self) -> str:
        return self.name

class Clients(models.Model):
    is_company = models.BooleanField()
    name = models.CharField(max_length=30)
    telephone = models.CharField(max_length=30)
    fio = models.CharField(max_length=60)

    def __str__(self) -> str:
        if (self.is_company):
            return self.name
        return self.fio

class Equipment_types(models.Model):
    name = models.CharField(max_length=30)

    def __str__(self) -> str:
        return self.name

class Equipment(models.Model):
    name = models.CharField(max_length=40)
    type = models.ForeignKey(Equipment_types, on_delete=models.SET_NULL, null=True) # если удаляется тип оборудования, то все оборудование связанное с ним остается, но тип у него будет null
    inv_number = models.CharField(max_length=45)

    def __str__(self) -> str:
        return self.name

class Workers(models.Model):
    # id = models.IntegerField()
    fio = models.CharField(max_length=60)
    position = models.ForeignKey(Positions, on_delete=models.SET_DEFAULT, default='Нет должности')
    role = models.ForeignKey(Roles, on_delete=models.SET_DEFAULT, default='Нет роли')

    def __str__(self) -> str:
        return self.fio

    # def __dict__(self) -> dict:
    #     return self.fio
class Applications(models.Model):
    type = models.CharField(max_length=30)
    priority = models.ForeignKey(Priority, on_delete=models.SET_DEFAULT, default='Нет приоритета')
    description = models.CharField(max_length=30)
    files = models.FilePathField()
    client = models.ForeignKey(Clients, on_delete=models.CASCADE)
    service_object = models.ForeignKey(Service_objects, on_delete=models.CASCADE)
    equipment = models.ForeignKey(Equipment, on_delete=models.CASCADE)
    worker = models.ForeignKey(Workers, on_delete=models.SET_DEFAULT, default='Нет работника')
    create_date = models.DateTimeField()
    planned_end_date = models.DateTimeField()
    taken_date = models.DateTimeField(null=True)
    end_date = models.DateTimeField()
    status = models.ForeignKey(Statuses, on_delete=models.SET_DEFAULT, default='Создано')

    def __init__(self, **kwargs):
        now = datetime.now()
        dt_string = now.strftime("%d/%m/%Y %H:%M:%S")
        self.create_date = dt_string
        self.planned_end_date = 12
        super().__init__(**kwargs)

