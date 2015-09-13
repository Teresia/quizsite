from django.db import models

class Quiz(models.Model):
	name = models.CharField(max_length=100)
	slug = models.SlugField(max_length=100)
	image = models.CharField(max_length=100)
	description = models.TextField()


	def __unicode__(self):
		return self.name

class Question(models.Model):
	quiz = models.ForeignKey(Quiz, related_name="questions")
	question = models.TextField()
	answer1 = models.CharField(max_length=100)
	answer2 = models.CharField(max_length=100)
	answer3 = models.CharField(max_length=100)
	correct = models.PositiveIntegerField()

	def __unicode__(self):
		return self.quiz.name + " / " + self.question

class ImageQuestion(models.Model):
	quiz = models.ForeignKey(Quiz, related_name="questions")
	question = models.TextField()
	imageAnswer1 = models.CharField(max_length=100)
	imageAnswer2 = models.CharField(max_length=100)
	correct = models.PositiveIntegerField()

	def __unicode__(self):
		return self.quiz.name + " / " + self.question