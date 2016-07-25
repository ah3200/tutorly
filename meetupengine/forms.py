from django import forms
from django.forms import inlineformset_factory
from meetupengine.models import Course, Classroom, Registration

class CourseForm(forms.ModelForm):
    class Meta:
        model = Course
        fields = ('name', 'subject', 'level', 'slug', 'description','tutor',)

ClassroomFormSet = inlineformset_factory(Course, Classroom, fields = ('location','datetime_from','datetime_to','schedule','max_registration'))
        
class ClassroomForm(forms.ModelForm):
    class Meta:
        model = Classroom
        fields = ('course','location','datetime_from','datetime_to','schedule')
        
class RegistrationForm(forms.ModelForm):
    class Meta:
        model = Registration
        fields = ('classroom','student')