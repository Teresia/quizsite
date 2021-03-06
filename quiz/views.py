# coding: utf-8
from django.shortcuts import render
from quiz.models import Quiz
from django.shortcuts import redirect


# def index(request):
# 	return render(request, "quiz/index.html")
def index(request):
	context = {
			"quizzes": Quiz.objects.all(),
	}
	return render(request, "quiz/index.html", context)

def quiz(request, slug):
	context = {
		"quiz": Quiz.objects.get(slug=slug),
	}
	return render(request, "quiz/quiz.html", context)


def question(request, slug, number):
	number = int(number)
	quiz = Quiz.objects.get(slug=slug)
	questions = quiz.questions.all()
	if request.POST:
		answer = int(request.POST["answer"])
		saved_answers = {}
		if quiz.slug in request.session:
			saved_answers = request.session[quiz.slug]

		saved_answers[str(number)] = answer
		request.session[quiz.slug] = saved_answers

		if questions.count() == number:
				return redirect("result_page", quiz.slug)
		else:
			return redirect("question_page", quiz.slug, number +1)

	question = questions[number - 1]
	context = {
			"question_number": number,
			"question": question.question,
			"answer1": question.answer1,
			"answer2": question.answer2,
			"quiz": quiz,
			"correct": question.correct,
	}
	return render(request, "quiz/question.html", context)





def result(request, slug):
	quiz = Quiz.objects.get(slug=slug)
	questions = quiz.questions.all()
	saved_answers = request.session[slug]
	num_correct_answers = 0
	for counter, question in enumerate(questions):
			if question.correct == saved_answers[str(counter + 1)]:
				num_correct_answers += 1

	context = {
		"correct": num_correct_answers,
		"total": questions.count(),
		"quiz": quiz,
		"questions": quiz.questions.all(),
		"your_answer": saved_answers,
	}
	return render(request, "quiz/result.html", context)


