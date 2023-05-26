
from django.urls import path,include
from . import views
app_name='collegeapp'
urlpatterns = [

  path('',views.demo,name='demo'),
  path('login',views.login,name='login'),
  path('logout',views.logout,name='logout'),
  path('home',views.home,name='home'),
  path('dept',views.dept,name='dept'),
  path('formdept',views.formdept,name='formdept'),
  path('get_topics_ajax', views.get_topics_ajax, name="get_topics_ajax"),
  path('register',views.register,name='register'),

]