from django.conf.urls import url
from quiz import views
urlpatterns = [
	url(r"^$", views.index, name ="start_page"),
	url(r"^quiz/([a-z-]+)/$", views.quiz, name ="quiz_page"),
	url(r"^quiz/([a-z-]+)/question/([0-9]+)/$", views.question, name ="question_page"),
	url(r"^quiz/([a-z-]+)/result/$", views.result, name ="result_page"),
]