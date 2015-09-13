from django.contrib import admin

# Register your models here.
from django.contrib import admin
from quiz.models import Quiz, Question, ImageQuestion
admin.site.register(Quiz)
admin.site.register(Question)
admin.site.register(ImageQuestion)

