# coding: utf-8
from django.shortcuts import render
from quiz.models import Quiz


# quizzes = {
# 	"apor": {
#    		"name": u"Ap-quizzet",
# 	   	"description": u"Testa dina kunskaper om våra närmaste släktingar!",
# 	   	"image": u"/static/orangutan.jpg",
# 	},
# 	"cats": {
# 	   	"name": u"Katt-quizzet",
# 	   	"description": u"Vad kan du egentligen om katter?",
# 	   	"image": u"/static/cat.jpg",

# 	},
# 	"pigs": {
# 	    	"name": u"Gris-quizzet",
# 	    	"description": u"Hur mycket kan du om grisar?",
# 	    	"image": u"/static/pig.jpg"	},
# }


# def index(request):
# 	return render(request, "quiz/index.html")
def index(request):
	context = {
	    	"quizzes": Quiz.objects.all(),
	}
	return render(request, "quiz/index.html", context)

def quiz(request, slug):
	context = {
		"quiz": quizzes[slug],
		"quiz_slug": slug,
	}
	return render(request, "quiz/quiz.html", context)

def question(request, slug, number):
	context = {
		"question_number": number,
	    "question": u"Hur många bultar har ölandsbron?",
		"answer1": u"12",
	   	"answer2": u"66 400",
	    "answer3": u"7 428 954",
	    "quiz_slug": slug,
	}
	return render(request, "quiz/question.html", context)


def result(request, slug):
	context = {
	    "correct": 12,
	    "total": 20,
		"quiz_slug": slug,
	}
	return render(request, "quiz/result.html", context)

