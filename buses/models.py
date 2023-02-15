from django.db import models

class Bus(models.Model):
    bus_name = models.CharField(max_length=100)
    bus_number = models.CharField(max_length=20)

    def __str__(self):
        return self.bus_name

class Route(models.Model):
    route_name = models.CharField(max_length=100,help_text="route name")
    route_number = models.CharField(max_length=20)
    buses = models.ManyToManyField(Bus)

    def __str__(self):
        return self.route_name

class BusRoute(models.Model):
    bus = models.ForeignKey(Bus, on_delete=models.CASCADE)
    route = models.ForeignKey(Route, on_delete=models.CASCADE)
    from_time = models.TimeField()
    to_time = models.TimeField()

    def __str__(self):
        return f'{self.bus} runs on {self.route} from {self.from_time} to {self.to_time}'

