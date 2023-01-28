# Generated by Django 4.1.4 on 2023-01-28 19:18

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('inv', '0003_remove_multiplecorrectquestion_question_ptr_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Choice',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='UserAnswer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('answer', models.TextField(max_length=255)),
            ],
        ),
        migrations.RenameField(
            model_name='question',
            old_name='n_score',
            new_name='pen',
        ),
        migrations.RenameField(
            model_name='question',
            old_name='p_score',
            new_name='points',
        ),
        migrations.AlterField(
            model_name='quiz',
            name='quiz_master',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='creator', to=settings.AUTH_USER_MODEL),
        ),
        migrations.DeleteModel(
            name='QuestionAnswer',
        ),
        migrations.AddField(
            model_name='useranswer',
            name='question',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='ans1wer', to='inv.question'),
        ),
        migrations.AddField(
            model_name='useranswer',
            name='quiz_result',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='outcome', to='inv.quizresult'),
        ),
    ]