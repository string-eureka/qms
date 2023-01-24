from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required, user_passes_test
from users.models import User
from .models import Quiz, Question,QuizResult
from django.contrib import messages

def home(request):
    context={
        Quiz.objects.all()
    }
    return render(request, 'inv/home.html',{'context':context})

def is_quizmaster():
    return User.Quizmaster

def error(request):
    return render(request,'inv/error.html')

@login_required
def view_quiz(request, quiz_id):
    quiz = Quiz.objects.get(pk=quiz_id)
    questions_list = Quiz.questions.all()
    context = Quiz.objects.all()
    return render(request, 'view_quiz.html', {'quiz': quiz, 'questions_list': questions_list,'context': context})

@login_required
@user_passes_test(is_quizmaster,login_url='error')
def create_quiz(request):
    if request.method == 'POST':
        title = request.POST['title']
        desc = request.POST['desc']
        #if
        quiz = Quiz.objects.create(quizmaster=request.user, title=title, desc=desc)
        return redirect('view_quiz', quiz_id=quiz.id)
    else:
        return render(request, 'create_quiz.html')

# @login_required
# @user_passes_test(is_quizmaster)
# def update_quiz(request, quiz_id):
#     quiz = Quiz.objects.get(id=quiz_id)
#     if request.method == 'POST':
#         quiz.title = request.POST['title']
#         quiz.desc = request.POST['description']
#         quiz.save()
#         return redirect('view_quiz', quiz_id=quiz.id)
#     else:
#         return render(request, 'update_quiz.html', {'quiz': quiz})

# @login_required
# @user_passes_test(is_quizmaster)
# def delete_quiz(request, quiz_id):
#     quiz = Quiz.objects.get(id=quiz_id)
#     quiz.delete()
#     return redirect('quiz_list')

# @login_required
# @user_passes_test(is_quizmaster)
# def create_question(request, quiz_id):
#     quiz = Quiz.objects.get(id=quiz_id)
#     if request.method == 'POST':
#         question_text = request.POST['question_text']
#         question_type = request.POST['question_type']
#         if question_type == 'multiple_choice':
#             choice_1 = request.POST['choice_1']
#             choice_2 = request.POST['choice_2']
#             choice_3 = request.POST['choice_3']
#             choice_4 = request.POST['choice_4']
#             correct_choice = request.POST['correct_choice']
#             question = MCQ.objects.create(quiz=quiz, question_text=question_text, question_type=question_type, choice_1=choice_1, choice_2=choice_2, choice_3=choice_3, choice_4=choice_4, correct_choice=correct_choice)
#         elif question_type == 'numerical':
#             correct_answer = request.POST['correct_answer']
#             range = request.POST['range']
#             question = NumericalQuestion.objects.create(quiz=quiz, question_text=question_text, question_type=question_type, correct_answer=correct_answer, range=range)
#         elif question_type == 'true_false':
#             correct_answer = request.POST['correct_answer']
#             question = TrueFalseQuestion.objects.create(quiz=quiz, question_text=question_text, question_type=question_type, correct_answer=correct_answer)
#         elif question_type == 'multiple_correct':
#             choice_1 = request.POST['choice_1']
#             choice_2 = request.POST['choice_2']
#             choice_3 = request.POST['choice_3']
#             choice_4 = request.POST['choice_4']
#             correct_choices = request.POST['correct_choices']
#             question = MultipleCorrectQuestion.objects.create(quiz=quiz, question_text=question_text, question_type=question_type, choice_1=choice_1, choice_2=choice_2, choice_3=choice_3, choice_4=choice_4, correct_choices=correct_choices)
#         return redirect('view_quiz', quiz_id=quiz.id)
#     else:
#         return render(request, 'create_question.html', {'quiz': quiz})

# @login_required
# @user_passes_test(is_quizmaster)
# def update_question(request, question_id):
#     question = Question.objects.get(id=question_id)
#     if request.method == 'POST':
#         question.question_text = request.POST['question_text']
#         question.question_type = request.POST['question_type']
#         if question.question_type == 'multiple_choice':
#             question.choice_1 = request.POST['choice_1']
#             question.choice_2 = request.POST['choice_2']
#             question.choice_3 = request.POST['choice_3']
#             question.choice_4 = request.POST['choice_4']
#             question.correct_choice = request.POST['correct_choice']
#         elif question.question_type == 'numerical':
#             question.correct_answer = request.POST['correct_answer']
#             question.range = request.POST['range']
#         elif question.question_type == 'true_false':
#             question.correct_answer = request.POST['correct_answer']
#         elif question.question_type == 'multiple_correct':
#             question.choice_1 = request.POST['choice_1']
#             question.choice_2 = request.POST['choice_2']
#             question.choice_3 = request.POST['choice_3']
#             question.choice_4 = request.POST['choice_4']
#             question.correct_choices = request.POST['correct_choices']
#         question.save()
#         return redirect('view_quiz', quiz_id=question.quiz.id)
#     else:
#         return render(request, 'update_question.html', {'question': question})

# @login_required
# @user_passes_test(is_quizmaster)
# def delete_question(request, question_id):
#     question = Question.objects.get(id=question_id)
#     quiz_id = question.quiz.id
#     question.delete()
#     return redirect('view_quiz', quiz_id=quiz_id)

# @login_required
# def take_quiz(request, quiz_id):
#     quiz = Quiz.objects.get(id=quiz_id)
#     questions = quiz.questions.all()
#     quiz_taker, created = QuizTaker.objects.get_or_create(user=request.user, quiz=quiz)
#     if request.method == 'POST':
#         for question in questions:
#             answer = request.POST.get(str(question.id))
#             QuizResult.objects.create(quiz_taker=quiz_taker, question=question, answer=answer)
#         return redirect('view_quiz_result', quiz_taker_id=quiz_taker.id)
#     else:
#         return render(request, 'take_quiz.html', {'quiz': quiz, 'questions': questions})

# @login_required
# def view_quiz_result(request, quiz_taker_id):
#     quiz_taker = QuizTaker.objects.get(id=quiz_taker_id)
#     answers = quiz_taker.answers.all()
#     return render(request, 'view_quiz_result.html', {'quiz_taker': quiz_taker, 'answers': answers})