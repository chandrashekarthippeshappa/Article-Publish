from django.db import models

class Article(models.Model):
	title = models.CharField(max_length=100)
	author = models.CharField(max_length=100)
	published = models.DateField(auto_now=True)
	catogory = models.CharField(max_length=100)
	hero_image = models.ImageField(upload_to = 'profile_image',blank=True)
	optional_image = models.ImageField(upload_to = 'profile_image',blank=True)
	body = models.TextField(blank=True,null=True)


	def __str__(self):
		return self.title