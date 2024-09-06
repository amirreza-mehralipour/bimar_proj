from django.db import models

class Bimar(models.Model):
    name = models.CharField(max_length=255)
    explainations = models.TextField()

    def __str__(self) -> str:
        return self.name
    
class Khedmat(models.Model):
    name = models.CharField(max_length=255)
    price = models.BigIntegerField()

    def __str__(self) -> str:
        return self.name


class Nobat(models.Model):
    bimar = models.ForeignKey(Bimar, on_delete= models.PROTECT)
    date = models.DateTimeField()
    khedmat = models.ForeignKey(Khedmat, on_delete=models.PROTECT)


