from django.conf.urls import url, include
from django.views.generic import ListView
#from meetupengine.views import TutorListView, TutorDetailView, CourseListView, CourseDetailView
from meetupengine.views import *

urlpatterns = [
    url(r'^$', index, name='index'),
    url(r'^tutor/(?P<page>\d+)?/?$', TutorListView.as_view(paginate_by=10), name='tutor-list'),
    url(r'^tutor/(?P<slug>[-\w]+)/$', TutorDetailView.as_view(), name='tutor-detail'),
    url(r'^course/(?P<page>\d+)?/?$', CourseListView.as_view(paginate_by=10), name='course-list'),
    url(r'^course/(?P<slug>[-\w]+)/$', CourseDetailView.as_view(), name='course-detail'),
    url(r'^classroom/(?P<page>\d+)?/?$', ClassroomListView.as_view(paginate_by=10), name='classroom-list'),
    url(r'^student/(?P<slug>[-\w]+)/$', StudentDetailView.as_view(), name='student-detail'),
    url(r'^create/$', createNewCourse),
]