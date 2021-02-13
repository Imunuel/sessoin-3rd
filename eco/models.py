from django.db import models

class Position(models.Model):
    Positions_Name = models.CharField(max_length=50, verbose_name='Название должности')
    Rate = models.FloatField(default=0, verbose_name='Разряд')

    def __str__(self):
        return self.Positions_Name

    class Meta:
        verbose_name = 'Должности'
        verbose_name_plural = 'Должность'
        

class People(models.Model):
    full_name = models.CharField(max_length=100, verbose_name='Полное имя')
    position = models.ForeignKey(Position, on_delete=models.CASCADE, verbose_name='Должность')
    count_young = models.IntegerField(default=0, verbose_name='Количество детей до 18 лет')
    experience = models.IntegerField(default=0, verbose_name='Процент стажа') # стаж
    prize = models.IntegerField(default=0, verbose_name='Процент премии') # премия
    achievements = models.IntegerField(default=0, verbose_name='Процент за достижения') # достижения
    contract = models.IntegerField(default=0, verbose_name='Процент по контракту') # процент по контракту
    time_days = models.IntegerField(default=23, verbose_name='Количество проработанных дней')
    accrued = models.IntegerField(blank=True, default=0, verbose_name='Начисленно')
    salary = models.FloatField(blank=True, default=0, verbose_name='Карт-счет')

    def __str__(self):
        return self.full_name

    def save(self, *args, **kwargs):
        coefficient = {1:1, 2:1.07, 3:1.14, 4:1.21, 5:1.29, 6:1.38, 7:1.47, 8:1.57, 9:1.68, 10:1.79, 11:1.91, 12:2.03, 13:2.17, 14:2.31, 15:2.47, 16:2.63, 17:2.81, 18:3}
        if self.position.Rate in coefficient:
            TS = coefficient[self.position.Rate] * 185
        else:
            TS = 0
        accrued = (TS + (185 * self.experience / 100) + (TS * self.contract / 100) + (TS * self.achievements / 100) + (TS * self.prize / 100))/23 * self.time_days
        self.accrued = accrued
        if accrued < 709:
            if self.count_young > 1:
                tax = (accrued - 117 - (65 * self.count_young)) * 13 / 100
            else:
                tax = (accrued - 117 - (34 * self.count_young)) * 13 / 100
        else:
            if self.count_young > 1:
                tax = (accrued - 110 - (65 * self.count_young)) * 13 / 100
            else:
                tax = (accrued - 110 - (34 * self.count_young)) * 13 / 100
        UF = accrued * 1 / 100
        FSZN = accrued * 1 / 100
        self.salary = accrued - tax - UF - FSZN
        super(People, self).save(*args, **kwargs)

    class Meta:
        verbose_name = 'Работник'
        verbose_name_plural = 'Работники'