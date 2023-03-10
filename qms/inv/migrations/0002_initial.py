# Generated by Django 4.1.4 on 2023-01-24 17:33

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('inv', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AddField(
            model_name='quiztaker',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='quiz_takers', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='quizresult',
            name='quiz_taker',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='answers', to='inv.quiztaker'),
        ),
        migrations.AddField(
            model_name='quiz',
            name='quiz_master',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='questionanswer',
            name='question',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='answers', to='inv.question'),
        ),
        migrations.AddField(
            model_name='questionanswer',
            name='quiz_result',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='answers', to='inv.quizresult'),
        ),
        migrations.AddField(
            model_name='question',
            name='question_quiz',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='questions', to='inv.quiz'),
        ),
    ]
