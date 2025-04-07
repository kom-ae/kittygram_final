from django.contrib.auth import get_user_model
from django.db import models

from constants import (ACHIEVEMENT_MAX_LENGTH, CAT_COLOR_MAX_LENGTH,
                       CAT_NAME_MAX_LENGTH)

User = get_user_model()


class Achievement(models.Model):
    name = models.CharField(max_length=ACHIEVEMENT_MAX_LENGTH)

    class Meta:
        verbose_name = 'достижение'
        verbose_name_plural = 'Достижения'

    def __str__(self):
        return self.name


class Cat(models.Model):
    name = models.CharField(max_length=CAT_NAME_MAX_LENGTH)
    color = models.CharField(max_length=CAT_COLOR_MAX_LENGTH)
    birth_year = models.IntegerField()
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    achievements = models.ManyToManyField(
        Achievement,
        through='AchievementCat'
    )
    image = models.ImageField(
        upload_to='cats/images/',
        null=True,
        default=None
    )

    class Meta:
        verbose_name = 'кот'
        verbose_name_plural = 'Коты'
        default_related_name = 'cats'

    def __str__(self):
        return self.name


class AchievementCat(models.Model):
    achievement = models.ForeignKey(Achievement, on_delete=models.CASCADE)
    cat = models.ForeignKey(Cat, on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'достижение - кот'
        verbose_name_plural = 'Достижения - Коты'
        default_related_name = 'achievementscats'

    def __str__(self):
        return f'{self.achievement} {self.cat}'
