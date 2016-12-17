from django.contrib.auth.models import User
from django.db import models as m
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType


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


class Content(m.Model):
    module = m.ForeignKey(Module, related_name='contents')
    content_type = m.ForeignKey(ContentType)
    object_id = m.PositiveIntegerField()
    item = GenericForeignKey('content_type', 'object_id')


class ItemBase(m.Model):
    owner = m.ForeignKey(User, related_name='%(class)s_related')
    title = m.CharField(max_length=250)
    created = m.DateTimeField(auto_now_add=True)
    updated = m.DateTimeField(auto_now=True)

    class Meta:
        abstract = True

    def __str__(self):
        return self.title


class Text(ItemBase):
    content = m.TextField()


class File(ItemBase):
    file = m.FileField(upload_to='files')


class Image(ItemBase):
    file = m.FileField(upload_to='images')


class Video(ItemBase):
    url = m.URLField()
