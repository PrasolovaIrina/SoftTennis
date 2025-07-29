from django.db import models

class Tournament(models.Model):
    name = models.CharField(max_length=200)
    location = models.CharField(max_length=200)
    start_date = models.DateField()
    end_date = models.DateField()
    description = models.TextField(blank=True)
    logo = models.ImageField(upload_to='tournament_logos/', blank=True, null=True)

    def __str__(self):
        return self.name