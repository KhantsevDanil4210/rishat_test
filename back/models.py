from django.db import models

class Item(models.Model):
    name = models.CharField(max_length=30, verbose_name='name')
    description = models.CharField(max_length=30, verbose_name='description')
    price = models.IntegerField()

    def __str__(self):
        return str(self.name)
