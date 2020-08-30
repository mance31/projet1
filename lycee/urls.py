from django.conf.urls import url
from . import views
from django.urls import path
from .views import StudentCreateView, call, editstudent

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^(?P<cursus_id>[0-9]+)$', views.detail, name='detail'),
    # /lycee/student/73
    url(r'^student/(?P<student_id>[0-9]+)$', views.detail_student, name='detail_student'),
    url(r'^student/create/$', StudentCreateView.as_view(), name='create_student'),
    url(r'^edit/(?P<pk>\d+)/$', editstudent.as_view(), name='editstudent'),
    url(r'^call/(?P<presence_id>[0-9]+)$', views.calleffec, name='calleffec'),
    url(r'^call/call/$',call.as_view(),name='call'),
    url(r'^cursuscall/(?P<cursus_id>[0-9]+)$', views.callcursus, name='callcursus'),
    #url(r'^lycee/cursuscall/(?P<presence_id>[0-9]+)$', views.curscalleffect,name='curscalleffect')
]