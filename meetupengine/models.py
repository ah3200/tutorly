from __future__ import unicode_literals

from django.db import models
from django.core.urlresolvers import reverse
# Create your models here.
from django.contrib.auth.models import User

class Tutor(models.Model):
    user = models.OneToOneField(User, related_name='tutor')
    slug = models.SlugField(max_length=40)
    website = models.URLField(default='', blank=True)
    bio = models.TextField(default='', blank=True)
    phone = models.CharField(max_length=20, blank=True, default='')
    email = models.EmailField(max_length=30, blank=True)
    city = models.CharField(max_length=100, default='', blank=True)
    
    def get_absolute_url(self):
        return reverse('tutor-detail', kwargs={'slug':self.slug})
    
class Student(models.Model):
    user = models.OneToOneField(User, related_name='student')
    bio = models.TextField(default='', blank=True)
    phone = models.CharField(max_length=20, blank=True, default='')
    email = models.EmailField(max_length=30, blank=True)
    city = models.CharField(max_length=100, default='', blank=True)
    
class Course(models.Model):
    name = models.TextField(max_length=50)
    subject = models.TextField(max_length=50)
    slug = models.SlugField(max_length=40, default='course-template')
    level = models.TextField(max_length=10)
    description = models.TextField()
    tutor = models.ForeignKey(Tutor, related_name='tutor')

    def get_absolute_url(self):
        return reverse('course-detail', kwargs={'slug':self.slug})

class Classroom(models.Model):
    course = models.ForeignKey(Course)
    slug = models.SlugField(max_length=40, default='classroom-template')
    location = models.TextField(max_length=50)
    datetime_from = models.DateTimeField()
    datetime_to = models.DateTimeField()
    schedule = models.TextField()
    max_registration = models.IntegerField()
    registered = models.IntegerField()

class Registration(models.Model):
    classroom = models.ForeignKey(Classroom)
    student = models.ForeignKey(Student)
    registration_status = models.TextField(max_length=20)


    


    
    
    