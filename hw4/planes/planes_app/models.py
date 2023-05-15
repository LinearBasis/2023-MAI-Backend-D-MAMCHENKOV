from django.db import models

class Company(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=250,null=False)
    
    def __str__(self):
        return self.name

class Trip(models.Model):
    id = models.AutoField(primary_key=True)
    company = models.ForeignKey(Company, on_delete=models.deletion.CASCADE, null=False)
    plane = models.CharField(max_length=250,null=False)
    town_from = models.CharField(max_length=250,null=False)
    town_to = models.CharField(max_length=250,null=False)
    time_in = models.DateTimeField(null=False)
    time_out = models.DateTimeField(null=False)

    # Метод __str__ для возвращения строкового представления объекта
    def __str__(self):
        return f"{self.company} : {self.town_from} - {self.town_to} : {self.id}"
    
class Passenger(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=250,null=False)
    
    def __str__(self):
        return self.name

class Pass_in_trip(models.Model):
    id = models.AutoField(primary_key=True)
    trip = models.ForeignKey(Trip, on_delete=models.deletion.CASCADE)
    passenger = models.ForeignKey(Passenger, on_delete=models.deletion.CASCADE)
    place = models.CharField(max_length=250,null=False)

    def __str__(self):
        return f'{self.trip} - {self.passenger} : {self.place}'
