from django.db import models
from users.models import User

class Quiz(models.Model):
    quiz_master = models.ForeignKey(User, on_delete=models.CASCADE,related_name='creator')
    quiz_title = models.CharField(max_length=255,default='New Quiz')
    quiz_desc = models.CharField(max_length=255,default='Quiz Description')
    quiz_created = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.quiz_title

class Question(models.Model):
    quiz = models.ForeignKey(Quiz, on_delete=models.CASCADE, related_name='questions')
    prompt = models.CharField(max_length=255,default='Enter your Question Here')
    type = models.CharField(max_length=255)
    points=models.IntegerField(default=1)
    pen=models.IntegerField(default=0)

    def __str__(self):
        return self.prompt

class QuizResult(models.Model):
    quiz_taker = models.ForeignKey(User, on_delete=models.CASCADE, related_name='taker')
    quiz = models.ForeignKey(Quiz, on_delete=models.CASCADE, related_name='result')
    score = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return (self.quiz_taker,self.quiz,self.score)

class UserAnswer(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE, related_name='ans1wer')
    quiz_result = models.ForeignKey(QuizResult, on_delete=models.CASCADE, related_name='outcome')
    answer = models.TextField(max_length=255)

    def __str__(self):
        return self.answer

class Choice(models.Model):
    pass
