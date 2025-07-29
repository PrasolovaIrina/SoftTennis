from django.db import models

class Player(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    birth_date = models.DateField()
    country = models.CharField(max_length=100)
    photo = models.ImageField(upload_to='player_photos/', blank=True, null=True)
    rank = models.IntegerField(blank=True, null=True)

    def __str__(self):
        return f'{self.first_name} {self.last_name}'