from django.db import models


class Products(models.Model):
    title = models.CharField(default='', max_length=70)
    price = models.IntegerField(default=0)
    description = models.TextField(default='')

    class Meta:
        db_table = 'Products'
