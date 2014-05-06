from django.db import models

# Create your models here.
#Experimental Models 
#Will be replaced
class Blog_Post(models.Model):
	title = models.CharField(max_length=30)
	contents = models.CharField(max_length=250)
	class Admin:
		pass
