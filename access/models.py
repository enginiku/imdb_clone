from django.db import models

# Create your models here.
class User(models.Model):
	name = models.CharField(max_length=60)
	email = models.CharField(max_length=60)
	is_admin = models.BooleanField()
	api_key = models.CharField(max_length=60)

	class Meta:
		db_table = 'access_users'