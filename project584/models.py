from django.db import models

class Auth(models.Model):
	email = models.EmailField()
	password = CharField(max_length=30)

# class Account_info(models.Model):
# 	username = CharField(max_length=20)
# 	email = EmailField() # FIX: Relier en relation une à une, a email de la classe Auth
# 	visible = BooleanField(default=True) # Si visible est true le bio et tout 
