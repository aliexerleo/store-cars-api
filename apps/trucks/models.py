from django.db import models


class Trucks(models.Model):
    mark = models.CharField(max_length=255)
    model = models.CharField(max_length=255)
    year = models.IntegerField()
    price = models.IntegerField()
    COLOR = (('White', 'BLANCO'), 
             ('Red', 'ROJO'),
             ('Blue', 'AZUL'),
             ('Black', 'NEGRO'),
             ('Green', 'VERDE'),
             ('Yellow', 'AMARILLO'),
             ('Brown', 'MARRON'),
             ('Silver', 'PLATEADO'),
             ('Golden', 'DORADO'),
    )
    color = models.CharField(max_length=50, choices=COLOR, default='White')
    description = models.TextField(blank=True)

    def __str__(self):
        return "{0}, {1}, {2}".format(self.mark, self.color, self.year)