from django.db import models

# Create your models here.

# One to one relationship

class Language(models.Model):
	# parent model
	name = models.CharField(max_length = 25)

	def __str__(self):
		return self.name

class Framework(models.Model):
	# child model
	name = models.CharField(max_length = 25)
	language = models.ForeignKey(Language, on_delete=models.CASCADE)

	def __str__(self):
		return f"{self.name}"


# Many to many relationship
# Many movies can have many characters and same character can be part of many movies.

class Movies(models.Model):

	name = models.CharField(max_length=50)

	def __str__(self):
		return self.name

class Characters(models.Model):

	name = models.CharField(max_length=50)
	movies = models.ManyToManyField(Movies)

	def __str__(self):
		return self.name