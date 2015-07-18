from django.db import models

# Create your models here.
class Length(models.Model):
    length_of_room = models.IntegerField(null=True, blank=True)
    number = models.CharField(max_length=10, null=True, blank=True)

    def __str__(self):
        return self.number


class Width(models.Model):
    width_of_room = models.IntegerField(null=True, blank=True)
    number = models.CharField(max_length=10, null=True, blank=True)

    def __str__(self):
        return self.number


