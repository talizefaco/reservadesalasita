from django.db import models

# Create your models here.

class salaCasd(models.Model):
	comecoReserva = models.CharField(max_length=64)
	terminoReserva = models.CharField(max_length=64)
	donoReserva = models.CharField(max_length=64)


class salaCasdVest(models.Model):
	comecoReserva = models.CharField(max_length=64)
	terminoReserva = models.CharField(max_length=64)
	donoReserva = models.CharField(max_length=64)


class salaCasdinho(models.Model):
	comecoReserva = models.CharField(max_length=64)
	terminoReserva = models.CharField(max_length=64)
	donoReserva = models.CharField(max_length=64)

	
class salaDepCult(models.Model):
	comecoReserva = models.CharField(max_length=64)
	terminoReserva = models.CharField(max_length=64)
	donoReserva = models.CharField(max_length=64)

	