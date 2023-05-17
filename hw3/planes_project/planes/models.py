from django.db import models


class Flight(models.Model):
    flight_number = models.CharField(max_length=50)
    departure_city = models.CharField(max_length=100)
    arrival_city = models.CharField(max_length=100)
    departure_date = models.DateField()
    arrival_date = models.DateField()
    passengers = models.ManyToManyField('Passenger', related_name='flights', blank=True)

    def __str__(self):
        return self.flight_number


class Airline(models.Model):
    name = models.CharField(max_length=100)
    established_date = models.DateField()

    def __str__(self):
        return self.name


class Airport(models.Model):
    name = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    country = models.CharField(max_length=100)
    code = models.CharField(max_length=10)

    def __str__(self):
        return self.name


class Passenger(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    gender = models.CharField(max_length=10)
    age = models.IntegerField()

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
