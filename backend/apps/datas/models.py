from django.db import models

class Industry(models.Model):
	name	= models.CharField(max_length=200, null=True)
	active 	= models.BooleanField(default=True)
	ordre 	= models.IntegerField(default=0)

	def __str__(self):
		return self.name

	class Meta:
		verbose_name = "Secteur d'activité"
		verbose_name_plural = "Liste des secteur d'activité"
		ordering = ['-ordre', 'name']


class Employes(models.Model):
	name 	= models.CharField(max_length=200, null=True)
	active 	= models.BooleanField(default=True)

	def __str__(self):
		return self.name

	class Meta:
		verbose_name = "Nombre d'employés"
		verbose_name_plural = "Liste nombre employés"