from django.db import models

class Project(models.Model):
	title = models.CharField(max_length=100)
	description = models.TextField()
	image = models.ImageField(upload_to='portfolio/images')
	techno = models.TextField()
	githublink = models.TextField()

	def __str__(self):
		return self.title

class Contact(models.Model):
	name = models.CharField(max_length=200)
	email = models.EmailField(max_length=100)
	phone = models.CharField(max_length=20)
	message = models.TextField(blank=True)

	def __str__(self):
		return self.name		