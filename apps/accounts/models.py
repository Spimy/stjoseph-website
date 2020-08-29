from django.db import models
from django.contrib.auth.models import AbstractUser


class Role(models.Model):

    STUDENT = 1
    TEACHER = 2
    RECTOR = 3
    STUDENT_COUNCIL = 4
    NEWS_CLUB = 5

    ROLE_CHOICES = (
        (STUDENT, 'student'),
        (TEACHER, 'teacher'),
        (RECTOR, 'rector'),
        (STUDENT_COUNCIL, 'student_council'),
        (NEWS_CLUB, 'news_club'),
    )

    id = models.PositiveSmallIntegerField(
        choices=ROLE_CHOICES,
        primary_key=True
    )

    def __str__(self):
        return self.get_id_display()


class User(AbstractUser):

    avatar = models.ImageField(upload_to='users/avatars', blank=True)
    roles = models.ManyToManyField(Role, related_name='users', blank=True)

    def save(self, *args, **kwargs):
        super(User, self).save(*args, **kwargs)
        if self.roles.count() == 0:
            self.roles.add(Role.objects.get_or_create(id=Role.STUDENT))
            super(User, self).save(*args, **kwargs)

    def __str__(self):
        return self.username
