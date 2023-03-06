from django.db import models
from django.conf import settings

# from django.contrib.auth.models import User
# from users.models import Profile

AVAILABLE = (
    ("Available", "Available"),
    ("Unavailable", "Unavailable"),
)


class Department(models.Model):
    name = models.CharField(max_length=100)
    
    """author = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
    )"""

    class Meta:
        verbose_name_plural = 'Департаменты'


class Discipline(models.Model):
    name = models.CharField(max_length=100)
    department = models.ForeignKey(
        Department,
        null=True,
        blank=True,
        on_delete=models.CASCADE
    )

    @property
    def get_department(self):
        return self.department

    class Meta:
        verbose_name_plural = 'Дисциплины'


class Course(models.Model):
    class Meta:
        ordering = ['name', 'discipline', 'platform', 'price', 'available', 'link', 'weeks', 'hours']
        verbose_name_plural = 'Курсы'

    discipline = models.ForeignKey(Discipline, null=False, blank=True, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    platform = models.CharField(max_length=100)
    price = models.CharField(max_length=25)
    available = models.CharField(max_length=20, choices=AVAILABLE, default='Available')
    link = models.URLField(max_length=256)
    weeks = models.IntegerField()
    hours = models.IntegerField()

    def __str__(self):
        return f"Course(pk={self.pk}, name={self.name!r}"

    @property
    def get_discipline(self):
        return self.discipline
