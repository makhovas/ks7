# Generated by Django 4.2.6 on 2023-11-22 13:45

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Habits',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('place', models.CharField(help_text='Место, в котором необходимо выполнять привычку.', max_length=255)),
                ('notification_time', models.CharField(choices=[('fifteen', 'За 15 минут'), ('thirty', 'За 30 минут'), ('hour', 'За час'), ('two_hours', 'За 2 часа'), ('day', 'За 24 часа')], default='thirty', help_text='За сколько присылать уведомления до начала привычки', max_length=20)),
                ('time', models.TimeField(help_text='Время, когда необходимо выполнять привычку.')),
                ('action', models.CharField(help_text='Действие, которое представляет из себя привычку.', max_length=255)),
                ('is_reward', models.BooleanField(default=False, help_text='Признак приятной привычки.')),
                ('frequency', models.CharField(choices=[('daily', 'Ежедневная'), ('weekly', 'Еженедельная')], default='daily', help_text='Периодичность выполнения привычки для напоминания в днях.', max_length=20)),
                ('weekday', models.CharField(choices=[('today', 'Сегодня'), ('tomorrow', 'Завтра')], default='today', help_text='Старт выполнения привычки.', max_length=20)),
                ('reward', models.CharField(blank=True, help_text='Вознаграждение за выполнение привычки.', max_length=255)),
                ('estimated_time', models.IntegerField(help_text='Время, которое предположительно потратит пользователь на выполнение привычки.')),
                ('is_public', models.BooleanField(default=False, help_text='Признак публичности привычки.')),
                ('date_of_start', models.DateField(auto_now_add=True)),
                ('is_starting', models.BooleanField(default=False)),
                ('notification', models.CharField(choices=[('telegram', 'Телеграм'), ('email', 'Почта')], default='telegram', help_text='Тип оповещения telegram/email.', max_length=20)),
                ('related_habit', models.ForeignKey(blank=True, help_text='Связанная привычка, если таковая имеется.', null=True, on_delete=django.db.models.deletion.CASCADE, to='habits.habits')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
