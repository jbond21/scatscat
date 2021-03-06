# Generated by Django 3.0.7 on 2020-12-16 16:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('scat', '0002_auto_20201216_1527'),
    ]

    operations = [
        migrations.AddField(
            model_name='team',
            name='question1',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='question_1', to='scat.Questions'),
        ),
        migrations.AddField(
            model_name='team',
            name='question10',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='question_10', to='scat.Questions'),
        ),
        migrations.AddField(
            model_name='team',
            name='question11',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='question_11', to='scat.Questions'),
        ),
        migrations.AddField(
            model_name='team',
            name='question12',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='question_12', to='scat.Questions'),
        ),
        migrations.AddField(
            model_name='team',
            name='question2',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='question_2', to='scat.Questions'),
        ),
        migrations.AddField(
            model_name='team',
            name='question3',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='question_3', to='scat.Questions'),
        ),
        migrations.AddField(
            model_name='team',
            name='question4',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='question_4', to='scat.Questions'),
        ),
        migrations.AddField(
            model_name='team',
            name='question5',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='question_5', to='scat.Questions'),
        ),
        migrations.AddField(
            model_name='team',
            name='question6',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='question_6', to='scat.Questions'),
        ),
        migrations.AddField(
            model_name='team',
            name='question7',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='question_7', to='scat.Questions'),
        ),
        migrations.AddField(
            model_name='team',
            name='question8',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='question_8', to='scat.Questions'),
        ),
        migrations.AddField(
            model_name='team',
            name='question9',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='question_9', to='scat.Questions'),
        ),
    ]
