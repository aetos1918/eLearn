from django.contrib.auth.models import User
from django.db import models as m


# Create your models here.

class Subject(m.Model):
    title = m.CharField(max_length=200)
    slug = m.SlugField(max_length=200, unique=True)

    class Meta:
        ordering = ('title',)

    def __str__(self):
        return self.title


class Course(m.Model):
    owner = m.ForeignKey(User, related_name='courses_rerlated')
    subject = m.ForeignKey(Subject,
                           related_name='courses')
    title = m.CharField(max_length=200)
    slug = m.SlugField(max_length=200, unique=True)
    overview = m.TextField()
    created = m.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ('-created',)

    def __str__(self):
        return self.title


class Module(m.Model):
    courses = m.ForeignKey(Course,
                           related_name='modules')
    title = m.CharField(max_length=200)
    description = m.TextField(blank=True)

    def __str__(self):
        return self.title
