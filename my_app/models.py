from django.db import models

# Create your models here.
class Review(models.Model):
	title = models.CharField(max_length=50)
	about = models.TextField()
	image = models.ImageField(blank=True, null=True)
	author = models.CharField(max_length=50)


	def __str__(self):
		return self.title