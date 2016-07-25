from django.shortcuts import render, redirect
from django.views.generic import ListView, DetailView
from meetupengine.models import Tutor, Course, Classroom, Registration, Student
from meetupengine.forms import CourseForm, ClassroomForm, RegistrationForm, ClassroomFormSet

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
class ClassroomListView(ListView):
    
    template_name = 'meetupengine/classroom_list.html'
    context_object_name = "course"
    
    def get_queryset(self):
        return Course.objects.prefetch_related("classrooms").all()
    
    def get_context_data(self, **kwargs):
        context = super(ClassroomListView, self).get_context_data(**kwargs)
        return context
# Classroom details view

# Student details view
class StudentDetailView(DetailView):
    
    model = Student
    
    def get_context_data(self, **kwargs):
        context = super(StudentDetailView, self).get_context_data(**kwargs)
        return context

# Tutor creates (delete, update) Course 
def createNewCourse(request):
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        course_form = CourseForm(request.POST)
            # check whether it's valid:
        if course_form.is_valid():
            post = course_form.save(commit=False)
            classroom_form = ClassroomFormSet(request.POST, instance=post)
            post.tutor = Tutor.objects.get(user=request.user)
            
            if classroom_form.is_valid():
                post.save()
                classroom_form.save()
            # Without this next line the tags won't be saved.
            #  form.save_m2m()
                return redirect('/course/')
    return render(request,'meetupengine/new_course.html',{'form':CourseForm(),'classroom_form':ClassroomFormSet()})

# Tutor add (delete, update) classrooms
def createNewClassroom(request):
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = ClassroomForm(request.POST)
            # check whether it's valid:
        if form.is_valid():
            post = form.save(commit=False)
#            storypost.pub_date = timezone.now()
#            storypost.site = get_current_site(request)
#            post.tutor = Tutor.objects.get(user=request.user)
            post.save()
            # Without this next line the tags won't be saved.
            #  form.save_m2m()
            return redirect('/course/')
    return render(request,'meetupengine/new_classroom.html',{'form':ClassroomForm()})

# Student registered (drop) classroom

# Studetn search for course/classroom


    
    