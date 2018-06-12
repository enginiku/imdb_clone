from django.db import models

# Create your models here.
class Movie(models.Model):
	name = models.CharField(max_length=100)
	director = models.CharField(max_length=60)
	genres = models.CharField(max_length=100)
	imdb_score = models.DecimalField(max_digits=3, decimal_places=1)
	popularity = models.DecimalField(max_digits=3, decimal_places=1)

	class Meta:
		db_table = 'catalogues_movies'