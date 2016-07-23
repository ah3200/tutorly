from django.shortcuts import render
from django.views.generic import ListView, DetailView
from meetupengine.models import Tutor, Course, Classroom, Registration, Student

# Create your views here.
from django.http import HttpResponse

def index(request):
    return render(request,'meetupengine/index.html')
#    return HttpResponse("Hello, world. You're at the tutor app index.")

# Tutor list view
class TutorListView(ListView):
    
    model = Tutor
    
    def get_context_data(self, **kwargs):
        context = super(TutorListView, self).get_context_data(**kwargs)
#        context['now'] = timezone.now()
        return context
# Tutor details view
class TutorDetailView(DetailView):
    
    model = Tutor
    
    def get_context_data(self, **kwargs):
        context = super(TutorDetailView, self).get_context_data(**kwargs)
        return context
    
# Course list view
class CourseListView(ListView):
    
    model = Course
    
    def get_context_data(self, **kwargs):
        context = super(CourseListView, self).get_context_data(**kwargs)
#        context['now'] = timezone.now()
        return context
# Course details view
class CourseDetailView(DetailView):
    
    model = Course
    
    def get_context_data(self, **kwargs):
        context = super(CourseDetailView, self).get_context_data(**kwargs)
        return context

# Classroom list view

# Classroom details view

# Student list view

# Registration list view