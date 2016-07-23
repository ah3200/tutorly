from django.contrib import admin

# Register your models here.
from django.contrib.auth.models import User

from meetupengine.models import Tutor, Student, Course, Classroom, Registration

admin.site.register(Tutor)
admin.site.register(Student)
admin.site.register(Course)
admin.site.register(Classroom)
admin.site.register(Registration)