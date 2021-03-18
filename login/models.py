from django.db import models

from django.contrib.auth.models import User

# Create your models here.
class Users_Profile(models.Model):
	user = models.OneToOneField(User, on_delete=models.CASCADE)

class Services_Users(models.Model):
	number = models.IntegerField(default=0, null=False)
	name = models.CharField(max_length=30, null=True)
	description = models.CharField(max_length=1000, null=True)
	price1 = models.IntegerField(default=0, null=False)
	price2 = models.IntegerField(null=True)
	price3 = models.IntegerField(null=True)
	username = models.ForeignKey(User, on_delete=models.CASCADE, null=True)

	def __str__(self):
		return f'{self.user}\' Profile'