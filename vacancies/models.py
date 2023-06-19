from django.db import models


class Specialty(models.Model):
    code = models.CharField(max_length=20) # Предпологается, что code уникален, можно добавить unique=True
                                           # Тогда Django и база данных будут следить за тем, что значения поля уникальные
                                           # Или даже сделать это поле primary_key
                                           # Подробнее https://django.fun/ru/docs/django/4.1/ref/models/fields/#unique
    title = models.CharField(max_length=20)
    picture = models.URLField(default='https://place-hold.it/100x60')


class Company(models.Model):
    id = models.IntegerField(primary_key=True) # Если id имеет тип int, можно явно не указывать id, 
                                               # в этом случае будет использовано PrimaryKeyField по умолчанию 
                                               # Подробнее тут https://django.fun/ru/docs/django/4.1/topics/db/models/#automatic-primary-key-fields
    title = models.CharField(max_length=20)
    location = models.CharField(max_length=20)
    logo = models.URLField(default='https://place-hold.it/100x60')
    description = models.TextField()
    employee_count = models.IntegerField()


class Vacancy(models.Model):
    id = models.IntegerField(primary_key=True)
    title = models.CharField(max_length=50)
    specialty = models.ForeignKey(Specialty, on_delete=models.CASCADE, related_name="vacancies")
    company = models.ForeignKey(Company, on_delete=models.CASCADE, related_name="vacancies")
    skills = models.TextField()
    description = models.TextField()
    salary_min = models.IntegerField()
    salary_max = models.IntegerField()
    posted = models.DateField()






