from django.db import models
from users.models import User

class Quiz(models.Model):
    quiz_master = models.ForeignKey(User, on_delete=models.CASCADE)
    quiz_title = models.CharField(max_length=255,default='New Quiz')
    quiz_desc = models.CharField(max_length=255,default='Quiz Description')
    quiz_created = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.title

class Question(models.Model):
    quiz = models.ForeignKey(Quiz, on_delete=models.CASCADE, related_name='questions')
    prompt = models.TextField()
    p_score=models.IntegerField(default=1)
    n_score=models.IntegerField(default=0)
    type = models.CharField(max_length=255)

    def __str__(self):
        return self.prompt

class QuizResult(models.Model):
    quiz_taker = models.ForeignKey(User, on_delete=models.CASCADE, related_name='taker')
    quiz = models.ForeignKey(Quiz, on_delete=models.CASCADE, related_name='result')
    score = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)

class QuestionAnswer(models.Model): #Create 4 for Each Type
    question = models.ForeignKey(Question, on_delete=models.CASCADE, related_name='answer')
    quiz_result = models.ForeignKey(QuizResult, on_delete=models.CASCADE, related_name='outcome')
    answer = models.TextField()