from django.conf.urls import url
from quiz import views
urlpatterns = [
	url(r"^$", views.index),
	url(r"^quiz/([a-z-]+)/$", views.quiz),
	url(r"^quiz/[a-z-]+/question/[0-9]/$", views.question),
	url(r"^quiz/[a-z-]+/result/$", views.result),
]